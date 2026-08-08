import time
from typing import TYPE_CHECKING, Any, ClassVar

from typing_extensions import override

from BaseClasses import Entrance, EntranceType, Item, ItemClassification, Region, Tutorial
from entrance_rando import EntranceRandomizationError, disconnect_entrance_for_randomization, randomize_entrances
from Options import Accessibility
from Utils import Version
from worlds.AutoWorld import WebWorld, World

from .connections import ERGroups, ToemRegion, connection_name_to_id, region_connections, within_region_groups
from .constants import GAME_NAME, TOEM_MAX_GER_ATTEMPTS
from .items import ItemGroup, ItemName, ToemItem, item_name_groups, item_name_to_id, item_table
from .locations import (
    EventName,
    LocationData,
    LocationGroup,
    LocationName,
    ToemLocation,
    event_table,
    location_name_groups,
    location_name_to_id,
    location_table,
    location_to_item_name,
    portrait_locations,
)
from .options import EntranceRandomization, ToemOptions
from .regions import FullRegionName, RegionName
from .rules import init_stamp_requirements, set_entrance_rules, set_location_rules, set_victory_rule

if TYPE_CHECKING:
    from Options import PerGameCommonOptions


class ToemWebWorld(WebWorld):
    theme: ClassVar[str] = "grassFlowers"
    tutorials: list[Tutorial] = [  # noqa: RUF012
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up the TOEM randomizer.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["DrTChops","0xDEAFC0DE"],
        ),
    ]


class ToemWorld(World):
    game: ClassVar[str] = GAME_NAME
    web: ClassVar[WebWorld] = ToemWebWorld()
    options_dataclass: ClassVar[type["PerGameCommonOptions"]] = ToemOptions
    options: ToemOptions
    item_name_groups: ClassVar[dict[str, set[str]]] = item_name_groups
    location_name_groups: ClassVar[dict[str, set[str]]] = location_name_groups
    item_name_to_id: ClassVar[dict[str, int]] = item_name_to_id
    location_name_to_id: ClassVar[dict[str, int]] = location_name_to_id
    origin_region_name: str = FullRegionName.START_MENU
    progressive_stamp_requirements: dict[str, int]
    transitions: dict[str, int] # has to be a str key as that's all json supports
    is_ut: bool
    ut_can_gen_without_yaml = True
    deferred_entrances: dict[str, tuple[Entrance, Region]]
    found_entrances_datastorage_key = "Slot:{player}:TraversedEntrances"

    @override
    def generate_early(self) -> None:
        self.is_ut = getattr(self.multiworld, "generation_is_fake", False)
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            gen_version = Version(*map(int, slot_data["version"].split(".")))
            if gen_version[:2] != self.world_version[:2]:
                raise Exception(
                    f"Toem version error: The version of the apworld used to generate ({slot_data['version']}) "
                    f"does not match the version installed ({self.world_version.as_simple_string()})"
                )
            for key, value in slot_data["options"].items():
                opt = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))
            self.transitions = dict(slot_data["transitions"].items())
        else:
            self.transitions = {}

        if self.options.homelanda_stamp_requirement > 0:
            stamp_name = ItemName.PROGRESSIVE_STAMP if self.options.progressive_stamps else ItemName.HOMELANDA_STAMP
            self.multiworld.local_early_items[self.player][stamp_name] = int(self.options.homelanda_stamp_requirement)
        if self.options.include_items and self.options.honk_attachment_early:
            self.multiworld.early_items[self.player][ItemName.HONK_ATTACHMENT] = 1

    def create_location(self, name: str, data: LocationData) -> ToemLocation | None:
        region = self.get_region(data.region)
        location = ToemLocation(self.player, name, location_name_to_id[name], region)
        region.locations.append(location)
        return location

    def create_event(self, event_name: str, region_name: str, item_name: str | None = None) -> None:
        if item_name is None:
            item_name = event_name
        item = ToemItem(item_name, ItemClassification.progression, None, self.player)
        region = self.get_region(region_name)
        location = ToemLocation(self.player, event_name, None, region)
        location.place_locked_item(item)
        region.locations.append(location)

    @override
    def create_regions(self) -> None:
        regions = {connection.src_region_name for connection in region_connections}
        regions |= {connection.dst_region_name for connection in region_connections}
        for region in regions:
            if self.options.include_basto or not region.startswith(RegionName.BASTO):
                self.multiworld.regions.append(ToemRegion(region, self.player, self.multiworld))

        logic_groups: set[str] = {LocationGroup.QUEST, LocationGroup.COMPENDIUM}
        if self.options.include_items:
            logic_groups.add(LocationGroup.ITEM)
        if self.options.include_cassettes:
            logic_groups.add(LocationGroup.CASSETTE)
        if self.options.include_achievements:
            logic_groups.add(LocationGroup.ACHIEVEMENT)

        for location_name, location_data in location_table.items():
            is_basto = location_name_to_id[location_name] >= location_name_to_id[LocationName.QUEST_BALLOONS]
            if not self.options.include_basto and is_basto:
                continue
            if location_data.group not in logic_groups:
                if location_name in location_to_item_name:
                    item_name = location_to_item_name[location_name]
                    if item_table[item_name].classification & ItemClassification.progression != 0:
                        self.create_event(location_name, location_data.region, item_name)
                elif self.options.include_basto and self.options.include_items and location_name in portrait_locations:
                    self.create_event(location_name, location_data.region)
            else:
                self.create_location(location_name, location_data)

        if self.options.include_basto:
            self.create_event(EventName.BASTO_BONFIRE, FullRegionName.BASTO_BUS_STOP_BOTTOM)
            for event_name, event_data in event_table.items():
                self.create_event(event_name, event_data.region)
        else:
            self.create_event(EventName.TOEM_EXPERIENCED, FullRegionName.MOUNTAIN_TOP_TOEM)

    @override
    def create_item(self, name: str) -> ToemItem:
        return ToemItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    @override
    def create_items(self) -> None:
        itempool: list[Item] = []

        logic_groups: set[str] = {ItemGroup.STAMP, ItemGroup.PHOTO}
        if self.options.include_items:
            logic_groups.add(ItemGroup.ITEM)
        if self.options.include_cassettes:
            logic_groups.add(ItemGroup.CASSETTE)

        for item_name, item_data in item_table.items():
            if (item_data.group not in logic_groups or
                    (not self.options.include_basto and item_data.parent_region == RegionName.BASTO)):
                continue

            quantity = item_data.quantity
            if item_data.group == ItemGroup.STAMP:
                if self.options.progressive_stamps and item_name != ItemName.PROGRESSIVE_STAMP:
                    continue
                if not self.options.progressive_stamps and item_name == ItemName.PROGRESSIVE_STAMP:
                    continue
                if not self.options.include_basto and item_name == ItemName.PROGRESSIVE_STAMP:
                    quantity -= item_table[ItemName.BASTO_STAMP].quantity

            itempool.extend(self.create_item(item_name) for _ in range(quantity))

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        while len(itempool) < total_locations:
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    @override
    def get_filler_item_name(self) -> str:
        return self.random.choice(tuple(item_name_groups[ItemGroup.PHOTO]))

    @override
    def set_rules(self) -> None:
        init_stamp_requirements(self)
        set_location_rules(self)
        set_victory_rule(self)

    @override
    def connect_entrances(self) -> None:
        should_randomize = self.options.entrance_randomization != EntranceRandomization.option_disabled
        for connection in region_connections:
            if not self.options.include_basto and (connection.src_region_name.startswith(RegionName.BASTO)
                                                or connection.dst_region_name.startswith(RegionName.BASTO)):
                continue
            src_region = self.get_region(connection.src_region_name)
            if not should_randomize or connection.group == ERGroups.EXCLUDED:
                dst_region = self.get_region(connection.dst_region_name)
                src_region.connect(dst_region, connection.name)
            else:
                self.generate_entrance_pair(src_region, connection.name, connection.group)
        set_entrance_rules(self)

        if should_randomize:
            if self.is_ut:
                er_targets = {
                    connection_name_to_id[entrance.name]: entrance
                    for region in self.get_regions()
                    for entrance in region.entrances
                    if not entrance.parent_region
                }
                er_exits = {
                    connection_name_to_id[_exit.name]: _exit
                    for region in self.get_regions()
                    for _exit in region.exits
                    if not _exit.connected_region
                }
                self.deferred_entrances = {
                    int(entrance_id): (er_exits[exit_id], er_targets[int(entrance_id)].connected_region)
                    for entrance_id, exit_id in self.transitions.items()
                }
                for er_target in er_targets.values():
                    er_target.connected_region.entrances.remove(er_target)
                if getattr(self.multiworld, "enforce_deferred_connections", "default") == "off":
                    for (_exit, entrance_region) in self.deferred_entrances.values():
                        _exit.connect(entrance_region)
                    self.deferred_entrances = {}
            else:
                if self.options.entrance_randomization == EntranceRandomization.option_within_region:
                    group_lookup = within_region_groups
                start_time = time.perf_counter()
                for i in range(TOEM_MAX_GER_ATTEMPTS):
                    failed = False
                    try:
                        er_state = randomize_entrances(self, True, group_lookup)
                        # Check if all basto day/night regions are reachable
                        if self.options.include_basto and self.options.accessibility != Accessibility.option_minimal:
                            for event_name in event_table:
                                if not self.get_location(event_name).can_reach(er_state.collection_state):
                                    import logging
                                    logging.info("GER event access failure")
                                    failed = True
                                    break
                    except EntranceRandomizationError as err:
                        if i >= TOEM_MAX_GER_ATTEMPTS - 1:
                            raise EntranceRandomizationError(
                                f"Toem failed GER after {TOEM_MAX_GER_ATTEMPTS} attemps."
                            ) from err
                        failed = True
                    if not failed:
                        break
                    for region in self.get_regions():
                        for _exit in region.get_exits():
                            if (_exit.randomization_group != ERGroups.EXCLUDED
                                    and _exit.parent_region
                                    and _exit.connected_region):
                                disconnect_entrance_for_randomization(_exit, _exit.randomization_group)
                else:
                    raise EntranceRandomizationError(f"Toem failed GER after {TOEM_MAX_GER_ATTEMPTS} attemps.")

                end_time = time.perf_counter()
                self.benchmark_time = end_time - start_time
                self.transitions = {
                    str(connection_name_to_id[from_]): connection_name_to_id[to_]
                    for from_, to_ in er_state.pairings
                }

    def generate_entrance_pair(self, region: Region, name: str, group: int):
        exit = region.create_exit(name)
        exit.randomization_group = group
        exit.randomization_type = EntranceType.TWO_WAY
        er_target = region.create_er_target(name)
        er_target.randomization_group = group
        er_target.randomization_type = EntranceType.TWO_WAY

    @override
    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "version": self.world_version.as_simple_string(),
            "options": self.options.as_dict(
                "include_basto",
                "include_items",
                "include_cassettes",
                "include_achievements",
                "progressive_stamps",
                "homelanda_stamp_requirement",
                "oaklaville_stamp_requirement",
                "stanhamn_stamp_requirement",
                "logcity_stamp_requirement",
                "kiiruberg_stamp_requirement",
                "basto_stamp_requirement",
                "honk_attachment_early",
                "entrance_randomization",
            ),
            "transitions": self.transitions
        }

    # UT Integration
    def reconnect_found_entrances(self, key: str, value: Any):
        if value:
            new_entrances = set(self.deferred_entrances) & set(value)
            for entrance_id in new_entrances:
                # check if we just removed the this entrance from it's reverse
                if entrance_id not in self.deferred_entrances:
                    continue
                _exit, entrance_region = self.deferred_entrances[entrance_id]
                _exit.connect(entrance_region)
                reverse_id = connection_name_to_id[_exit.name]
                reverse_exit, reverse_entrance_region = self.deferred_entrances[reverse_id]
                reverse_exit.connect(reverse_entrance_region)
                del self.deferred_entrances[entrance_id]
                del self.deferred_entrances[reverse_id]

    # visualize_regions helpers
    def visualize_regions(self, region_filter = None, entrance_filter = None):
        from Utils import visualize_regions
        root_region = self.get_region(FullRegionName.START_MENU)

        if region_filter:
            saved_region_cache = self.multiworld.regions.region_cache[self.player]
            new_region_cache = {
                region_name: region
                for region_name, region in saved_region_cache.items()
                if region_filter(region)
            }
            self.multiworld.regions.region_cache[self.player] = new_region_cache
            if root_region.name not in new_region_cache:
                root_region = next(region for region in new_region_cache.values()
                                   if "Bus stop" in region.name or "Harbor bottom" in region.name)
        if entrance_filter:
            saved_exits: dict[Region, list[Entrance]] = {}
            for region in self.get_regions():
                saved_exits[region] = region.exits
                region.exits = [_exit for _exit in region.exits if entrance_filter(_exit)]

        state = self.multiworld.get_all_state(allow_partial_entrances=True)
        state.update_reachable_regions(self.player)
        visualize_regions(root_region, "toem.puml", show_entrance_names=True,
                          regions_to_highlight=state.reachable_regions[self.player], detail_other_regions=True)

        if entrance_filter:
            for region, exits in saved_exits.items():
                region.exits = exits
        if region_filter:
            self.multiworld.regions.region_cache[self.player] = saved_region_cache

    def no_helpers_filter(self):
        from .connections import ConnectionName
        last_non_helper = next(i for i, connection in enumerate(region_connections)
                               if connection.name == ConnectionName.JUNGLE_LEFT)
        helper_connections = {connection.name for connection in region_connections[last_non_helper+1:]}
        return lambda _exit: _exit.name not in helper_connections

    def visualize_ger(self, placeable_entrance_regions: set[Region]):
        from collections import deque
        root_region = self.get_region(FullRegionName.START_MENU)
        seen: set[Region] = set()
        regions: deque[Region] = deque((root_region,))
        while regions:
            if (current_region := regions.popleft()) not in seen:
                seen.add(current_region)
                regions.extend(exit_.connected_region for exit_ in current_region.exits if exit_.connected_region)
        unconnected_regions = {region for region in self.get_regions() if region not in seen}
        ignored_regions = unconnected_regions - placeable_entrance_regions

        def region_filter(region):
            return region not in ignored_regions
        self.visualize_regions(region_filter, self.no_helpers_filter())

    def visualize_super_region(self, parent_region: str):
        def region_filter(region):
            return region.name.startswith(f"{parent_region} - ")
        self.visualize_regions(region_filter, self.no_helpers_filter())

from collections.abc import Callable
from typing import TYPE_CHECKING, final

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule

from .items import ItemName, ItemGroup, item_table
from .locations import LocationName, location_table
from .regions import RegionName

if TYPE_CHECKING:
    from . import ToemWorld


@final
class EventName:
    TOEM_EXPERIENCED = "TOEM Experienced"
    BASTO_BONFIRE = "Basto Bonfire"


CollectionRule = Callable[[CollectionState], bool]


def init_stamp_requirements(world: "ToemWorld") -> None:
    if world.options.progressive_stamps:
        world.progressive_stamp_requirements = {}
        total = world.options.homelanda_stamp_requirement
        world.progressive_stamp_requirements[RegionName.HOMELANDA] = total
        total += world.options.oaklaville_stamp_requirement
        world.progressive_stamp_requirements[RegionName.OAKLAVILLE] = total
        total += world.options.stanhamn_stamp_requirement
        world.progressive_stamp_requirements[RegionName.STANHAMN] = total
        total += world.options.logcity_stamp_requirement
        world.progressive_stamp_requirements[RegionName.LOGCITY] = total
        total += world.options.kiiruberg_stamp_requirement
        world.progressive_stamp_requirements[RegionName.KIIRUBERG] = total
        total += world.options.basto_stamp_requirement
        world.progressive_stamp_requirements[RegionName.BASTO] = total


def set_item_rules(world: "ToemWorld") -> None:
    for location in world.get_locations():
        if location.address is None: # skip events
            continue
        if location.name == LocationName.TAPE_SAILORS_TUNE:
            if world.options.progressive_stamps:
                add_rule(location, lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.BASTO]))
            else:
                add_rule(location, lambda state: state.has(ItemName.BASTO_STAMP, world.player, world.options.basto_stamp_requirement))
        item_filter = lambda req: (
            (item_table[req].group == ItemGroup.ITEM and world.options.include_items) or
            (item_table[req].group == ItemGroup.CASSETTE and world.options.include_cassettes)
        )
        requirements = tuple(req for req in location_table[location.name].requirements if item_filter(req))
        if len(requirements) == 0:
            continue
        add_rule(location, lambda state, reqs=requirements: state.has_all(reqs, world.player))
        # require all four ice creams so that you can't use it in the wrong place
        if ItemName.ICE_CREAM in requirements:
            add_rule(location, lambda state: state.has(ItemName.ICE_CREAM, world.player, 4))


def set_entrance_rules(world: "ToemWorld") -> None:
    if world.options.progressive_stamps:
        stamp_entrance_rules: dict[tuple[str, str], CollectionRule] = {
            (RegionName.HOMELANDA, RegionName.OAKLAVILLE): lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.HOMELANDA]),
            (RegionName.OAKLAVILLE, RegionName.STANHAMN): lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.OAKLAVILLE]),
            (RegionName.STANHAMN, RegionName.LOGCITY): lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.STANHAMN]),
            (RegionName.LOGCITY, RegionName.KIIRUBERG): lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.LOGCITY]),
            (RegionName.KIIRUBERG, RegionName.MOUNTAIN_TOP): lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.KIIRUBERG]),
        }
    else:
        stamp_entrance_rules: dict[tuple[str, str], CollectionRule] = {
            (RegionName.HOMELANDA, RegionName.OAKLAVILLE): lambda state: state.has(ItemName.HOMELANDA_STAMP, world.player, world.options.homelanda_stamp_requirement),
            (RegionName.OAKLAVILLE, RegionName.STANHAMN): lambda state: state.has(ItemName.OAKLAVILLE_STAMP, world.player, world.options.oaklaville_stamp_requirement),
            (RegionName.STANHAMN, RegionName.LOGCITY): lambda state: state.has(ItemName.STANHAMN_STAMP, world.player, world.options.stanhamn_stamp_requirement),
            (RegionName.LOGCITY, RegionName.KIIRUBERG): lambda state: state.has(ItemName.LOGCITY_STAMP, world.player, world.options.logcity_stamp_requirement),
            (RegionName.KIIRUBERG, RegionName.MOUNTAIN_TOP): lambda state: state.has(ItemName.KIIRUBERG_STAMP, world.player, world.options.kiiruberg_stamp_requirement),
        }

    for (from_, to_), rule in stamp_entrance_rules.items():
        if to_ == RegionName.BASTO and not world.options.include_basto:
            continue
        set_rule(world.get_entrance(f"{from_} -> {to_}"), rule)

    if world.options.include_items:
        item_entrance_rules: dict[tuple[str, str], CollectionRule] = {
            (RegionName.OAKLAVILLE, RegionName.STANHAMN): lambda state: state.has(ItemName.HONK_ATTACHMENT, world.player),
            (RegionName.MOUNTAIN_TOP, RegionName.BASTO): lambda state: state.has(ItemName.CLIMBING_BOOTS, world.player),
        }
        for (from_, to_), rule in item_entrance_rules.items():
            if to_ == RegionName.BASTO and not world.options.include_basto:
                continue
            add_rule(world.get_entrance(f"{from_} -> {to_}"), rule)


def set_location_rules(world: "ToemWorld") -> None:
    location_rules: dict[str, CollectionRule] = {
        LocationName.QUEST_EXPERIENCE_TOEM: lambda state: state.can_reach_region(RegionName.MOUNTAIN_TOP, world.player),
        LocationName.QUEST_MONSTERS: lambda state: state.can_reach_region(RegionName.KIIRUBERG, world.player),
        LocationName.ITEM_MONSTER_MASK: lambda state: state.can_reach_region(RegionName.KIIRUBERG, world.player),
        LocationName.QUEST_GHOST_HELPER: lambda state: state.can_reach_region(RegionName.LOGCITY, world.player),
        LocationName.CHEEVO_STRONG_AS_AN_OAK: lambda state: state.can_reach_region(RegionName.KIIRUBERG, world.player),
        LocationName.ITEM_FLAG: lambda state: state.can_reach_region(RegionName.KIIRUBERG, world.player),
        LocationName.QUEST_PAINTINGS: lambda state: state.can_reach_region(RegionName.MOUNTAIN_TOP, world.player),
        LocationName.CHEEVO_STORY: lambda state: state.can_reach_region(RegionName.MOUNTAIN_TOP, world.player),
    }

    valid_locations = set(location.name for location in world.get_locations())
    for location_name, rule in location_rules.items():
        if location_name in valid_locations:
            add_rule(world.get_location(location_name), rule)


def set_victory_rule(world: "ToemWorld") -> None:
    if world.options.include_basto:
        victory_event_name = EventName.BASTO_BONFIRE
        if world.options.progressive_stamps:
            victory_rule = lambda state: (
                (not world.options.include_items or state.has(ItemName.WATERGUN, world.player)) and
                state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.BASTO])
            )
        else:
            victory_rule = lambda state: (
                (not world.options.include_items or state.has(ItemName.WATERGUN, world.player)) and
                state.has(ItemName.BASTO_STAMP, world.player, world.options.basto_stamp_requirement)
            )
    else:
        victory_event_name = EventName.TOEM_EXPERIENCED
        victory_rule = lambda state: not world.options.include_items or state.has(ItemName.CLIMBING_BOOTS, world.player)

    set_rule(world.get_location(victory_event_name), victory_rule)
    world.multiworld.completion_condition[world.player] = lambda state: state.has(
        victory_event_name,
        world.player,
    )

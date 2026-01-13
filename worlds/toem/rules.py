from collections.abc import Callable
from typing import TYPE_CHECKING, final

from BaseClasses import CollectionState, Region
from worlds.generic.Rules import set_rule, add_rule

from .items import ItemName, ItemGroup, item_table
from .locations import LocationName, LocationGroup, location_table, item_to_location_name
from .regions import FullRegionName, RegionName
from .connections import region_connections

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

ratskullz_locations = (
    FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_CROSSWALK, FullRegionName.LOGCITY_OVERPASS, 
    FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_RATSKULLZ_ALLEY, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, 
    FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_OUTSIDE_GALLERY
)

def collect_requirements_regions(requirments: tuple[str | tuple[str]], world: "ToemWorld") -> set[Region]:
    def collect_requirement_regions(requirment: str) -> set[Region]:
        if requirment in location_table:
            regions = collect_requirements_regions(location_table[requirment].requirements, world)
            regions.add(world.get_region(location_table[requirment].region))
            return regions
        elif requirment in item_table:
            if requirment==ItemName.ICE_CREAM and not world.options.include_items:
                # require all four ice creams so that you can't use it in the wrong place
                new_requirements = (location_table[LocationName.ITEM_ICE_CREAM_BANAKIN].requirements + 
                    location_table[LocationName.ITEM_ICE_CREAM_MELONEAR].requirements +
                    location_table[LocationName.ITEM_ICE_CREAM_BEANUT].requirements +
                    location_table[LocationName.ITEM_ICE_CREAM_ORANGANAS].requirements)
                regions = collect_requirements_regions(new_requirements, world)
                regions.add(world.get_region(FullRegionName.BASTO_OUTSIDE_CASTLE))
                return regions
            if (item_table[requirment].group == ItemGroup.ITEM and not world.options.include_items or
                item_table[requirment].group == ItemGroup.CASSETTE and not world.options.include_cassettes):
                return collect_requirement_regions(item_to_location_name[requirment])
            return set()
        else:
            return {world.get_region(requirment)}
    
    regions = set()
    for req in requirments:
        if isinstance(req, tuple):
            for or_req in req:
                regions.update(collect_requirement_regions(or_req))
        else:
            regions.update(collect_requirement_regions(req))
    return regions

def check_requirements(state: CollectionState, requirments: tuple[str | tuple[str]], world: "ToemWorld") -> bool:
    def check_requirement(requirment: str) -> bool:
        if requirment in location_table:
            location = location_table[requirment]
            if (location.group == LocationGroup.ITEM and not world.options.include_items or
                location.group == LocationGroup.CASSETTE and not world.options.include_cassettes or
                location.group == LocationGroup.ACHIEVEMENT and not world.options.include_achievements):
                return state.can_reach_region(location.region, world.player) and check_requirements(state, location.requirements, world)
            return state.can_reach_location(requirment, world.player)
        elif requirment in item_table:
            if requirment==ItemName.ICE_CREAM:
                # require all four ice creams so that you can't use it in the wrong place
                if not world.options.include_items:
                    new_requirements = (location_table[LocationName.ITEM_ICE_CREAM_BANAKIN].requirements + 
                        location_table[LocationName.ITEM_ICE_CREAM_MELONEAR].requirements +
                        location_table[LocationName.ITEM_ICE_CREAM_BEANUT].requirements +
                        location_table[LocationName.ITEM_ICE_CREAM_ORANGANAS].requirements)
                    return check_requirements(state, new_requirements, world)
                return state.has(requirment, world.player, 4)
            if (item_table[requirment].group == ItemGroup.ITEM and not world.options.include_items or
                item_table[requirment].group == ItemGroup.CASSETTE and not world.options.include_cassettes):
                return check_requirements(state, location_table[item_to_location_name[requirment]].requirements, world)
            return state.has(requirment, world.player)
        return state.can_reach_region(requirment, world.player)
    
    for req in requirments:
        if isinstance(req, tuple):
            for or_req in req:
                if check_requirement(or_req):
                    break
            else:
                return False
        elif not check_requirement(req):
            return False
    return True

def set_location_rules(world: "ToemWorld") -> None:
    for location in world.get_locations():
        if location.address is None: # skip events
            continue
        if location.name == LocationName.TAPE_SAILORS_TUNE:
            if world.options.progressive_stamps:
                add_rule(location, lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.BASTO]))
            else:
                add_rule(location, lambda state: state.has(ItemName.BASTO_STAMP, world.player, world.options.basto_stamp_requirement))
        elif location.name == LocationName.QUEST_RATSKULLZ:
            add_rule(location, lambda state: sum(state.can_reach_region(loc, world.player) for loc in ratskullz_locations) >= 5)

        requirements = location_table[location.name].requirements
        if len(requirements) == 0:
            continue
        add_rule(location, lambda state, reqs=requirements: check_requirements(state, reqs, world))


def set_entrance_rules(world: "ToemWorld") -> None:
    if world.options.progressive_stamps:
        stamp_entrance_rules: dict[str, CollectionRule] = {
            "Oaklaville bus stop": lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.HOMELANDA]),
            "Stanhamn bus stop": lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.OAKLAVILLE]),
            "Logcity bus stop": lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.STANHAMN]),
            "Kiiruberg bus stop": lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.LOGCITY]),
            "Mountain top bus stop": lambda state: state.has(ItemName.PROGRESSIVE_STAMP, world.player, world.progressive_stamp_requirements[RegionName.KIIRUBERG]),
        }
    else:
        stamp_entrance_rules: dict[str, CollectionRule] = {
            "Oaklaville bus stop": lambda state: state.has(ItemName.HOMELANDA_STAMP, world.player, world.options.homelanda_stamp_requirement),
            "Stanhamn bus stop": lambda state: state.has(ItemName.OAKLAVILLE_STAMP, world.player, world.options.oaklaville_stamp_requirement),
            "Logcity bus stop": lambda state: state.has(ItemName.STANHAMN_STAMP, world.player, world.options.stanhamn_stamp_requirement),
            "Kiiruberg bus stop": lambda state: state.has(ItemName.LOGCITY_STAMP, world.player, world.options.logcity_stamp_requirement),
            "Mountain top bus stop": lambda state: state.has(ItemName.KIIRUBERG_STAMP, world.player, world.options.kiiruberg_stamp_requirement),
        }

    for entrance, rule in stamp_entrance_rules.items():
        set_rule(world.get_entrance(entrance), rule)

    for parent, sub_regions in region_connections.items():
        if not world.options.include_basto and parent == RegionName.BASTO:
            continue
        for _, connections in sub_regions.items():
            for connection in connections:
                if not world.options.include_basto and connection.dst_region_name == FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY:
                    continue
                requirements = connection.requirements
                if len(requirements) == 0:
                    continue
                rule = lambda state, reqs=requirements: check_requirements(state, reqs, world)
                entrance = world.get_entrance(connection.name)
                add_rule(entrance, rule)
                regions = collect_requirements_regions(requirements, world)
                for region in regions:
                    world.multiworld.register_indirect_condition(region, entrance)

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
        victory_rule = lambda state: check_requirements(state, (LocationName.QUEST_EXPERIENCE_TOEM,), world)

    set_rule(world.get_location(victory_event_name), victory_rule)
    world.multiworld.completion_condition[world.player] = lambda state: state.has(
        victory_event_name,
        world.player,
    )

from collections import deque
from typing import TYPE_CHECKING
from typing_extensions import override
from dataclasses import dataclass
from copy import deepcopy

from BaseClasses import CollectionState, Region, Entrance
from rule_builder.rules import Rule, Has, CanReachLocation, NestedRule, HasAll, HasAny, And, Or, CanReachRegion

from .constants import GAME_NAME
from .locations import LocationName, EventName, EventData, event_table, location_table, bonfire_rule, location_to_item_name
from .items import ItemName, ItemGroup, item_table
from .regions import FullRegionName, RegionName
from .connections import region_connections

if TYPE_CHECKING:
    from . import ToemWorld


def init_stamp_requirements(world: "ToemWorld") -> None:
    if world.options.progressive_stamps:
        world.progressive_stamp_requirements = {}
        total = world.options.homelanda_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.HOMELANDA] = total
        total += world.options.oaklaville_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.OAKLAVILLE] = total
        total += world.options.stanhamn_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.STANHAMN] = total
        total += world.options.logcity_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.LOGCITY] = total
        total += world.options.kiiruberg_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.KIIRUBERG] = total
        total += world.options.basto_stamp_requirement.value
        world.progressive_stamp_requirements[RegionName.BASTO] = total

basto_bed_regions = {FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_TENT, FullRegionName.BASTO_OUTSIDE_CASTLE, 
        FullRegionName.BASTO_GYM_HOUSE, FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_JUNGLE}

@dataclass()
class BastoDayNightRule(Rule["ToemWorld"], game=GAME_NAME):
    
    event_data: EventData

    @override
    def _instantiate(self, world: "ToemWorld") -> Rule.Resolved:
        return self.Resolved(self.event_data.region, self.event_data.is_day, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        event_region_name: str
        is_day: bool

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            event_region = state.multiworld.get_region(self.event_region_name, self.player)
            queue: deque[Region] = deque([event_region])
            seen = {event_region}
            while queue:
                region = queue.popleft()
                for entrance in region.entrances:
                    if entrance.parent_region and entrance.parent_region not in seen and entrance.can_reach(state):
                        if entrance.name == "Lily pad pond night bridge from right":
                            if not self.is_day:
                                return True
                        elif entrance.name == "Bonfire day bridge from top":
                            if self.is_day:
                                return True
                        elif not entrance.parent_region.name.startswith(RegionName.BASTO):
                            if self.is_day:
                                return True
                        elif entrance.parent_region.name in basto_bed_regions:
                            return True
                        else:
                            seen.add(entrance.parent_region)
                            queue.append(entrance.parent_region)
            return False
        
        #@override
        #def region_dependencies(self) -> dict[str, set[int]]:
        #    return {region: {id(self)} for region in ratskullz_regions}

# TODO implement event item instead of subsituting
def expand_location(world: "ToemWorld", location_name: str) -> Rule:
    rule = CanReachRegion(location_table[location_name].region)
    if location_table[location_name].rule is not None:
        rule &= substitute_rule(world, location_table[location_name].rule)
    return rule

item_to_location_name = {v: k for k, v in location_to_item_name.items()}
def substitute_item(world: "ToemWorld", item_name: str, original_rule: Rule) -> Rule:
    if not world.options.include_cassettes and item_name == ItemName.FISHERMANS_WHISTLE_TAPE:
        return expand_location(world, LocationName.TAPE_FISHERMANS_WHISTLE)
    if not world.options.include_items and item_name in item_table and item_table[item_name].group == ItemGroup.ITEM:
        if item_name == ItemName.ICE_CREAM:
            ice_creams = [LocationName.ITEM_ICE_CREAM_BANAKIN, LocationName.ITEM_ICE_CREAM_MELONEAR, LocationName.ITEM_ICE_CREAM_BEANUT, LocationName.ITEM_ICE_CREAM_ORANGANAS]
            return And(*[expand_location(world, ice_cream) for ice_cream in ice_creams])
        return expand_location(world, item_to_location_name[item_name])
    return original_rule

def substitute_location(world: "ToemWorld", original_rule: CanReachLocation) -> Rule:
    if not world.options.include_achievements and original_rule.location_name.startswith("Achievement"):
        return expand_location(world, original_rule.location_name)
    return original_rule

def substitute_rule(world: "ToemWorld", original_rule: Rule) -> Rule:
    rule = deepcopy(original_rule)
    if isinstance(rule, NestedRule):
        rule.children = tuple(substitute_rule(world, child) for child in rule.children)
    elif isinstance(rule, Has):
        rule = substitute_item(world, rule.item_name, rule)
    elif isinstance(rule, HasAll):
        rule = And(*[substitute_item(world, item_name, Has(item_name)) for item_name in rule.item_names], options=rule.options, filtered_resolution=rule.filtered_resolution)
    elif isinstance(rule, HasAny):
        rule = Or(*[substitute_item(world, item_name, Has(item_name)) for item_name in rule.item_names], options=rule.options, filtered_resolution=rule.filtered_resolution)
    elif isinstance(rule, CanReachLocation):
        rule = substitute_location(world, rule)
    return rule

def substitute_rule(world: "ToemWorld", original_rule: Rule) -> Rule:
    rule = deepcopy(original_rule)
    if isinstance(rule, NestedRule):
        rule.children = tuple(substitute_rule(world, child) for child in rule.children)
    elif isinstance(rule, Has):
        rule = substitute_item(world, rule.item_name, rule)
    elif isinstance(rule, HasAll):
        rule = And(*[substitute_item(world, item_name, Has(item_name)) for item_name in rule.item_names], options=rule.options, filtered_resolution=rule.filtered_resolution)
    elif isinstance(rule, HasAny):
        rule = Or(*[substitute_item(world, item_name, Has(item_name)) for item_name in rule.item_names], options=rule.options, filtered_resolution=rule.filtered_resolution)
    elif isinstance(rule, CanReachLocation):
        rule = substitute_location(world, rule)
    return rule

def set_location_rules(world: "ToemWorld") -> None:
    for location in world.get_locations():
        if location.name not in location_table: # skip pure events
            continue
        rule = location_table[location.name].rule
        if rule is not None:
            world.set_rule(location, substitute_rule(world, rule))

    if world.options.include_basto:
        for event_name, event_data in event_table.items():
            world.set_rule(world.get_location(event_name), BastoDayNightRule(event_data))

def secondary_indirects(world: "ToemWorld", resolved_rule: Rule.Resolved, entrance: Entrance) -> None:
    if isinstance(resolved_rule, NestedRule.Resolved):
        for child in resolved_rule.children:
            secondary_indirects(world, child, entrance)
    elif isinstance(resolved_rule, CanReachLocation.Resolved):
        location_rule = world.get_location(resolved_rule.location_name).access_rule
        if isinstance(location_rule, Rule.Resolved):
            for region in location_rule.region_dependencies().keys():
                world.multiworld.register_indirect_condition(world.get_region(region), entrance)
            secondary_indirects(world, location_rule, entrance)

def set_entrance_rules(world: "ToemWorld") -> None:
    for connection in region_connections:
        if not world.options.include_basto and (connection.src_region_name.startswith(RegionName.BASTO)
                                             or connection.dst_region_name.startswith(RegionName.BASTO)):
            continue
        if connection.rule is not None:
            rule = substitute_rule(world, connection.rule)
            entrance = world.get_entrance(connection.name)
            world.set_rule(entrance, rule)
            secondary_indirects(world, entrance.access_rule, entrance)

def set_victory_rule(world: "ToemWorld") -> None:
    if world.options.include_basto:
        victory_event_name = EventName.BASTO_BONFIRE
        victory_rule = substitute_rule(world, bonfire_rule)
    else:
        victory_event_name = EventName.TOEM_EXPERIENCED
        victory_rule = CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)

    world.set_rule(world.get_location(victory_event_name), victory_rule)
    world.set_completion_rule(Has(victory_event_name))

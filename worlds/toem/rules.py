from collections import deque
from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import override

from BaseClasses import CollectionState, Entrance, Region
from rule_builder.rules import CanReachLocation, Has, NestedRule, Rule

from .connections import all_connections
from .constants import GAME_NAME
from .locations import (
    EventData,
    EventName,
    LocationName,
    bonfire_rule,
    event_table,
    location_table,
)
from .regions import Area, RegionName

if TYPE_CHECKING:
    from . import ToemWorld


def init_stamp_requirements(world: "ToemWorld") -> None:
    if world.options.progressive_stamps:
        world.progressive_stamp_requirements = {}
        total = world.options.homelanda_stamp_requirement.value
        world.progressive_stamp_requirements[Area.HOMELANDA] = total
        total += world.options.oaklaville_stamp_requirement.value
        world.progressive_stamp_requirements[Area.OAKLAVILLE] = total
        total += world.options.stanhamn_stamp_requirement.value
        world.progressive_stamp_requirements[Area.STANHAMN] = total
        total += world.options.logcity_stamp_requirement.value
        world.progressive_stamp_requirements[Area.LOGCITY] = total
        total += world.options.kiiruberg_stamp_requirement.value
        world.progressive_stamp_requirements[Area.KIIRUBERG] = total
        total += world.options.basto_stamp_requirement.value
        world.progressive_stamp_requirements[Area.BASTO] = total

basto_bed_regions = {
    RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_TENT, RegionName.BASTO_OUTSIDE_CASTLE,
    RegionName.BASTO_GYM_HOUSE, RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_JUNGLE
}

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
                        elif not entrance.parent_region.name.startswith(Area.BASTO):
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

def set_location_rules(world: "ToemWorld") -> None:
    for location in world.get_locations():
        if location.name not in location_table: # skip pure events
            continue
        rule = location_table[location.name].rule
        if rule is not None:
            world.set_rule(location, rule)

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
    for connection_name, connection in all_connections.items():
        if not world.options.include_basto and (connection.src_region_name.startswith(Area.BASTO)
                                             or connection.dst_region_name.startswith(Area.BASTO)):
            continue
        if connection.rule is not None:
            entrance = world.get_entrance(connection_name)
            world.set_rule(entrance, connection.rule)
            secondary_indirects(world, entrance.access_rule, entrance)

def set_victory_rule(world: "ToemWorld") -> None:
    if world.options.include_basto:
        victory_event_name = EventName.BASTO_BONFIRE
        victory_rule = bonfire_rule
    else:
        victory_event_name = EventName.TOEM_EXPERIENCED
        victory_rule = CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)

    world.set_rule(world.get_location(victory_event_name), victory_rule)
    world.set_completion_rule(Has(victory_event_name))

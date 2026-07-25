from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar, final

from BaseClasses import Entrance, Region
from entrance_rando import ERPlacementState
from rule_builder.rules import CanReachLocation, CanReachRegion, Has, HasAll, Rule

from .items import ItemName
from .locations import EventName, LocationName, get_stamp_rule
from .regions import (
    FullRegionName,
    RegionName,
    basto_regions,
    kiiruberg_regions,
    logcity_regions,
    mountain_top_regions,
    oaklaville_regions,
    stanhamn_regions,
)


class ERGroups(IntEnum):
    EXCLUDED = 0
    # Areas
    HOMELANDA = 1
    OAKLAVILLE = 2
    STANHAMN = 3
    LOGCITY = 4
    KIIRUBERG = 5
    MOUNTAIN_TOP = 6
    BASTO = 7

within_region_groups: dict[ERGroups, list[ERGroups]] = {
    ERGroups.HOMELANDA: [ERGroups.HOMELANDA],
    ERGroups.OAKLAVILLE: [ERGroups.OAKLAVILLE],
    ERGroups.STANHAMN: [ERGroups.STANHAMN],
    ERGroups.LOGCITY: [ERGroups.LOGCITY],
    ERGroups.KIIRUBERG: [ERGroups.KIIRUBERG],
    ERGroups.MOUNTAIN_TOP: [ERGroups.MOUNTAIN_TOP],
    ERGroups.BASTO: [ERGroups.BASTO],
}

@dataclass(frozen=True)
class Connection:
    src_region_name: str
    dst_region_name: str
    name: str
    group: int
    rule: Rule | None = None

@final
class ConnectionName:
    # Menu
    START_GAME = "Start game"

    # Homelanda
    PLAYER_ROOM_EXIT = "Player room exit"
    PLAYER_ROOM_ENTRANCE = "Player room entrance"
    HOMELANDA_HOUSE_EXIT = "Homelanda house exit"
    HOMELANDA_HOUSE_ENTRANCE = "Homelanda house entrance"
    OAKLAVILLE_BUS_STOP = "Oaklaville bus stop"

    # Oaklaville
    STANHAMN_BUS_STOP = "Stanhamn bus stop"
    OAKLAVILLE_BUS_STOP_EXIT = "Oaklaville bus stop exit"
    OUTSIDE_HOTEL_DOWN = "Outside hotel down"
    OUTSIDE_HOTEL_LEFT = "Outside hotel left"
    OUTSIDE_HOTEL_RIGHT = "Outside hotel right"
    HOTEL_ENTRANCE = "Hotel entrance"
    HOTEL_EXIT = "Hotel exit"
    HOTEL_ELEVATOR_ENTRANCE = "Hotel elevator entrance"
    HOTEL_ELEVATOR_EXIT = "Hotel elevator exit"
    GHOST_CUP_GAME_RIGHT = "Ghost cup game right"
    MUSHROOM_HOUSE_ENTRANCE = "Mushroom house entrance"
    GHOST_CUP_GAME_LEFT = "Ghost cup game left"
    MUSHROOM_HOUSE_EXIT = "Mushroom house exit"
    HIDE_AND_SEEK_RIGHT = "Hide and seek right"
    HIDE_AND_SEEK_LEFT = "Hide and seek left"
    GRAVEYARD_RIGHT = "Graveyard right"
    SKELETON_HOUSE_ENTRANCE = "Skeleton house entrance"
    SKELETON_HOUSE_EXIT = "Skeleton house exit"
    SKELETON_HOUSE_BALCONY_EXIT = "Skeleton house balcony exit"
    SKELETON_HOUSE_BALCONY_ENTRANCE = "Skeleton house balcony entrance"
    SCOUT_CAMP_LEFT = "Scout camp left"
    SCOUT_CAMP_UP = "Scout camp up"
    SCOUT_CAMP_RIGHT = "Scout camp right"
    OAKLAVILLE_TRAIL_LOG_FROM_TOP = "Oaklaville trail log from top"
    OAKLAVILLE_TRAIL_UP = "Oaklaville trail up"
    OAKLAVILLE_TRAIL_LOG_FROM_BOTTOM = "Oaklaville trail log from bottom"
    OAKLAVILLE_TRAIL_DOWN = "Oaklaville trail down"
    LOOKOUT_EXIT = "Lookout exit"
    PLAYGROUND_LEFT = "Playground left"
    PLAYGROUND_RIGHT = "Playground right"
    RAVE_BOUNCER_FROM_TOP = "Rave bouncer from top"
    RAVE_ENTRANCE = "Rave entrance"
    RAVE_BOUNCER_FROM_BOTTOM = "Rave bouncer from bottom"
    OUTSIDE_RAVE_LEFT = "Outside rave left"
    RAVE_EXIT = "Rave exit"

    # Stanhamn
    LOGCITY_BUS_STOP = "Logcity bus stop"
    PHOTO_GUILD_HUT_ENTRANCE = "Photo guild hut entrance"
    STANHAMN_BUS_STOP_LEFT = "Stanhamn bus stop left"
    STANHAMN_BUS_STOP_RIGHT = "Stanhamn bus stop right"
    RAFT_UP = "Raft up"
    PHOTO_GUILD_HUT_EXIT = "Photo guild hut exit"
    PIRATE_DRAWBRIDGE_RIGHT = "Pirate Drawbridge right"
    PIRATE_DRAWBRIDGE_LEFT = "Pirate Drawbridge left"
    HIPPO_BEACH_RIGHT = "Hippo beach right"
    HIPPO_BEACH_MANHOLE = "Hippo beach manhole"
    HIPPO_BEACH_LEFT = "Hippo beach left"
    UNDERWATER_EXIT = "Underwater exit"
    OUTSIDE_LIGHTHOUSE_RIGHT = "Outside lighthouse right"
    OUTSIDE_LIGHTHOUSE_UP = "Outside lighthouse up"
    LIGHTHOUSE_ENTRANCE = "Lighthouse entrance"
    LIGHTHOUSE_EXIT = "Lighthouse exit"
    LIGHTHOUSE_ROOF_ENTRANCE = "Lighthouse roof entrance"
    LIGHTHOUSE_ROOF_EXIT = "Lighthouse roof exit"
    KING_FISH_BEACH_EXIT = "King fish beach exit"
    DOCKS_LEFT_EXIT = "Docks left exit"
    VIKING_EXPRESS_STAMHAMN_STOP = "Viking express Stamhamn stop"
    DOCKS_DRAWBRIDGE_FROM_LEFT = "Docks drawbridge from left"
    DOCKS_RIGHT_EXIT = "Docks right exit"
    DOCKS_DRAWBRIDGE_FROM_RIGHT = "Docks drawbridge from right"
    FISHING_TOWER_LEFT = "Fishing tower left"
    FISHING_TOWER_UP = "Fishing tower up"
    GHOST_DRAWBRIDGE_LEFT = "Ghost drawbridge left"
    GHOST_DRAWBRIDGE_FROM_TOP = "Ghost drawbridge from top"
    GHOST_DRAWBRIDGE_DOWN = "Ghost drawbridge down"
    GHOST_DRAWBRIDGE_FROM_BOTTOM = "Ghost drawbridge from bottom"
    RAFT_DOWN = "Raft down"
    HYDROPLANT_ENTRANCE = "Hydroplant entrance"
    OUTSIDE_HYDROPLANT_RIGHT = "Outside hydroplant right"
    HYDROPLANT_EXIT = "Hydroplant exit"

    # Logcity
    KIIRUBERG_BUS_STOP = "Kiiruberg bus stop"
    ESCALATOR_UP = "Escalator up"
    LOGCITY_BUS_STOP_ENTRANCE = "Logcity bus stop entrance"
    CLOCK_TOWER_LEFT = "Clock tower left"
    CLOCK_TOWER_UP = "Clock tower up"
    CLOCK_TOWER_RIGHT = "Clock tower right"
    CROSS_WALK_RIGHT = "Cross walk right"
    CROSS_WALK_UP = "Cross walk up"
    OVERPASS_DOWN = "Overpass down"
    NEWS_HOUSE_ENTRANCE = "News house entrance"
    OVERPASS_UP = "Overpass up"
    OVERPASS_RIGHT = "Overpass right"
    NEWS_HOUSE_EXIT = "News house exit"
    SKATE_PARK_DOWN = "Skate park down"
    SKATE_PARK_RIGHT = "Skate park right"
    SKATE_PARK_TAXI = "Skate park taxi"
    RATSKULLZ_ALLEY_EXIT = "Ratskullz alley exit"
    FASHION_SHOW_ENTRANCE = "Fashion show entrance"
    OUTSIDE_FASHION_SHOW_DOWN = "Outside fashion show down"
    OUTSIDE_FASHION_SHOW_LEFT = "Outside fashion show left"
    OUTSIDE_FASHION_SHOW_RIGHT = "Outside fashion show right"
    FASHION_SHOW_SECURITY_FROM_TOP = "Fashion show security from top"
    FASHION_SHOW_BACKSTAGE_ENTRANCE = "Fashion show backstage entrance"
    FASHION_SHOW_SECURITY_FROM_BOTTOM = "Fashion show security from bottom"
    FASHION_SHOW_EXIT = "Fashion show exit"
    FASHION_SHOW_BACKSTAGE_EXIT = "Fashion show backstage exit"
    CAFE_ENTRANCE = "Cafe entrance"
    OUTSIDE_CAFE_LEFT = "Outside cafe left"
    OUTSIDE_CAFE_UP = "Outside cafe up"
    OUTSIDE_CAFE_TAXI = "Outside cafe taxi"
    CAFE_EXIT = "Cafe exit"
    GALLERY_ENTRANCE = "Gallery entrance"
    OUTSIDE_GALLERY_SHOW_DOWN = "Outside gallery show down"
    OUTSIDE_GALLERY_SHOW_LEFT = "Outside gallery show left"
    GALLERY_EXIT = "Gallery exit"

    # Kiiruberg
    MOUNTAIN_TOP_BUS_STOP = "Mountain top bus stop"
    KIIRUBERG_BUS_STOP_UP = "Kiiruberg bus stop up"
    BIRTHDAY_PARTY_ROPE_FROM_BOTTOM = "Birthday party rope from bottom"
    BALLOON_HOUSE_ENTRANCE = "Balloon house entrance"
    BIRTHDAY_PARTY_DOWN = "Birthday party down"
    BIRTHDAY_PARTY_LEFT = "Birthday party left"
    BIRTHDAY_PARTY_RIGHT = "Birthday party right"
    BIRTHDAY_PARTY_ROPE_FROM_TOP = "Birthday party rope from top"
    BIRTHDAY_PARTY_UP = "Birthday party up"
    BALLOON_HOUSE_EXIT = "Balloon house exit"
    OLD_MANS_HOUSE_ENTRANCE = "Old man's house entrance"
    FROZEN_POND_RIGHT = "Frozen pond right"
    OLD_MANS_HOUSE_EXIT = "Old man's house exit"
    SNOWMAN_SQUARE_ROPE_FROM_BOTTOM = "Snowman square rope from bottom"
    MILITARY_BASE_ENTRANCE = "Military base entrance"
    MECKS_HOUSE_ENTRANCE = "Meck's house entrance"
    SNOWMAN_SQUARE_DOWN = "Snowman square down"
    SNOWMAN_SQUARE_ROPE_FROM_TOP = "Snowman square rope from top"
    SNOWMAN_SQUARE_LEFT = "Snowman square left"
    SNOWMAN_SQUARE_UP = "Snowman square up"
    MILITARY_BASE_EXIT = "Military base exit"
    MECKS_HOUSE_EXIT = "Meck's house exit"
    WIZARD_TOWER_ENTRANCE = "Wizard tower entrance"
    OUTSIDE_WIZARD_TOWER_RIGHT = "Outside wizard tower right"
    WIZARD_PORTAL_ENTRANCE = "Wizard portal entrance"
    WIZARD_TOWER_EXIT = "Wizard tower exit"
    WIZARD_PORTAL_EXIT = "Wizard portal exit"
    CLIFFS_DOWN = "Cliffs down"
    CLIFFS_BOTTOM_ROPE_FROM_BOTTOM = "Cliffs bottom rope from bottom"
    CLIFFS_RIGHT = "Cliffs right"
    CLIFFS_BOTTOM_ROPE_FROM_MIDDLE = "Cliffs bottom rope from middle"
    CLIFFS_TOP_ROPE_FROM_MIDDLE = "Cliffs top rope from middle"
    CLIFFS_UP = "Cliffs up"
    CLIFFS_TOP_ROPE_FROM_TOP = "Cliffs top rope from top"
    BLIZZARD_BRIDGE_LEFT = "Blizzard bridge left"
    BLIZZARD_BRIDGE_ROPE_FROM_LOWER_LEFT = "Blizzard bridge rope from lower left"
    BLIZZARD_BRIDGE_BREAK_ICE_FROM_BOTTOM = "Blizzard bridge break ice from bottom"
    MAN_CAVE_ENTRANCE = "Man cave entrance"
    BLIZZARD_BRIDGE_ROPE_FROM_UPPER_LEFT = "Blizzard bridge rope from upper left"
    BLIZZARD_BRIDGE_BREAK_ICE_FROM_TOP = "Blizzard bridge break ice from top"
    BLIZZARD_BRIDGE_ROPE_FROM_LOWER_RIGHT = "Blizzard bridge rope from lower right"
    BLIZZARD_BRIDGE_ROPE_FROM_UPPER_RIGHT = "Blizzard bridge rope from upper right"
    BLIZZARD_BRIDGE_RIGHT = "Blizzard bridge right"
    MAN_CAVE_EXIT = "Man cave exit"
    BLIZZARD_MONSTER_EXIT = "Blizzard monster exit"
    OBSERVATORY_ENTRANCE = "Observatory entrance"
    OUTSIDE_OBSERVATORY_ROPE_FROM_TOP = "Outside observatory rope from top"
    OUTSIDE_OBSERVATORY_ROPE_FROM_BOTTOM = "Outside observatory rope from bottom"
    OUTSIDE_OBSERVATORY_DOWN = "Outside observatory down"
    OUTSIDE_OBSERVATORY_RIGHT = "Outside observatory right"
    OBSERVATORY_EXIT = "Observatory exit"
    SKI_LODGE_ENTRANCE = "Ski lodge entrance"
    SKI_LIFT_BASE_LEFT = "Ski lift base left"
    SKI_LIFT_UP = "Ski lift up"
    SKI_LODGE_EXIT = "Ski lodge exit"
    SKI_MOUNTAIN_TOP_LEFT = "Ski mountain top left"
    SKI_LIFT_DOWN = "Ski lift down"

    # Mountain top
    MOUNTAIN_TOP_BUS_STOP_CLIMB = "Mountain top bus stop climb"
    TOEM_DESCEND = "Toem descend"

    # Basto
    BASTO_HARBOR_GATE_FROM_TOP = "Basto harbor gate from top"
    BASTO_HARBOR_UP = "Basto harbor up"
    BASTO_HARBOR_GATE_FROM_BOTTOM = "Basto harbor gate from bottom"
    VIKING_EXPRESS_BASTO_STOP = "Viking express Basto stop"
    LILY_PAD_POND_DOWN = "Lily pad pond down"
    LILY_PAD_POND_LEFT = "Lily pad pond left"
    LILY_PAD_POND_NIGHT_BRIDGE_FROM_LEFT = "Lily pad pond night bridge from left"
    LILY_PAD_POND_RIGHT = "Lily pad pond right"
    LILY_PAD_POND_UP = "Lily pad pond up"
    LILY_PAD_POND_NIGHT_BRIDGE_FROM_RIGHT = "Lily pad pond night bridge from right"
    TENT_ENTRANCE = "Tent entrance"
    CAMPSITE_RIGHT = "Campsite right"
    TENT_EXIT = "Tent exit"
    CASTLE_ENTRANCE = "Castle entrance"
    GYM_HOUSE_ENTRANCE = "Gym house entrance"
    OUTSIDE_CASTLE_DOWN = "Outside castle down"
    OUTSIDE_CASTLE_LEFT = "Outside castle left"
    CASTLE_EXIT = "Castle exit"
    GYM_HOUSE_EXIT = "Gym house exit"
    BONFIRE_LOWER_RIGHT = "Bonfire lower right"
    BONFIRE_UPPER_RIGHT = "Bonfire upper right"
    BONFIRE_DAY_BRIDGE_FROM_TOP = "Bonfire day bridge from top"
    CARNIVAL_ENTRANCE = "Carnival entrance"
    BONFIRE_DAY_BRIDGE_FROM_BOTTOM = "Bonfire day bridge from bottom"
    CARNIVAL_EXIT = "Carnival exit"
    GHOST_HANGOUT_CAVE_ENTRANCE = "Ghost hangout cave entrance"
    GHOST_HANGOUT_LEFT = "Ghost hangout left"
    SECRET_CAVE_ROOM_ENTRANCE = "Secret cave room entrance"
    GHOST_HANGOUT_CAVE_EXIT = "Ghost hangout cave exit"
    JUNGLE_CAVE_EXIT = "Jungle cave exit"
    SECRET_CAVE_ROOM_EXIT = "Secret cave room exit"
    JUNGLE_CAVE_ENTRANCE = "Jungle cave entrance"
    JUNGLE_LEFT = "Jungle left"


region_connections: list[Connection] = [
    # Menu
    Connection(FullRegionName.START_MENU, FullRegionName.HOMELANDA_PLAYER_ROOM, ConnectionName.START_GAME, ERGroups.EXCLUDED),

    # Homelanda
    Connection(FullRegionName.HOMELANDA_PLAYER_ROOM, FullRegionName.HOMELANDA_LIVING_ROOM, ConnectionName.PLAYER_ROOM_EXIT, ERGroups.HOMELANDA),
    Connection(FullRegionName.HOMELANDA_LIVING_ROOM, FullRegionName.HOMELANDA_PLAYER_ROOM, ConnectionName.PLAYER_ROOM_ENTRANCE, ERGroups.HOMELANDA),
    Connection(FullRegionName.HOMELANDA_LIVING_ROOM, FullRegionName.HOMELANDA_BUS_STOP, ConnectionName.HOMELANDA_HOUSE_EXIT, ERGroups.HOMELANDA),
    Connection(FullRegionName.HOMELANDA_BUS_STOP, FullRegionName.HOMELANDA_LIVING_ROOM, ConnectionName.HOMELANDA_HOUSE_ENTRANCE, ERGroups.HOMELANDA),
    Connection(FullRegionName.HOMELANDA_BUS_STOP, FullRegionName.OAKLAVILLE_BUS_STOP, ConnectionName.OAKLAVILLE_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(RegionName.HOMELANDA)),

    # Oaklaville
    Connection(FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.STANHAMN_BUS_STOP, ConnectionName.STANHAMN_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(RegionName.OAKLAVILLE)),
    Connection(FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, ConnectionName.OAKLAVILLE_BUS_STOP_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_BUS_STOP, ConnectionName.OUTSIDE_HOTEL_DOWN, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, ConnectionName.OUTSIDE_HOTEL_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_CAMP, ConnectionName.OUTSIDE_HOTEL_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_HOTEL, ConnectionName.HOTEL_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_HOTEL, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, ConnectionName.HOTEL_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_HOTEL, FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, ConnectionName.HOTEL_ELEVATOR_ENTRANCE, ERGroups.OAKLAVILLE, CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    Connection(FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, FullRegionName.OAKLAVILLE_HOTEL, ConnectionName.HOTEL_ELEVATOR_EXIT, ERGroups.OAKLAVILLE, CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, ConnectionName.GHOST_CUP_GAME_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, ConnectionName.MUSHROOM_HOUSE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, ConnectionName.GHOST_CUP_GAME_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, ConnectionName.MUSHROOM_HOUSE_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, ConnectionName.HIDE_AND_SEEK_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, FullRegionName.OAKLAVILLE_GRAVEYARD, ConnectionName.HIDE_AND_SEEK_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_GRAVEYARD, FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, ConnectionName.GRAVEYARD_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_GRAVEYARD, FullRegionName.OAKLAVILLE_SKELETON_HOUSE, ConnectionName.SKELETON_HOUSE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE, FullRegionName.OAKLAVILLE_GRAVEYARD, ConnectionName.SKELETON_HOUSE_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE, FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, ConnectionName.SKELETON_HOUSE_BALCONY_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, FullRegionName.OAKLAVILLE_SKELETON_HOUSE, ConnectionName.SKELETON_HOUSE_BALCONY_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, ConnectionName.SCOUT_CAMP_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_TRAIL_BOTTOM, ConnectionName.SCOUT_CAMP_UP, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_PLAYGROUND, ConnectionName.SCOUT_CAMP_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_TRAIL_TOP, FullRegionName.OAKLAVILLE_TRAIL_BOTTOM, ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_TOP, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_LOG_JAM)),
    Connection(FullRegionName.OAKLAVILLE_TRAIL_TOP, FullRegionName.OAKLAVILLE_LOOKOUT, ConnectionName.OAKLAVILLE_TRAIL_UP, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_TRAIL_BOTTOM, FullRegionName.OAKLAVILLE_TRAIL_TOP, ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_BOTTOM, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_LOG_JAM)),
    Connection(FullRegionName.OAKLAVILLE_TRAIL_BOTTOM, FullRegionName.OAKLAVILLE_CAMP, ConnectionName.OAKLAVILLE_TRAIL_DOWN, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_LOOKOUT, FullRegionName.OAKLAVILLE_TRAIL_TOP, ConnectionName.LOOKOUT_EXIT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_PLAYGROUND, FullRegionName.OAKLAVILLE_CAMP, ConnectionName.PLAYGROUND_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_PLAYGROUND, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, ConnectionName.PLAYGROUND_RIGHT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, ConnectionName.RAVE_BOUNCER_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.GHOST_GLASSES) & CanReachRegion(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM)),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, FullRegionName.OAKLAVILLE_RAVE, ConnectionName.RAVE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, ConnectionName.RAVE_BOUNCER_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.GHOST_GLASSES)),
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, FullRegionName.OAKLAVILLE_PLAYGROUND, ConnectionName.OUTSIDE_RAVE_LEFT, ERGroups.OAKLAVILLE),
    Connection(FullRegionName.OAKLAVILLE_RAVE, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, ConnectionName.RAVE_EXIT, ERGroups.OAKLAVILLE),

    # Stanhamn
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.LOGCITY_BUS_STOP, ConnectionName.LOGCITY_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(RegionName.STANHAMN)),
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_PHOTO_GUILD_HUT, ConnectionName.PHOTO_GUILD_HUT_ENTRANCE, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, ConnectionName.STANHAMN_BUS_STOP_LEFT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_DOCKS_LEFT, ConnectionName.STANHAMN_BUS_STOP_RIGHT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, ConnectionName.RAFT_UP, ERGroups.STANHAMN, Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_PHOTO_GUILD_HUT, FullRegionName.STANHAMN_BUS_STOP, ConnectionName.PHOTO_GUILD_HUT_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, FullRegionName.STANHAMN_BUS_STOP, ConnectionName.PIRATE_DRAWBRIDGE_RIGHT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, FullRegionName.STANHAMN_HIPPO_BEACH, ConnectionName.PIRATE_DRAWBRIDGE_LEFT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, ConnectionName.HIPPO_BEACH_RIGHT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_UNDERWATER, ConnectionName.HIPPO_BEACH_MANHOLE, ERGroups.STANHAMN, HasAll(ItemName.HONK_ATTACHMENT, ItemName.DIVING_HELMET)),
    Connection(FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ConnectionName.HIPPO_BEACH_LEFT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_UNDERWATER, FullRegionName.STANHAMN_HIPPO_BEACH, ConnectionName.UNDERWATER_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, FullRegionName.STANHAMN_HIPPO_BEACH, ConnectionName.OUTSIDE_LIGHTHOUSE_RIGHT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, FullRegionName.STANHAMN_KING_FISH_BEACH, ConnectionName.OUTSIDE_LIGHTHOUSE_UP, ERGroups.STANHAMN, Has(ItemName.HONK_ATTACHMENT)),
    Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, FullRegionName.STANHAMN_LIGHTHOUSE, ConnectionName.LIGHTHOUSE_ENTRANCE, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_LIGHTHOUSE, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ConnectionName.LIGHTHOUSE_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_LIGHTHOUSE, FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, ConnectionName.LIGHTHOUSE_ROOF_ENTRANCE, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, FullRegionName.STANHAMN_LIGHTHOUSE, ConnectionName.LIGHTHOUSE_ROOF_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_KING_FISH_BEACH, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ConnectionName.KING_FISH_BEACH_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.STANHAMN_BUS_STOP, ConnectionName.DOCKS_LEFT_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.BASTO_BUS_STOP_BOTTOM, ConnectionName.VIKING_EXPRESS_STAMHAMN_STOP, ERGroups.EXCLUDED, Has(ItemName.BASTO_TICKET)),
    Connection(FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.STANHAMN_DOCKS_RIGHT, ConnectionName.DOCKS_DRAWBRIDGE_FROM_LEFT, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.STANHAMN_FISHING_TOWER, ConnectionName.DOCKS_RIGHT_EXIT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.STANHAMN_DOCKS_LEFT, ConnectionName.DOCKS_DRAWBRIDGE_FROM_RIGHT, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_FISHING_TOWER, FullRegionName.STANHAMN_DOCKS_RIGHT, ConnectionName.FISHING_TOWER_LEFT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_FISHING_TOWER, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, ConnectionName.FISHING_TOWER_UP, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, ConnectionName.GHOST_DRAWBRIDGE_LEFT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, ConnectionName.GHOST_DRAWBRIDGE_FROM_TOP, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, FullRegionName.STANHAMN_FISHING_TOWER, ConnectionName.GHOST_DRAWBRIDGE_DOWN, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, ConnectionName.GHOST_DRAWBRIDGE_FROM_BOTTOM, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, FullRegionName.STANHAMN_BUS_STOP, ConnectionName.RAFT_DOWN, ERGroups.STANHAMN, Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, FullRegionName.STANHAMN_HYDROPLANT, ConnectionName.HYDROPLANT_ENTRANCE, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, ConnectionName.OUTSIDE_HYDROPLANT_RIGHT, ERGroups.STANHAMN),
    Connection(FullRegionName.STANHAMN_HYDROPLANT, FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, ConnectionName.HYDROPLANT_EXIT, ERGroups.STANHAMN),

    # Logcity
    Connection(FullRegionName.LOGCITY_BUS_STOP, FullRegionName.KIIRUBERG_BUS_STOP, ConnectionName.KIIRUBERG_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(RegionName.LOGCITY)),
    Connection(FullRegionName.LOGCITY_BUS_STOP, FullRegionName.LOGCITY_CLOCK_TOWER, ConnectionName.ESCALATOR_UP, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_BUS_STOP, ConnectionName.LOGCITY_BUS_STOP_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_CROSSWALK, ConnectionName.CLOCK_TOWER_LEFT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ConnectionName.CLOCK_TOWER_UP, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_OUTSIDE_CAFE, ConnectionName.CLOCK_TOWER_RIGHT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CROSSWALK, FullRegionName.LOGCITY_CLOCK_TOWER, ConnectionName.CROSS_WALK_RIGHT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CROSSWALK, FullRegionName.LOGCITY_OVERPASS, ConnectionName.CROSS_WALK_UP, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OVERPASS, FullRegionName.LOGCITY_CROSSWALK, ConnectionName.OVERPASS_DOWN, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OVERPASS, FullRegionName.LOGCITY_NEWS_HOUSE, ConnectionName.NEWS_HOUSE_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OVERPASS, FullRegionName.LOGCITY_SKATE_PARK, ConnectionName.OVERPASS_UP, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OVERPASS, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ConnectionName.OVERPASS_RIGHT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_NEWS_HOUSE, FullRegionName.LOGCITY_OVERPASS, ConnectionName.NEWS_HOUSE_EXIT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_OVERPASS, ConnectionName.SKATE_PARK_DOWN, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_RATSKULLZ_ALLEY, ConnectionName.SKATE_PARK_RIGHT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_OUTSIDE_CAFE, ConnectionName.SKATE_PARK_TAXI, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_RATSKULLZ_ALLEY, FullRegionName.LOGCITY_SKATE_PARK, ConnectionName.RATSKULLZ_ALLEY_EXIT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM, ConnectionName.FASHION_SHOW_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_CLOCK_TOWER, ConnectionName.OUTSIDE_FASHION_SHOW_DOWN, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_OVERPASS, ConnectionName.OUTSIDE_FASHION_SHOW_LEFT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_OUTSIDE_GALLERY, ConnectionName.OUTSIDE_FASHION_SHOW_RIGHT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_FASHION_SHOW_TOP, FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM, ConnectionName.FASHION_SHOW_SECURITY_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.REPORTER_HAT) & CanReachRegion(FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM)),
    Connection(FullRegionName.LOGCITY_FASHION_SHOW_TOP, FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, ConnectionName.FASHION_SHOW_BACKSTAGE_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM, FullRegionName.LOGCITY_FASHION_SHOW_TOP, ConnectionName.FASHION_SHOW_SECURITY_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.REPORTER_HAT)),
    Connection(FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ConnectionName.FASHION_SHOW_EXIT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, FullRegionName.LOGCITY_FASHION_SHOW_TOP, ConnectionName.FASHION_SHOW_BACKSTAGE_EXIT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_CAFE, ConnectionName.CAFE_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_CLOCK_TOWER, ConnectionName.OUTSIDE_CAFE_LEFT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_OUTSIDE_GALLERY, ConnectionName.OUTSIDE_CAFE_UP, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_SKATE_PARK, ConnectionName.OUTSIDE_CAFE_TAXI, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_CAFE, FullRegionName.LOGCITY_OUTSIDE_CAFE, ConnectionName.CAFE_EXIT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_GALLERY, ConnectionName.GALLERY_ENTRANCE, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_OUTSIDE_CAFE, ConnectionName.OUTSIDE_GALLERY_SHOW_DOWN, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ConnectionName.OUTSIDE_GALLERY_SHOW_LEFT, ERGroups.LOGCITY),
    Connection(FullRegionName.LOGCITY_GALLERY, FullRegionName.LOGCITY_OUTSIDE_GALLERY, ConnectionName.GALLERY_EXIT, ERGroups.LOGCITY),

    # Kiiruberg
    Connection(FullRegionName.KIIRUBERG_BUS_STOP, FullRegionName.MOUNTAIN_TOP_BUS_STOP, ConnectionName.MOUNTAIN_TOP_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(RegionName.KIIRUBERG)),
    Connection(FullRegionName.KIIRUBERG_BUS_STOP, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ConnectionName.KIIRUBERG_BUS_STOP_UP, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BALLOON_HOUSE, ConnectionName.BALLOON_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BUS_STOP, ConnectionName.BIRTHDAY_PARTY_DOWN, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_FROZEN_POND, ConnectionName.BIRTHDAY_PARTY_LEFT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_SKI_LIFT_BASE, ConnectionName.BIRTHDAY_PARTY_RIGHT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ConnectionName.BIRTHDAY_PARTY_UP, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BALLOON_HOUSE, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ConnectionName.BALLOON_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, ConnectionName.OLD_MANS_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ConnectionName.FROZEN_POND_RIGHT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, FullRegionName.KIIRUBERG_FROZEN_POND, ConnectionName.OLD_MANS_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.KIIRUBERG_MILITARY_BASE, ConnectionName.MILITARY_BASE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.KIIRUBERG_MECKS_HOUSE, ConnectionName.MECKS_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, ConnectionName.SNOWMAN_SQUARE_DOWN, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, ConnectionName.SNOWMAN_SQUARE_LEFT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, ConnectionName.SNOWMAN_SQUARE_UP, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_MILITARY_BASE, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ConnectionName.MILITARY_BASE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_MECKS_HOUSE, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ConnectionName.MECKS_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, FullRegionName.KIIRUBERG_WIZARD_TOWER, ConnectionName.WIZARD_TOWER_ENTRANCE, ERGroups.KIIRUBERG, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ConnectionName.OUTSIDE_WIZARD_TOWER_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, FullRegionName.KIIRUBERG_COSMO_GARDEN, ConnectionName.WIZARD_PORTAL_ENTRANCE, ERGroups.KIIRUBERG, CanReachLocation(LocationName.QUEST_ICE_WIZARD)),
    Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, ConnectionName.WIZARD_TOWER_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_COSMO_GARDEN, FullRegionName.KIIRUBERG_WIZARD_TOWER, ConnectionName.WIZARD_PORTAL_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ConnectionName.CLIFFS_DOWN, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, ConnectionName.CLIFFS_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.HONK_ATTACHMENT)),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_MIDDLE, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, FullRegionName.KIIRUBERG_CLIFFS_TOP, ConnectionName.CLIFFS_TOP_ROPE_FROM_MIDDLE, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, ConnectionName.CLIFFS_UP, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, ConnectionName.CLIFFS_TOP_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, ConnectionName.BLIZZARD_BRIDGE_LEFT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_LEFT, ERGroups.EXCLUDED, HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_BOTTOM, ERGroups.EXCLUDED, HasAll(ItemName.HONK_ATTACHMENT, ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, FullRegionName.KIIRUBERG_MAN_CAVE, ConnectionName.MAN_CAVE_ENTRANCE, ERGroups.KIIRUBERG, CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_LEFT, ERGroups.EXCLUDED, HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.HONK_ATTACHMENT)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_RIGHT, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_RIGHT, ERGroups.EXCLUDED, HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.KIIRUBERG_BLIZZARD_MONSTER, ConnectionName.BLIZZARD_BRIDGE_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.HONK_ATTACHMENT)),
    Connection(FullRegionName.KIIRUBERG_MAN_CAVE, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, ConnectionName.MAN_CAVE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_BLIZZARD_MONSTER, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ConnectionName.BLIZZARD_MONSTER_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, FullRegionName.KIIRUBERG_OBSERVATORY, ConnectionName.OBSERVATORY_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, FullRegionName.KIIRUBERG_CLIFFS_TOP, ConnectionName.OUTSIDE_OBSERVATORY_DOWN, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, ConnectionName.OUTSIDE_OBSERVATORY_RIGHT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_OBSERVATORY, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, ConnectionName.OBSERVATORY_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, FullRegionName.KIIRUBERG_SKI_LODGE, ConnectionName.SKI_LODGE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ConnectionName.SKI_LIFT_BASE_LEFT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, ConnectionName.SKI_LIFT_UP, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_LODGE, FullRegionName.KIIRUBERG_SKI_LIFT_BASE, ConnectionName.SKI_LODGE_EXIT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, ConnectionName.SKI_MOUNTAIN_TOP_LEFT, ERGroups.KIIRUBERG),
    Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, FullRegionName.KIIRUBERG_SKI_LIFT_BASE, ConnectionName.SKI_LIFT_DOWN, ERGroups.KIIRUBERG),

    # Mountain top
    Connection(FullRegionName.MOUNTAIN_TOP_BUS_STOP, FullRegionName.MOUNTAIN_TOP_TOEM, ConnectionName.MOUNTAIN_TOP_BUS_STOP_CLIMB, ERGroups.MOUNTAIN_TOP),
    Connection(FullRegionName.MOUNTAIN_TOP_TOEM, FullRegionName.MOUNTAIN_TOP_BUS_STOP, ConnectionName.TOEM_DESCEND, ERGroups.MOUNTAIN_TOP),

    # Basto
    Connection(FullRegionName.BASTO_BUS_STOP_TOP, FullRegionName.BASTO_BUS_STOP_BOTTOM, ConnectionName.BASTO_HARBOR_GATE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.WATERGUN)),
    Connection(FullRegionName.BASTO_BUS_STOP_TOP, FullRegionName.BASTO_LILY_PAD_POND_LEFT, ConnectionName.BASTO_HARBOR_UP, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM, FullRegionName.BASTO_BUS_STOP_TOP, ConnectionName.BASTO_HARBOR_GATE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.WATERGUN)),
    Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM, FullRegionName.STANHAMN_DOCKS_LEFT, ConnectionName.VIKING_EXPRESS_BASTO_STOP, ERGroups.EXCLUDED, Has(ItemName.BASTO_TICKET)),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.BASTO_BUS_STOP_TOP, ConnectionName.LILY_PAD_POND_DOWN, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.BASTO_CAMP, ConnectionName.LILY_PAD_POND_LEFT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.BASTO_LILY_PAD_POND_RIGHT, ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_LEFT, ERGroups.EXCLUDED, Has(EventName.BASTO_LILY_PAD_POND_LEFT_NIGHT)),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_GHOST_HANGOUT, ConnectionName.LILY_PAD_POND_RIGHT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_OUTSIDE_CASTLE, ConnectionName.LILY_PAD_POND_UP, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_LILY_PAD_POND_LEFT, ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_RIGHT, ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_CAMP, FullRegionName.BASTO_TENT, ConnectionName.TENT_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_CAMP, FullRegionName.BASTO_LILY_PAD_POND_LEFT, ConnectionName.CAMPSITE_RIGHT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_TENT, FullRegionName.BASTO_CAMP, ConnectionName.TENT_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_CASTLE, ConnectionName.CASTLE_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_GYM_HOUSE, ConnectionName.GYM_HOUSE_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_LILY_PAD_POND_RIGHT, ConnectionName.OUTSIDE_CASTLE_DOWN, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_BONFIRE_TOP, ConnectionName.OUTSIDE_CASTLE_LEFT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_CASTLE, FullRegionName.BASTO_OUTSIDE_CASTLE, ConnectionName.CASTLE_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_GYM_HOUSE, FullRegionName.BASTO_OUTSIDE_CASTLE, ConnectionName.GYM_HOUSE_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_OUTSIDE_CASTLE, ConnectionName.BONFIRE_LOWER_RIGHT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_JUNGLE, ConnectionName.BONFIRE_UPPER_RIGHT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_BONFIRE_BOTTOM, ConnectionName.BONFIRE_DAY_BRIDGE_FROM_TOP, ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BONFIRE_BOTTOM, FullRegionName.BASTO_CARNIVAL, ConnectionName.CARNIVAL_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_BONFIRE_BOTTOM, FullRegionName.BASTO_BONFIRE_TOP, ConnectionName.BONFIRE_DAY_BRIDGE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(EventName.BASTO_BONFIRE_BOTTOM_DAY)),
    Connection(FullRegionName.BASTO_CARNIVAL, FullRegionName.BASTO_BONFIRE_BOTTOM, ConnectionName.CARNIVAL_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_CAVE, ConnectionName.GHOST_HANGOUT_CAVE_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_LILY_PAD_POND_RIGHT, ConnectionName.GHOST_HANGOUT_LEFT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_CAVE, FullRegionName.BASTO_SECRET_CAVE, ConnectionName.SECRET_CAVE_ROOM_ENTRANCE, ERGroups.BASTO, HasAll(ItemName.PICKAXE, ItemName.WATERGUN)),
    Connection(FullRegionName.BASTO_CAVE, FullRegionName.BASTO_GHOST_HANGOUT, ConnectionName.GHOST_HANGOUT_CAVE_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_CAVE, FullRegionName.BASTO_JUNGLE, ConnectionName.JUNGLE_CAVE_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_SECRET_CAVE, FullRegionName.BASTO_CAVE, ConnectionName.SECRET_CAVE_ROOM_EXIT, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_JUNGLE, FullRegionName.BASTO_CAVE, ConnectionName.JUNGLE_CAVE_ENTRANCE, ERGroups.BASTO),
    Connection(FullRegionName.BASTO_JUNGLE, FullRegionName.BASTO_BONFIRE_TOP, ConnectionName.JUNGLE_LEFT, ERGroups.BASTO),

    # Helper connections
    # Super region connections
    *[Connection(region, FullRegionName.OAKLAVILLE, f"{region} in {RegionName.OAKLAVILLE}", ERGroups.EXCLUDED) for region in oaklaville_regions],
    *[Connection(region, FullRegionName.STANHAMN, f"{region} in {RegionName.STANHAMN}", ERGroups.EXCLUDED) for region in stanhamn_regions],
    *[Connection(region, FullRegionName.LOGCITY, f"{region} in {RegionName.LOGCITY}", ERGroups.EXCLUDED) for region in logcity_regions],
    *[Connection(region, FullRegionName.KIIRUBERG, f"{region} in {RegionName.KIIRUBERG}", ERGroups.EXCLUDED) for region in kiiruberg_regions],
    *[Connection(region, FullRegionName.MOUNTAIN_TOP, f"{region} in {RegionName.MOUNTAIN_TOP}", ERGroups.EXCLUDED) for region in mountain_top_regions],
    *[Connection(region, FullRegionName.BASTO, f"{region} in {RegionName.BASTO}", ERGroups.EXCLUDED) for region in basto_regions],
    # Compendium connections
    Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.SQUIRRELS, "Squirrel from Ghost cup game", ERGroups.EXCLUDED),
    Connection(FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, FullRegionName.SQUIRRELS, "Squirrels from Hotel elevator", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_BUS_STOP, FullRegionName.SEAGULLS, "Seagulls from Stanhamn bus stop", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.SEAGULLS, "Seagulls from Hippo beach", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, FullRegionName.SEAGULLS, "Seagulls from Outside lighthouse", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.SUNDAY_SWAN, "Sunday swan from Docks left", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.SUNDAY_SWAN, "Sunday swan from Docks right", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.PIGEON, "Pigeon from Clock tower", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.PIGEON, "Pigeon from Outside cafe", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.PIGEON, "Pigeon from Outside gallery", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_RATSKULLZ_ALLEY, FullRegionName.PIGEON, "Pigeon from Ratskullz alley", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.GOAT, "Goat from Birthday party bottom", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, FullRegionName.GOAT, "Goat from Birthday party top", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, FullRegionName.GOAT, "Goat from Ski mountain top", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.GOAT, "Goat from Cliffs top", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, FullRegionName.GOAT, "Goat from Cliffs middle", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_CAVE, FullRegionName.BAT, "Bat from Cave", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BAT, "Bat from Bonfire top", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BAT, "Bat from Outside castle", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM, FullRegionName.BEAK_BIRD, "Beak bird from Harbor bottom", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BUS_STOP_TOP, FullRegionName.BEAK_BIRD, "Beak bird from Harbor top", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.BEAK_BIRD, "Beak bird from Lily pad pond left", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BEAK_BIRD, "Beak bird from Lily pad pond right", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM, FullRegionName.BITLING_TATO, "Bitling tato from Harbor bottom", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BUS_STOP_TOP, FullRegionName.BITLING_TATO, "Bitling tato from Harbor top", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.WATER_STRIDER, "Water strider from Lily pad pond left", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.WATER_STRIDER, "Water strider from Outside castle", ERGroups.EXCLUDED),
    # Achievement connections
    Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.GOOD_BOY, "Pet Tom", ERGroups.EXCLUDED),
    Connection(FullRegionName.OAKLAVILLE_HOTEL, FullRegionName.GOOD_BOY, "Pet Oskar", ERGroups.EXCLUDED),
    Connection(FullRegionName.OAKLAVILLE_GRAVEYARD, FullRegionName.GOOD_BOY, "Pet Sero", ERGroups.EXCLUDED),
    Connection(FullRegionName.OAKLAVILLE_CAMP, FullRegionName.GOOD_BOY, "Pet the Pet rock", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.GOOD_BOY, "Pet Fia", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.GOOD_BOY, "Pet Fräs", ERGroups.EXCLUDED),
    Connection(FullRegionName.STANHAMN_KING_FISH_BEACH, FullRegionName.GOOD_BOY, "Pet Willemijn", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.GOOD_BOY, "Pet Portillo", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_BALLOON_HOUSE, FullRegionName.GOOD_BOY, "Pet Mikée or Nariko", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_MECKS_HOUSE, FullRegionName.GOOD_BOY, "Pet Teddy", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT, FullRegionName.MAXIMUM_VACATION, "Sit on a chair in Lily pad pond left", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_GYM_HOUSE, FullRegionName.MAXIMUM_VACATION, "Sit on a chair in Gym house", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_CARNIVAL, FullRegionName.MAXIMUM_VACATION, "Sit on a chair in Carnival", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.MAXIMUM_VACATION, "Sit on a chair in Bonfire top", ERGroups.EXCLUDED),
    Connection(FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.MAXIMUM_VACATION, "Sit on a chair in Ghost hangout", ERGroups.EXCLUDED),
    # Cassette connections
    Connection(FullRegionName.LOGCITY_BUS_STOP, FullRegionName.BIG_CITY_TAPE, "Visit Logicity bus stop", ERGroups.EXCLUDED),
    Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.BIG_CITY_TAPE, "Visit Outside fasion show", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.STORIES_OF_SNOW_TAPE, "Visit Birthday party bottom", ERGroups.EXCLUDED),
    Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, FullRegionName.STORIES_OF_SNOW_TAPE, "Visit Birthday party top", ERGroups.EXCLUDED),
]

connection_name_to_id: dict[str, int] = {connection.name: i for i, connection in enumerate(region_connections, start=1)}


required_regions_always = {
    ConnectionName.OAKLAVILLE_TRAIL_DOWN: (FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_BUS_STOP,
                                           FullRegionName.OAKLAVILLE_HOTEL),
    ConnectionName.HOTEL_EXIT: (FullRegionName.OAKLAVILLE_LOOKOUT,),
    ConnectionName.DOCKS_LEFT_EXIT: (FullRegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.DOCKS_RIGHT_EXIT: (FullRegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.GHOST_DRAWBRIDGE_LEFT: (FullRegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.GHOST_DRAWBRIDGE_DOWN: (FullRegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.WIZARD_TOWER_EXIT: (FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,),
}
required_regions_no_items = required_regions_always | {
    ConnectionName.OUTSIDE_RAVE_LEFT: (FullRegionName.OAKLAVILLE_GRAVEYARD,),
    ConnectionName.FASHION_SHOW_EXIT: (FullRegionName.LOGCITY_NEWS_HOUSE,),
    ConnectionName.BIRTHDAY_PARTY_UP: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.WIZARD_TOWER_ENTRANCE: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.OUTSIDE_WIZARD_TOWER_RIGHT: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_DOWN: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_RIGHT: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_UP: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.OBSERVATORY_ENTRANCE: (FullRegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.WIZARD_TOWER_EXIT: (FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_SKI_LODGE,
                            FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.BLIZZARD_BRIDGE_LEFT: (FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_SKI_LODGE,
                                          FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.BLIZZARD_BRIDGE_RIGHT: (FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_SKI_LODGE,
                                           FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.MAN_CAVE_ENTRANCE: (FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_SKI_LODGE,
                                       FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
}

class ToemEntrance(Entrance):
    def can_connect_to(self, other: Entrance, dead_end: bool, er_state: "ERPlacementState") -> bool:
        living_room_entrances = {ConnectionName.PLAYER_ROOM_EXIT, ConnectionName.HOMELANDA_HOUSE_ENTRANCE}
        if self.name in living_room_entrances and other.name in living_room_entrances:
            return False
        if not dead_end:
            if other.name in {ConnectionName.OAKLAVILLE_TRAIL_UP, ConnectionName.RAVE_ENTRANCE,
                              ConnectionName.FASHION_SHOW_BACKSTAGE_ENTRANCE}:
                return False
            required_regions = required_regions_always if er_state.world.options.include_items \
                               else required_regions_no_items
            if other.name in required_regions:
                if not all(er_state.world.get_region(region) in er_state.placed_regions
                           for region in required_regions[other.name]):
                    return False
            expanding_dead_ends = {
                ConnectionName.HYDROPLANT_EXIT: RegionName.STANHAMN,
                ConnectionName.LOOKOUT_EXIT: RegionName.OAKLAVILLE,
            }
            if not er_state.world.options.include_items:
                expanding_dead_ends |= {
                    ConnectionName.LIGHTHOUSE_ROOF_EXIT: RegionName.STANHAMN,
                    ConnectionName.NEWS_HOUSE_EXIT: RegionName.LOGCITY,
                    ConnectionName.SKI_LODGE_EXIT: RegionName.KIIRUBERG,
                }
            if other.name in expanding_dead_ends:
                region_exits = [ex for region in er_state.world.multiworld.get_regions(er_state.world.player)
                                if region.name.startswith(expanding_dead_ends[other.name])
                                for ex in region.exits
                                if not ex.connected_region]
                if len(er_state.find_placeable_exits(True, region_exits)) <= 1:
                    return False

        # Run the regular Entrance class's method and return its result like normal.
        return super().can_connect_to(other, dead_end, er_state)

class ToemRegion(Region):
    entrance_type: ClassVar[type[ToemEntrance]] = ToemEntrance

from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar, final

from BaseClasses import Entrance, Region
from entrance_rando import ERPlacementState
from rule_builder.rules import CanReachLocation, CanReachRegion, Has, HasAll, Rule

from .items import ItemName
from .locations import EventName, LocationName, get_stamp_rule
from .regions import (
    Area,
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
    Connection(RegionName.START_MENU, RegionName.HOMELANDA_PLAYER_ROOM,
               ConnectionName.START_GAME, ERGroups.EXCLUDED),

    # Homelanda
    Connection(RegionName.HOMELANDA_PLAYER_ROOM, RegionName.HOMELANDA_LIVING_ROOM,
               ConnectionName.PLAYER_ROOM_EXIT, ERGroups.HOMELANDA),
    Connection(RegionName.HOMELANDA_LIVING_ROOM, RegionName.HOMELANDA_PLAYER_ROOM,
               ConnectionName.PLAYER_ROOM_ENTRANCE, ERGroups.HOMELANDA),
    Connection(RegionName.HOMELANDA_LIVING_ROOM, RegionName.HOMELANDA_BUS_STOP,
               ConnectionName.HOMELANDA_HOUSE_EXIT, ERGroups.HOMELANDA),
    Connection(RegionName.HOMELANDA_BUS_STOP, RegionName.HOMELANDA_LIVING_ROOM,
               ConnectionName.HOMELANDA_HOUSE_ENTRANCE, ERGroups.HOMELANDA),
    Connection(RegionName.HOMELANDA_BUS_STOP, RegionName.OAKLAVILLE_BUS_STOP,
               ConnectionName.OAKLAVILLE_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(Area.HOMELANDA)),

    # Oaklaville
    Connection(RegionName.OAKLAVILLE_BUS_STOP, RegionName.STANHAMN_BUS_STOP,
               ConnectionName.STANHAMN_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(Area.OAKLAVILLE)),
    Connection(RegionName.OAKLAVILLE_BUS_STOP, RegionName.OAKLAVILLE_OUTSIDE_HOTEL,
               ConnectionName.OAKLAVILLE_BUS_STOP_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_BUS_STOP,
               ConnectionName.OUTSIDE_HOTEL_DOWN, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_GHOST_CUP_GAME,
               ConnectionName.OUTSIDE_HOTEL_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_CAMP,
               ConnectionName.OUTSIDE_HOTEL_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_HOTEL,
               ConnectionName.HOTEL_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_HOTEL, RegionName.OAKLAVILLE_OUTSIDE_HOTEL,
               ConnectionName.HOTEL_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_HOTEL, RegionName.OAKLAVILLE_HOTEL_ELEVATOR,
               ConnectionName.HOTEL_ELEVATOR_ENTRANCE, ERGroups.OAKLAVILLE,
               CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    Connection(RegionName.OAKLAVILLE_HOTEL_ELEVATOR, RegionName.OAKLAVILLE_HOTEL,
               ConnectionName.HOTEL_ELEVATOR_EXIT, ERGroups.OAKLAVILLE,
               CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    Connection(RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_OUTSIDE_HOTEL,
               ConnectionName.GHOST_CUP_GAME_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_MUSHROOM_HOUSE,
               ConnectionName.MUSHROOM_HOUSE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_HIDE_AND_SEEK,
               ConnectionName.GHOST_CUP_GAME_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_MUSHROOM_HOUSE, RegionName.OAKLAVILLE_GHOST_CUP_GAME,
               ConnectionName.MUSHROOM_HOUSE_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_HIDE_AND_SEEK, RegionName.OAKLAVILLE_GHOST_CUP_GAME,
               ConnectionName.HIDE_AND_SEEK_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_HIDE_AND_SEEK, RegionName.OAKLAVILLE_GRAVEYARD,
               ConnectionName.HIDE_AND_SEEK_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_GRAVEYARD, RegionName.OAKLAVILLE_HIDE_AND_SEEK,
               ConnectionName.GRAVEYARD_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_GRAVEYARD, RegionName.OAKLAVILLE_SKELETON_HOUSE,
               ConnectionName.SKELETON_HOUSE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_SKELETON_HOUSE, RegionName.OAKLAVILLE_GRAVEYARD,
               ConnectionName.SKELETON_HOUSE_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_SKELETON_HOUSE, RegionName.OAKLAVILLE_SKELETON_BALCONY,
               ConnectionName.SKELETON_HOUSE_BALCONY_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_SKELETON_BALCONY, RegionName.OAKLAVILLE_SKELETON_HOUSE,
               ConnectionName.SKELETON_HOUSE_BALCONY_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_OUTSIDE_HOTEL,
               ConnectionName.SCOUT_CAMP_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_TRAIL_BOTTOM,
               ConnectionName.SCOUT_CAMP_UP, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_PLAYGROUND,
               ConnectionName.SCOUT_CAMP_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_TRAIL_TOP, RegionName.OAKLAVILLE_TRAIL_BOTTOM,
               ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_TOP, ERGroups.EXCLUDED,
               CanReachLocation(LocationName.QUEST_LOG_JAM)),
    Connection(RegionName.OAKLAVILLE_TRAIL_TOP, RegionName.OAKLAVILLE_LOOKOUT,
               ConnectionName.OAKLAVILLE_TRAIL_UP, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_TRAIL_BOTTOM, RegionName.OAKLAVILLE_TRAIL_TOP,
               ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_BOTTOM, ERGroups.EXCLUDED,
               CanReachLocation(LocationName.QUEST_LOG_JAM)),
    Connection(RegionName.OAKLAVILLE_TRAIL_BOTTOM, RegionName.OAKLAVILLE_CAMP,
               ConnectionName.OAKLAVILLE_TRAIL_DOWN, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_LOOKOUT, RegionName.OAKLAVILLE_TRAIL_TOP,
               ConnectionName.LOOKOUT_EXIT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_PLAYGROUND, RegionName.OAKLAVILLE_CAMP,
               ConnectionName.PLAYGROUND_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_PLAYGROUND, RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM,
               ConnectionName.PLAYGROUND_RIGHT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM,
               ConnectionName.RAVE_BOUNCER_FROM_TOP, ERGroups.EXCLUDED,
               Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM)),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, RegionName.OAKLAVILLE_RAVE,
               ConnectionName.RAVE_ENTRANCE, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP,
               ConnectionName.RAVE_BOUNCER_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.GHOST_GLASSES)),
    Connection(RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, RegionName.OAKLAVILLE_PLAYGROUND,
               ConnectionName.OUTSIDE_RAVE_LEFT, ERGroups.OAKLAVILLE),
    Connection(RegionName.OAKLAVILLE_RAVE, RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP,
               ConnectionName.RAVE_EXIT, ERGroups.OAKLAVILLE),

    # Stanhamn
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.LOGCITY_BUS_STOP,
               ConnectionName.LOGCITY_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(Area.STANHAMN)),
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_PHOTO_GUILD_HUT,
               ConnectionName.PHOTO_GUILD_HUT_ENTRANCE, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_PIRATE_DRAWBRIDGE,
               ConnectionName.STANHAMN_BUS_STOP_LEFT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_DOCKS_LEFT,
               ConnectionName.STANHAMN_BUS_STOP_RIGHT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_OUTSIDE_HYDROPLANT,
               ConnectionName.RAFT_UP, ERGroups.STANHAMN,
               Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_PHOTO_GUILD_HUT, RegionName.STANHAMN_BUS_STOP,
               ConnectionName.PHOTO_GUILD_HUT_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, RegionName.STANHAMN_BUS_STOP,
               ConnectionName.PIRATE_DRAWBRIDGE_RIGHT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, RegionName.STANHAMN_HIPPO_BEACH,
               ConnectionName.PIRATE_DRAWBRIDGE_LEFT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_PIRATE_DRAWBRIDGE,
               ConnectionName.HIPPO_BEACH_RIGHT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_UNDERWATER,
               ConnectionName.HIPPO_BEACH_MANHOLE, ERGroups.STANHAMN,
               HasAll(ItemName.HONK_ATTACHMENT, ItemName.DIVING_HELMET)),
    Connection(RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE,
               ConnectionName.HIPPO_BEACH_LEFT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_UNDERWATER, RegionName.STANHAMN_HIPPO_BEACH,
               ConnectionName.UNDERWATER_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_HIPPO_BEACH,
               ConnectionName.OUTSIDE_LIGHTHOUSE_RIGHT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_KING_FISH_BEACH,
               ConnectionName.OUTSIDE_LIGHTHOUSE_UP, ERGroups.STANHAMN, Has(ItemName.HONK_ATTACHMENT)),
    Connection(RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE,
               ConnectionName.LIGHTHOUSE_ENTRANCE, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_LIGHTHOUSE, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE,
               ConnectionName.LIGHTHOUSE_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE_ROOF,
               ConnectionName.LIGHTHOUSE_ROOF_ENTRANCE, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_LIGHTHOUSE_ROOF, RegionName.STANHAMN_LIGHTHOUSE,
               ConnectionName.LIGHTHOUSE_ROOF_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_KING_FISH_BEACH, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE,
               ConnectionName.KING_FISH_BEACH_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_DOCKS_LEFT, RegionName.STANHAMN_BUS_STOP,
               ConnectionName.DOCKS_LEFT_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_DOCKS_LEFT, RegionName.BASTO_BUS_STOP_BOTTOM,
               ConnectionName.VIKING_EXPRESS_STAMHAMN_STOP, ERGroups.EXCLUDED, Has(ItemName.BASTO_TICKET)),
    Connection(RegionName.STANHAMN_DOCKS_LEFT, RegionName.STANHAMN_DOCKS_RIGHT,
               ConnectionName.DOCKS_DRAWBRIDGE_FROM_LEFT, ERGroups.EXCLUDED,
               CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_DOCKS_RIGHT, RegionName.STANHAMN_FISHING_TOWER,
               ConnectionName.DOCKS_RIGHT_EXIT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_DOCKS_RIGHT, RegionName.STANHAMN_DOCKS_LEFT,
               ConnectionName.DOCKS_DRAWBRIDGE_FROM_RIGHT, ERGroups.EXCLUDED,
               CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_FISHING_TOWER, RegionName.STANHAMN_DOCKS_RIGHT,
               ConnectionName.FISHING_TOWER_LEFT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_FISHING_TOWER, RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM,
               ConnectionName.FISHING_TOWER_UP, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, RegionName.STANHAMN_OUTSIDE_HYDROPLANT,
               ConnectionName.GHOST_DRAWBRIDGE_LEFT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM,
               ConnectionName.GHOST_DRAWBRIDGE_FROM_TOP, ERGroups.EXCLUDED, CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, RegionName.STANHAMN_FISHING_TOWER,
               ConnectionName.GHOST_DRAWBRIDGE_DOWN, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP,
               ConnectionName.GHOST_DRAWBRIDGE_FROM_BOTTOM, ERGroups.EXCLUDED,
               CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_BUS_STOP,
               ConnectionName.RAFT_DOWN, ERGroups.STANHAMN,
               Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    Connection(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_HYDROPLANT,
               ConnectionName.HYDROPLANT_ENTRANCE, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP,
               ConnectionName.OUTSIDE_HYDROPLANT_RIGHT, ERGroups.STANHAMN),
    Connection(RegionName.STANHAMN_HYDROPLANT, RegionName.STANHAMN_OUTSIDE_HYDROPLANT,
               ConnectionName.HYDROPLANT_EXIT, ERGroups.STANHAMN),

    # Logcity
    Connection(RegionName.LOGCITY_BUS_STOP, RegionName.KIIRUBERG_BUS_STOP,
               ConnectionName.KIIRUBERG_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(Area.LOGCITY)),
    Connection(RegionName.LOGCITY_BUS_STOP, RegionName.LOGCITY_CLOCK_TOWER,
               ConnectionName.ESCALATOR_UP, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_BUS_STOP,
               ConnectionName.LOGCITY_BUS_STOP_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_CROSSWALK,
               ConnectionName.CLOCK_TOWER_LEFT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
               ConnectionName.CLOCK_TOWER_UP, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_OUTSIDE_CAFE,
               ConnectionName.CLOCK_TOWER_RIGHT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CROSSWALK, RegionName.LOGCITY_CLOCK_TOWER,
               ConnectionName.CROSS_WALK_RIGHT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CROSSWALK, RegionName.LOGCITY_OVERPASS,
               ConnectionName.CROSS_WALK_UP, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_CROSSWALK,
               ConnectionName.OVERPASS_DOWN, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_NEWS_HOUSE,
               ConnectionName.NEWS_HOUSE_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_SKATE_PARK,
               ConnectionName.OVERPASS_UP, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
               ConnectionName.OVERPASS_RIGHT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_NEWS_HOUSE, RegionName.LOGCITY_OVERPASS,
               ConnectionName.NEWS_HOUSE_EXIT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_OVERPASS,
               ConnectionName.SKATE_PARK_DOWN, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_RATSKULLZ_ALLEY,
               ConnectionName.SKATE_PARK_RIGHT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_OUTSIDE_CAFE,
               ConnectionName.SKATE_PARK_TAXI, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_RATSKULLZ_ALLEY, RegionName.LOGCITY_SKATE_PARK,
               ConnectionName.RATSKULLZ_ALLEY_EXIT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_FASHION_SHOW_BOTTOM,
               ConnectionName.FASHION_SHOW_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_CLOCK_TOWER,
               ConnectionName.OUTSIDE_FASHION_SHOW_DOWN, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_OVERPASS,
               ConnectionName.OUTSIDE_FASHION_SHOW_LEFT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_OUTSIDE_GALLERY,
               ConnectionName.OUTSIDE_FASHION_SHOW_RIGHT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_FASHION_SHOW_TOP, RegionName.LOGCITY_FASHION_SHOW_BOTTOM,
               ConnectionName.FASHION_SHOW_SECURITY_FROM_TOP, ERGroups.EXCLUDED,
               Has(ItemName.REPORTER_HAT) & CanReachRegion(RegionName.LOGCITY_FASHION_SHOW_BOTTOM)),
    Connection(RegionName.LOGCITY_FASHION_SHOW_TOP, RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE,
               ConnectionName.FASHION_SHOW_BACKSTAGE_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_FASHION_SHOW_BOTTOM, RegionName.LOGCITY_FASHION_SHOW_TOP,
               ConnectionName.FASHION_SHOW_SECURITY_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.REPORTER_HAT)),
    Connection(RegionName.LOGCITY_FASHION_SHOW_BOTTOM, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
               ConnectionName.FASHION_SHOW_EXIT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, RegionName.LOGCITY_FASHION_SHOW_TOP,
               ConnectionName.FASHION_SHOW_BACKSTAGE_EXIT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_CAFE,
               ConnectionName.CAFE_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_CLOCK_TOWER,
               ConnectionName.OUTSIDE_CAFE_LEFT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_OUTSIDE_GALLERY,
               ConnectionName.OUTSIDE_CAFE_UP, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_SKATE_PARK,
               ConnectionName.OUTSIDE_CAFE_TAXI, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_CAFE, RegionName.LOGCITY_OUTSIDE_CAFE,
               ConnectionName.CAFE_EXIT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_GALLERY,
               ConnectionName.GALLERY_ENTRANCE, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_OUTSIDE_CAFE,
               ConnectionName.OUTSIDE_GALLERY_SHOW_DOWN, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
               ConnectionName.OUTSIDE_GALLERY_SHOW_LEFT, ERGroups.LOGCITY),
    Connection(RegionName.LOGCITY_GALLERY, RegionName.LOGCITY_OUTSIDE_GALLERY,
               ConnectionName.GALLERY_EXIT, ERGroups.LOGCITY),

    # Kiiruberg
    Connection(RegionName.KIIRUBERG_BUS_STOP, RegionName.MOUNTAIN_TOP_BUS_STOP,
               ConnectionName.MOUNTAIN_TOP_BUS_STOP, ERGroups.EXCLUDED, get_stamp_rule(Area.KIIRUBERG)),
    Connection(RegionName.KIIRUBERG_BUS_STOP, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
               ConnectionName.KIIRUBERG_BUS_STOP_UP, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP,
               ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BALLOON_HOUSE,
               ConnectionName.BALLOON_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BUS_STOP,
               ConnectionName.BIRTHDAY_PARTY_DOWN, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_FROZEN_POND,
               ConnectionName.BIRTHDAY_PARTY_LEFT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_SKI_LIFT_BASE,
               ConnectionName.BIRTHDAY_PARTY_RIGHT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
               ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,
               ConnectionName.BIRTHDAY_PARTY_UP, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BALLOON_HOUSE, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
               ConnectionName.BALLOON_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_OLD_MANS_HOUSE,
               ConnectionName.OLD_MANS_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
               ConnectionName.FROZEN_POND_RIGHT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OLD_MANS_HOUSE, RegionName.KIIRUBERG_FROZEN_POND,
               ConnectionName.OLD_MANS_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
               ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_MILITARY_BASE,
               ConnectionName.MILITARY_BASE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_MECKS_HOUSE,
               ConnectionName.MECKS_HOUSE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP,
               ConnectionName.SNOWMAN_SQUARE_DOWN, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,
               ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER,
               ConnectionName.SNOWMAN_SQUARE_LEFT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_CLIFFS_BOTTOM,
               ConnectionName.SNOWMAN_SQUARE_UP, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_MILITARY_BASE, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,
               ConnectionName.MILITARY_BASE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_MECKS_HOUSE, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,
               ConnectionName.MECKS_HOUSE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, RegionName.KIIRUBERG_WIZARD_TOWER,
               ConnectionName.WIZARD_TOWER_ENTRANCE, ERGroups.KIIRUBERG, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
               ConnectionName.OUTSIDE_WIZARD_TOWER_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_WIZARD_TOWER, RegionName.KIIRUBERG_COSMO_GARDEN,
               ConnectionName.WIZARD_PORTAL_ENTRANCE, ERGroups.KIIRUBERG,
               CanReachLocation(LocationName.QUEST_ICE_WIZARD)),
    Connection(RegionName.KIIRUBERG_WIZARD_TOWER, RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER,
               ConnectionName.WIZARD_TOWER_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_COSMO_GARDEN, RegionName.KIIRUBERG_WIZARD_TOWER,
               ConnectionName.WIZARD_PORTAL_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_CLIFFS_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
               ConnectionName.CLIFFS_DOWN, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_CLIFFS_BOTTOM, RegionName.KIIRUBERG_CLIFFS_MIDDLE,
               ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT,
               ConnectionName.CLIFFS_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.HONK_ATTACHMENT)),
    Connection(RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_CLIFFS_BOTTOM,
               ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_MIDDLE, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_CLIFFS_TOP,
               ConnectionName.CLIFFS_TOP_ROPE_FROM_MIDDLE, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_CLIFFS_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM,
               ConnectionName.CLIFFS_UP, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_CLIFFS_TOP, RegionName.KIIRUBERG_CLIFFS_MIDDLE,
               ConnectionName.CLIFFS_TOP_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, RegionName.KIIRUBERG_CLIFFS_MIDDLE,
               ConnectionName.BLIZZARD_BRIDGE_LEFT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,
               ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_LEFT, ERGroups.EXCLUDED,
               HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT,
               ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_BOTTOM, ERGroups.EXCLUDED,
               HasAll(ItemName.HONK_ATTACHMENT, ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT,
                      ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, RegionName.KIIRUBERG_MAN_CAVE,
               ConnectionName.MAN_CAVE_ENTRANCE, ERGroups.KIIRUBERG,
               CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,
               ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_LEFT, ERGroups.EXCLUDED,
               HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT,
               ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.HONK_ATTACHMENT)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT,
               ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_RIGHT, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT,
               ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_RIGHT, ERGroups.EXCLUDED,
               HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    Connection(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_MONSTER,
               ConnectionName.BLIZZARD_BRIDGE_RIGHT, ERGroups.KIIRUBERG, Has(ItemName.HONK_ATTACHMENT)),
    Connection(RegionName.KIIRUBERG_MAN_CAVE, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT,
               ConnectionName.MAN_CAVE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_BLIZZARD_MONSTER, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,
               ConnectionName.BLIZZARD_MONSTER_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, RegionName.KIIRUBERG_OBSERVATORY,
               ConnectionName.OBSERVATORY_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM,
               ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP,
               ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, RegionName.KIIRUBERG_CLIFFS_TOP,
               ConnectionName.OUTSIDE_OBSERVATORY_DOWN, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP,
               ConnectionName.OUTSIDE_OBSERVATORY_RIGHT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_OBSERVATORY, RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP,
               ConnectionName.OBSERVATORY_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_SKI_LODGE,
               ConnectionName.SKI_LODGE_ENTRANCE, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
               ConnectionName.SKI_LIFT_BASE_LEFT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP,
               ConnectionName.SKI_LIFT_UP, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_LODGE, RegionName.KIIRUBERG_SKI_LIFT_BASE,
               ConnectionName.SKI_LODGE_EXIT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM,
               ConnectionName.SKI_MOUNTAIN_TOP_LEFT, ERGroups.KIIRUBERG),
    Connection(RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, RegionName.KIIRUBERG_SKI_LIFT_BASE,
               ConnectionName.SKI_LIFT_DOWN, ERGroups.KIIRUBERG),

    # Mountain top
    Connection(RegionName.MOUNTAIN_TOP_BUS_STOP, RegionName.MOUNTAIN_TOP_TOEM,
               ConnectionName.MOUNTAIN_TOP_BUS_STOP_CLIMB, ERGroups.MOUNTAIN_TOP, Has(ItemName.CLIMBING_BOOTS)),
    Connection(RegionName.MOUNTAIN_TOP_TOEM, RegionName.MOUNTAIN_TOP_BUS_STOP,
               ConnectionName.TOEM_DESCEND, ERGroups.MOUNTAIN_TOP, Has(ItemName.CLIMBING_BOOTS)),

    # Basto
    Connection(RegionName.BASTO_BUS_STOP_TOP, RegionName.BASTO_BUS_STOP_BOTTOM,
               ConnectionName.BASTO_HARBOR_GATE_FROM_TOP, ERGroups.EXCLUDED, Has(ItemName.WATERGUN)),
    Connection(RegionName.BASTO_BUS_STOP_TOP, RegionName.BASTO_LILY_PAD_POND_LEFT,
               ConnectionName.BASTO_HARBOR_UP, ERGroups.BASTO),
    Connection(RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BASTO_BUS_STOP_TOP,
               ConnectionName.BASTO_HARBOR_GATE_FROM_BOTTOM, ERGroups.EXCLUDED, Has(ItemName.WATERGUN)),
    Connection(RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.STANHAMN_DOCKS_LEFT,
               ConnectionName.VIKING_EXPRESS_BASTO_STOP, ERGroups.EXCLUDED, Has(ItemName.BASTO_TICKET)),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_BUS_STOP_TOP,
               ConnectionName.LILY_PAD_POND_DOWN, ERGroups.BASTO),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_CAMP,
               ConnectionName.LILY_PAD_POND_LEFT, ERGroups.BASTO),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_LILY_PAD_POND_RIGHT,
               ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_LEFT, ERGroups.EXCLUDED,
               Has(EventName.BASTO_LILY_PAD_POND_LEFT_NIGHT)),
    Connection(RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_GHOST_HANGOUT,
               ConnectionName.LILY_PAD_POND_RIGHT, ERGroups.BASTO),
    Connection(RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_OUTSIDE_CASTLE,
               ConnectionName.LILY_PAD_POND_UP, ERGroups.BASTO),
    Connection(RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_LILY_PAD_POND_LEFT,
               ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_RIGHT, ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_CAMP, RegionName.BASTO_TENT,
               ConnectionName.TENT_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_CAMP, RegionName.BASTO_LILY_PAD_POND_LEFT,
               ConnectionName.CAMPSITE_RIGHT, ERGroups.BASTO),
    Connection(RegionName.BASTO_TENT, RegionName.BASTO_CAMP,
               ConnectionName.TENT_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_CASTLE,
               ConnectionName.CASTLE_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_GYM_HOUSE,
               ConnectionName.GYM_HOUSE_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_LILY_PAD_POND_RIGHT,
               ConnectionName.OUTSIDE_CASTLE_DOWN, ERGroups.BASTO),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_BONFIRE_TOP,
               ConnectionName.OUTSIDE_CASTLE_LEFT, ERGroups.BASTO),
    Connection(RegionName.BASTO_CASTLE, RegionName.BASTO_OUTSIDE_CASTLE,
               ConnectionName.CASTLE_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_GYM_HOUSE, RegionName.BASTO_OUTSIDE_CASTLE,
               ConnectionName.GYM_HOUSE_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_OUTSIDE_CASTLE,
               ConnectionName.BONFIRE_LOWER_RIGHT, ERGroups.BASTO),
    Connection(RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_JUNGLE,
               ConnectionName.BONFIRE_UPPER_RIGHT, ERGroups.BASTO),
    Connection(RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_BONFIRE_BOTTOM,
               ConnectionName.BONFIRE_DAY_BRIDGE_FROM_TOP, ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BONFIRE_BOTTOM, RegionName.BASTO_CARNIVAL,
               ConnectionName.CARNIVAL_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_BONFIRE_BOTTOM, RegionName.BASTO_BONFIRE_TOP,
               ConnectionName.BONFIRE_DAY_BRIDGE_FROM_BOTTOM, ERGroups.EXCLUDED,
               Has(EventName.BASTO_BONFIRE_BOTTOM_DAY)),
    Connection(RegionName.BASTO_CARNIVAL, RegionName.BASTO_BONFIRE_BOTTOM,
               ConnectionName.CARNIVAL_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_CAVE,
               ConnectionName.GHOST_HANGOUT_CAVE_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_LILY_PAD_POND_RIGHT,
               ConnectionName.GHOST_HANGOUT_LEFT, ERGroups.BASTO),
    Connection(RegionName.BASTO_CAVE, RegionName.BASTO_SECRET_CAVE,
               ConnectionName.SECRET_CAVE_ROOM_ENTRANCE, ERGroups.BASTO, HasAll(ItemName.PICKAXE, ItemName.WATERGUN)),
    Connection(RegionName.BASTO_CAVE, RegionName.BASTO_GHOST_HANGOUT,
               ConnectionName.GHOST_HANGOUT_CAVE_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_CAVE, RegionName.BASTO_JUNGLE,
               ConnectionName.JUNGLE_CAVE_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_SECRET_CAVE, RegionName.BASTO_CAVE,
               ConnectionName.SECRET_CAVE_ROOM_EXIT, ERGroups.BASTO),
    Connection(RegionName.BASTO_JUNGLE, RegionName.BASTO_CAVE,
               ConnectionName.JUNGLE_CAVE_ENTRANCE, ERGroups.BASTO),
    Connection(RegionName.BASTO_JUNGLE, RegionName.BASTO_BONFIRE_TOP,
               ConnectionName.JUNGLE_LEFT, ERGroups.BASTO),

    # Helper connections
    # Super region connections
    *[Connection(region, RegionName.OAKLAVILLE,
                 f"{region} in {Area.OAKLAVILLE}", ERGroups.EXCLUDED) for region in oaklaville_regions],
    *[Connection(region, RegionName.STANHAMN,
                 f"{region} in {Area.STANHAMN}", ERGroups.EXCLUDED) for region in stanhamn_regions],
    *[Connection(region, RegionName.LOGCITY,
                 f"{region} in {Area.LOGCITY}", ERGroups.EXCLUDED) for region in logcity_regions],
    *[Connection(region, RegionName.KIIRUBERG,
                 f"{region} in {Area.KIIRUBERG}", ERGroups.EXCLUDED) for region in kiiruberg_regions],
    *[Connection(region, RegionName.MOUNTAIN_TOP,
                 f"{region} in {Area.MOUNTAIN_TOP}", ERGroups.EXCLUDED) for region in mountain_top_regions],
    *[Connection(region, RegionName.BASTO,
                 f"{region} in {Area.BASTO}", ERGroups.EXCLUDED) for region in basto_regions],
    # Compendium connections
    Connection(RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.SQUIRRELS,
               "Squirrel from Ghost cup game", ERGroups.EXCLUDED),
    Connection(RegionName.OAKLAVILLE_HOTEL_ELEVATOR, RegionName.SQUIRRELS,
               "Squirrels from Hotel elevator", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_BUS_STOP, RegionName.SEAGULLS,
               "Seagulls from Stanhamn bus stop", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_HIPPO_BEACH, RegionName.SEAGULLS,
               "Seagulls from Hippo beach", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.SEAGULLS,
               "Seagulls from Outside lighthouse", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_DOCKS_LEFT, RegionName.SUNDAY_SWAN,
               "Sunday swan from Docks left", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_DOCKS_RIGHT, RegionName.SUNDAY_SWAN,
               "Sunday swan from Docks right", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_CLOCK_TOWER, RegionName.PIGEON,
               "Pigeon from Clock tower", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.PIGEON,
               "Pigeon from Outside cafe", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.PIGEON,
               "Pigeon from Outside gallery", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_RATSKULLZ_ALLEY, RegionName.PIGEON,
               "Pigeon from Ratskullz alley", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.GOAT,
               "Goat from Birthday party bottom", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.GOAT,
               "Goat from Birthday party top", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, RegionName.GOAT,
               "Goat from Ski mountain top", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_CLIFFS_TOP, RegionName.GOAT,
               "Goat from Cliffs top", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.GOAT,
               "Goat from Cliffs middle", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_CAVE, RegionName.BAT,
               "Bat from Cave", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BONFIRE_TOP, RegionName.BAT,
               "Bat from Bonfire top", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BAT,
               "Bat from Outside castle", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BEAK_BIRD,
               "Beak bird from Harbor bottom", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BUS_STOP_TOP, RegionName.BEAK_BIRD,
               "Beak bird from Harbor top", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BEAK_BIRD,
               "Beak bird from Lily pad pond left", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BEAK_BIRD,
               "Beak bird from Lily pad pond right", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BITLING_TATO,
               "Bitling tato from Harbor bottom", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BUS_STOP_TOP, RegionName.BITLING_TATO,
               "Bitling tato from Harbor top", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.WATER_STRIDER,
               "Water strider from Lily pad pond left", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_OUTSIDE_CASTLE, RegionName.WATER_STRIDER,
               "Water strider from Outside castle", ERGroups.EXCLUDED),
    # Achievement connections
    Connection(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.GOOD_BOY,
               "Pet Tom", ERGroups.EXCLUDED),
    Connection(RegionName.OAKLAVILLE_HOTEL, RegionName.GOOD_BOY,
               "Pet Oskar", ERGroups.EXCLUDED),
    Connection(RegionName.OAKLAVILLE_GRAVEYARD, RegionName.GOOD_BOY,
               "Pet Sero", ERGroups.EXCLUDED),
    Connection(RegionName.OAKLAVILLE_CAMP, RegionName.GOOD_BOY,
               "Pet the Pet rock", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_DOCKS_RIGHT, RegionName.GOOD_BOY,
               "Pet Fia", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_DOCKS_LEFT, RegionName.GOOD_BOY,
               "Pet Fräs", ERGroups.EXCLUDED),
    Connection(RegionName.STANHAMN_KING_FISH_BEACH, RegionName.GOOD_BOY,
               "Pet Willemijn", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.GOOD_BOY,
               "Pet Portillo", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_BALLOON_HOUSE, RegionName.GOOD_BOY,
               "Pet Mikée or Nariko", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_MECKS_HOUSE, RegionName.GOOD_BOY,
               "Pet Teddy", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.MAXIMUM_VACATION,
               "Sit on a chair in Lily pad pond left", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_GYM_HOUSE, RegionName.MAXIMUM_VACATION,
               "Sit on a chair in Gym house", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_CARNIVAL, RegionName.MAXIMUM_VACATION,
               "Sit on a chair in Carnival", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_BONFIRE_TOP, RegionName.MAXIMUM_VACATION,
               "Sit on a chair in Bonfire top", ERGroups.EXCLUDED),
    Connection(RegionName.BASTO_GHOST_HANGOUT, RegionName.MAXIMUM_VACATION,
               "Sit on a chair in Ghost hangout", ERGroups.EXCLUDED),
    # Cassette connections
    Connection(RegionName.LOGCITY_BUS_STOP, RegionName.BIG_CITY_TAPE,
               "Visit Logicity bus stop", ERGroups.EXCLUDED),
    Connection(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.BIG_CITY_TAPE,
               "Visit Outside fasion show", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.STORIES_OF_SNOW_TAPE,
               "Visit Birthday party bottom", ERGroups.EXCLUDED),
    Connection(RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.STORIES_OF_SNOW_TAPE,
               "Visit Birthday party top", ERGroups.EXCLUDED),
]

connection_name_to_id: dict[str, int] = {connection.name: i for i, connection in enumerate(region_connections, start=1)}


required_regions_always = {
    ConnectionName.OAKLAVILLE_TRAIL_DOWN: (RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_BUS_STOP,
                                           RegionName.OAKLAVILLE_HOTEL),
    ConnectionName.HOTEL_EXIT: (RegionName.OAKLAVILLE_LOOKOUT,),
    ConnectionName.DOCKS_LEFT_EXIT: (RegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.DOCKS_RIGHT_EXIT: (RegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.GHOST_DRAWBRIDGE_LEFT: (RegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.GHOST_DRAWBRIDGE_DOWN: (RegionName.STANHAMN_HYDROPLANT,),
    ConnectionName.WIZARD_TOWER_EXIT: (RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,),
}
required_regions_no_items = required_regions_always | {
    ConnectionName.OUTSIDE_RAVE_LEFT: (RegionName.OAKLAVILLE_GRAVEYARD,),
    ConnectionName.FASHION_SHOW_EXIT: (RegionName.LOGCITY_NEWS_HOUSE,),
    ConnectionName.BIRTHDAY_PARTY_UP: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.WIZARD_TOWER_ENTRANCE: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.OUTSIDE_WIZARD_TOWER_RIGHT: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_DOWN: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_RIGHT: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.CLIFFS_UP: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.OBSERVATORY_ENTRANCE: (RegionName.KIIRUBERG_FROZEN_POND,),
    ConnectionName.WIZARD_TOWER_EXIT: (RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_SKI_LODGE,
                                    RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.BLIZZARD_BRIDGE_LEFT: (RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_SKI_LODGE,
                                          RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.BLIZZARD_BRIDGE_RIGHT: (RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_SKI_LODGE,
                                           RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
    ConnectionName.MAN_CAVE_ENTRANCE: (RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_SKI_LODGE,
                                       RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
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
                ConnectionName.HYDROPLANT_EXIT: Area.STANHAMN,
                ConnectionName.LOOKOUT_EXIT: Area.OAKLAVILLE,
            }
            if not er_state.world.options.include_items:
                expanding_dead_ends |= {
                    ConnectionName.LIGHTHOUSE_ROOF_EXIT: Area.STANHAMN,
                    ConnectionName.NEWS_HOUSE_EXIT: Area.LOGCITY,
                    ConnectionName.SKI_LODGE_EXIT: Area.KIIRUBERG,
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

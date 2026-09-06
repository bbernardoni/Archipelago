from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar, final

from BaseClasses import Entrance, Region
from entrance_rando import ERPlacementState
from rule_builder.rules import CanReachLocation, CanReachRegion, Has, HasAll, Rule, True_

from .items import HardLogic, ItemName
from .locations import EventName, LocationName, get_stamp_rule
from .regions import Area, RegionName, area_lists


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
    group: int = ERGroups.EXCLUDED
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


region_connections: dict[str, Connection] = {
    # Menu
    ConnectionName.START_GAME: Connection(RegionName.START_MENU, RegionName.HOMELANDA_PLAYER_ROOM),

    # Homelanda
    ConnectionName.PLAYER_ROOM_EXIT: Connection(
        RegionName.HOMELANDA_PLAYER_ROOM, RegionName.HOMELANDA_LIVING_ROOM, ERGroups.HOMELANDA),
    ConnectionName.PLAYER_ROOM_ENTRANCE: Connection(
        RegionName.HOMELANDA_LIVING_ROOM, RegionName.HOMELANDA_PLAYER_ROOM, ERGroups.HOMELANDA),
    ConnectionName.HOMELANDA_HOUSE_EXIT: Connection(
        RegionName.HOMELANDA_LIVING_ROOM, RegionName.HOMELANDA_BUS_STOP, ERGroups.HOMELANDA),
    ConnectionName.HOMELANDA_HOUSE_ENTRANCE: Connection(
        RegionName.HOMELANDA_BUS_STOP, RegionName.HOMELANDA_LIVING_ROOM, ERGroups.HOMELANDA),
    ConnectionName.OAKLAVILLE_BUS_STOP: Connection(
        RegionName.HOMELANDA_BUS_STOP, RegionName.OAKLAVILLE_BUS_STOP, ERGroups.EXCLUDED,
        get_stamp_rule(Area.HOMELANDA)),

    # Oaklaville
    ConnectionName.STANHAMN_BUS_STOP: Connection(
        RegionName.OAKLAVILLE_BUS_STOP, RegionName.STANHAMN_BUS_STOP, ERGroups.EXCLUDED,
        get_stamp_rule(Area.OAKLAVILLE)),
    ConnectionName.OAKLAVILLE_BUS_STOP_EXIT: Connection(
        RegionName.OAKLAVILLE_BUS_STOP, RegionName.OAKLAVILLE_OUTSIDE_HOTEL, ERGroups.OAKLAVILLE),
    ConnectionName.OUTSIDE_HOTEL_DOWN: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_BUS_STOP, ERGroups.OAKLAVILLE),
    ConnectionName.OUTSIDE_HOTEL_LEFT: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_GHOST_CUP_GAME, ERGroups.OAKLAVILLE),
    ConnectionName.OUTSIDE_HOTEL_RIGHT: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_CAMP, ERGroups.OAKLAVILLE),
    ConnectionName.HOTEL_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_HOTEL, ERGroups.OAKLAVILLE),
    ConnectionName.HOTEL_EXIT: Connection(
        RegionName.OAKLAVILLE_HOTEL, RegionName.OAKLAVILLE_OUTSIDE_HOTEL, ERGroups.OAKLAVILLE),
    ConnectionName.HOTEL_ELEVATOR_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_HOTEL, RegionName.OAKLAVILLE_HOTEL_ELEVATOR, ERGroups.OAKLAVILLE,
        CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    ConnectionName.HOTEL_ELEVATOR_EXIT: Connection(
        RegionName.OAKLAVILLE_HOTEL_ELEVATOR, RegionName.OAKLAVILLE_HOTEL, ERGroups.OAKLAVILLE,
        CanReachLocation(LocationName.QUEST_HOTEL_CHEF)),
    ConnectionName.GHOST_CUP_GAME_RIGHT: Connection(
        RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_OUTSIDE_HOTEL, ERGroups.OAKLAVILLE),
    ConnectionName.MUSHROOM_HOUSE_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_MUSHROOM_HOUSE, ERGroups.OAKLAVILLE),
    ConnectionName.GHOST_CUP_GAME_LEFT: Connection(
        RegionName.OAKLAVILLE_GHOST_CUP_GAME, RegionName.OAKLAVILLE_HIDE_AND_SEEK, ERGroups.OAKLAVILLE),
    ConnectionName.MUSHROOM_HOUSE_EXIT: Connection(
        RegionName.OAKLAVILLE_MUSHROOM_HOUSE, RegionName.OAKLAVILLE_GHOST_CUP_GAME, ERGroups.OAKLAVILLE),
    ConnectionName.HIDE_AND_SEEK_RIGHT: Connection(
        RegionName.OAKLAVILLE_HIDE_AND_SEEK, RegionName.OAKLAVILLE_GHOST_CUP_GAME, ERGroups.OAKLAVILLE),
    ConnectionName.HIDE_AND_SEEK_LEFT: Connection(
        RegionName.OAKLAVILLE_HIDE_AND_SEEK, RegionName.OAKLAVILLE_GRAVEYARD, ERGroups.OAKLAVILLE),
    ConnectionName.GRAVEYARD_RIGHT: Connection(
        RegionName.OAKLAVILLE_GRAVEYARD, RegionName.OAKLAVILLE_HIDE_AND_SEEK, ERGroups.OAKLAVILLE),
    ConnectionName.SKELETON_HOUSE_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_GRAVEYARD, RegionName.OAKLAVILLE_SKELETON_HOUSE, ERGroups.OAKLAVILLE),
    ConnectionName.SKELETON_HOUSE_EXIT: Connection(
        RegionName.OAKLAVILLE_SKELETON_HOUSE, RegionName.OAKLAVILLE_GRAVEYARD, ERGroups.OAKLAVILLE),
    ConnectionName.SKELETON_HOUSE_BALCONY_EXIT: Connection(
        RegionName.OAKLAVILLE_SKELETON_HOUSE, RegionName.OAKLAVILLE_SKELETON_BALCONY, ERGroups.OAKLAVILLE),
    ConnectionName.SKELETON_HOUSE_BALCONY_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_SKELETON_BALCONY, RegionName.OAKLAVILLE_SKELETON_HOUSE, ERGroups.OAKLAVILLE),
    ConnectionName.SCOUT_CAMP_LEFT: Connection(
        RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_OUTSIDE_HOTEL, ERGroups.OAKLAVILLE),
    ConnectionName.SCOUT_CAMP_UP: Connection(
        RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_TRAIL_BOTTOM, ERGroups.OAKLAVILLE),
    ConnectionName.SCOUT_CAMP_RIGHT: Connection(
        RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_PLAYGROUND, ERGroups.OAKLAVILLE),
    ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_TOP: Connection(
        RegionName.OAKLAVILLE_TRAIL_TOP, RegionName.OAKLAVILLE_TRAIL_BOTTOM, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_LOG_JAM)),
    ConnectionName.OAKLAVILLE_TRAIL_UP: Connection(
        RegionName.OAKLAVILLE_TRAIL_TOP, RegionName.OAKLAVILLE_LOOKOUT, ERGroups.OAKLAVILLE),
    ConnectionName.OAKLAVILLE_TRAIL_LOG_FROM_BOTTOM: Connection(
        RegionName.OAKLAVILLE_TRAIL_BOTTOM, RegionName.OAKLAVILLE_TRAIL_TOP, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_LOG_JAM)),
    ConnectionName.OAKLAVILLE_TRAIL_DOWN: Connection(
        RegionName.OAKLAVILLE_TRAIL_BOTTOM, RegionName.OAKLAVILLE_CAMP, ERGroups.OAKLAVILLE),
    ConnectionName.LOOKOUT_EXIT: Connection(
        RegionName.OAKLAVILLE_LOOKOUT, RegionName.OAKLAVILLE_TRAIL_TOP, ERGroups.OAKLAVILLE),
    ConnectionName.PLAYGROUND_LEFT: Connection(
        RegionName.OAKLAVILLE_PLAYGROUND, RegionName.OAKLAVILLE_CAMP, ERGroups.OAKLAVILLE),
    ConnectionName.PLAYGROUND_RIGHT: Connection(
        RegionName.OAKLAVILLE_PLAYGROUND, RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, ERGroups.OAKLAVILLE),
    ConnectionName.RAVE_BOUNCER_FROM_TOP: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM)),
    ConnectionName.RAVE_ENTRANCE: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, RegionName.OAKLAVILLE_RAVE, ERGroups.OAKLAVILLE),
    ConnectionName.RAVE_BOUNCER_FROM_BOTTOM: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, ERGroups.EXCLUDED,
        Has(ItemName.GHOST_GLASSES)),
    ConnectionName.OUTSIDE_RAVE_LEFT: Connection(
        RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, RegionName.OAKLAVILLE_PLAYGROUND, ERGroups.OAKLAVILLE),
    ConnectionName.RAVE_EXIT: Connection(
        RegionName.OAKLAVILLE_RAVE, RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, ERGroups.OAKLAVILLE),

    # Stanhamn
    ConnectionName.LOGCITY_BUS_STOP: Connection(
        RegionName.STANHAMN_BUS_STOP, RegionName.LOGCITY_BUS_STOP, ERGroups.EXCLUDED,
        get_stamp_rule(Area.STANHAMN)),
    ConnectionName.PHOTO_GUILD_HUT_ENTRANCE: Connection(
        RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_PHOTO_GUILD_HUT, ERGroups.STANHAMN),
    ConnectionName.STANHAMN_BUS_STOP_LEFT: Connection(
        RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_PIRATE_DRAWBRIDGE, ERGroups.STANHAMN),
    ConnectionName.STANHAMN_BUS_STOP_RIGHT: Connection(
        RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_DOCKS_LEFT, ERGroups.STANHAMN),
    ConnectionName.RAFT_UP: Connection(
        RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_OUTSIDE_HYDROPLANT, ERGroups.STANHAMN,
        Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.PHOTO_GUILD_HUT_EXIT: Connection(
        RegionName.STANHAMN_PHOTO_GUILD_HUT, RegionName.STANHAMN_BUS_STOP, ERGroups.STANHAMN),
    ConnectionName.PIRATE_DRAWBRIDGE_RIGHT: Connection(
        RegionName.STANHAMN_PIRATE_DRAWBRIDGE, RegionName.STANHAMN_BUS_STOP, ERGroups.STANHAMN),
    ConnectionName.PIRATE_DRAWBRIDGE_LEFT: Connection(
        RegionName.STANHAMN_PIRATE_DRAWBRIDGE, RegionName.STANHAMN_HIPPO_BEACH, ERGroups.STANHAMN),
    ConnectionName.HIPPO_BEACH_RIGHT: Connection(
        RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_PIRATE_DRAWBRIDGE, ERGroups.STANHAMN),
    ConnectionName.HIPPO_BEACH_MANHOLE: Connection(
        RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_UNDERWATER, ERGroups.STANHAMN,
        HasAll(ItemName.HONK_ATTACHMENT, ItemName.DIVING_HELMET)),
    ConnectionName.HIPPO_BEACH_LEFT: Connection(
        RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ERGroups.STANHAMN),
    ConnectionName.UNDERWATER_EXIT: Connection(
        RegionName.STANHAMN_UNDERWATER, RegionName.STANHAMN_HIPPO_BEACH, ERGroups.STANHAMN),
    ConnectionName.OUTSIDE_LIGHTHOUSE_RIGHT: Connection(
        RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_HIPPO_BEACH, ERGroups.STANHAMN),
    ConnectionName.OUTSIDE_LIGHTHOUSE_UP: Connection(
        RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_KING_FISH_BEACH, ERGroups.STANHAMN,
        Has(ItemName.HONK_ATTACHMENT)),
    ConnectionName.LIGHTHOUSE_ENTRANCE: Connection(
        RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE, ERGroups.STANHAMN),
    ConnectionName.LIGHTHOUSE_EXIT: Connection(
        RegionName.STANHAMN_LIGHTHOUSE, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ERGroups.STANHAMN),
    ConnectionName.LIGHTHOUSE_ROOF_ENTRANCE: Connection(
        RegionName.STANHAMN_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE_ROOF, ERGroups.STANHAMN),
    ConnectionName.LIGHTHOUSE_ROOF_EXIT: Connection(
        RegionName.STANHAMN_LIGHTHOUSE_ROOF, RegionName.STANHAMN_LIGHTHOUSE, ERGroups.STANHAMN),
    ConnectionName.KING_FISH_BEACH_EXIT: Connection(
        RegionName.STANHAMN_KING_FISH_BEACH, RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, ERGroups.STANHAMN),
    ConnectionName.DOCKS_LEFT_EXIT: Connection(
        RegionName.STANHAMN_DOCKS_LEFT, RegionName.STANHAMN_BUS_STOP, ERGroups.STANHAMN),
    ConnectionName.VIKING_EXPRESS_STAMHAMN_STOP: Connection(
        RegionName.STANHAMN_DOCKS_LEFT, RegionName.BASTO_BUS_STOP_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.BASTO_TICKET)),
    ConnectionName.DOCKS_DRAWBRIDGE_FROM_LEFT: Connection(
        RegionName.STANHAMN_DOCKS_LEFT, RegionName.STANHAMN_DOCKS_RIGHT, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.DOCKS_RIGHT_EXIT: Connection(
        RegionName.STANHAMN_DOCKS_RIGHT, RegionName.STANHAMN_FISHING_TOWER, ERGroups.STANHAMN),
    ConnectionName.DOCKS_DRAWBRIDGE_FROM_RIGHT: Connection(
        RegionName.STANHAMN_DOCKS_RIGHT, RegionName.STANHAMN_DOCKS_LEFT, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.FISHING_TOWER_LEFT: Connection(
        RegionName.STANHAMN_FISHING_TOWER, RegionName.STANHAMN_DOCKS_RIGHT, ERGroups.STANHAMN),
    ConnectionName.FISHING_TOWER_UP: Connection(
        RegionName.STANHAMN_FISHING_TOWER, RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, ERGroups.STANHAMN),
    ConnectionName.GHOST_DRAWBRIDGE_LEFT: Connection(
        RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, RegionName.STANHAMN_OUTSIDE_HYDROPLANT, ERGroups.STANHAMN),
    ConnectionName.GHOST_DRAWBRIDGE_FROM_TOP: Connection(
        RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.GHOST_DRAWBRIDGE_DOWN: Connection(
        RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, RegionName.STANHAMN_FISHING_TOWER, ERGroups.STANHAMN),
    ConnectionName.GHOST_DRAWBRIDGE_FROM_BOTTOM: Connection(
        RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, ERGroups.EXCLUDED,
        CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.RAFT_DOWN: Connection(
        RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_BUS_STOP, ERGroups.STANHAMN,
        Has(ItemName.HONK_ATTACHMENT) | CanReachLocation(LocationName.QUEST_POWER)),
    ConnectionName.HYDROPLANT_ENTRANCE: Connection(
        RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_HYDROPLANT, ERGroups.STANHAMN),
    ConnectionName.OUTSIDE_HYDROPLANT_RIGHT: Connection(
        RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, ERGroups.STANHAMN),
    ConnectionName.HYDROPLANT_EXIT: Connection(
        RegionName.STANHAMN_HYDROPLANT, RegionName.STANHAMN_OUTSIDE_HYDROPLANT, ERGroups.STANHAMN),

    # Logcity
    ConnectionName.KIIRUBERG_BUS_STOP: Connection(
        RegionName.LOGCITY_BUS_STOP, RegionName.KIIRUBERG_BUS_STOP, ERGroups.EXCLUDED,
        get_stamp_rule(Area.LOGCITY)),
    ConnectionName.ESCALATOR_UP: Connection(
        RegionName.LOGCITY_BUS_STOP, RegionName.LOGCITY_CLOCK_TOWER, ERGroups.LOGCITY),
    ConnectionName.LOGCITY_BUS_STOP_ENTRANCE: Connection(
        RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_BUS_STOP, ERGroups.LOGCITY),
    ConnectionName.CLOCK_TOWER_LEFT: Connection(
        RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_CROSSWALK, ERGroups.LOGCITY),
    ConnectionName.CLOCK_TOWER_UP: Connection(
        RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ERGroups.LOGCITY),
    ConnectionName.CLOCK_TOWER_RIGHT: Connection(
        RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_OUTSIDE_CAFE, ERGroups.LOGCITY),
    ConnectionName.CROSS_WALK_RIGHT: Connection(
        RegionName.LOGCITY_CROSSWALK, RegionName.LOGCITY_CLOCK_TOWER, ERGroups.LOGCITY),
    ConnectionName.CROSS_WALK_UP: Connection(
        RegionName.LOGCITY_CROSSWALK, RegionName.LOGCITY_OVERPASS, ERGroups.LOGCITY),
    ConnectionName.OVERPASS_DOWN: Connection(
        RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_CROSSWALK, ERGroups.LOGCITY),
    ConnectionName.NEWS_HOUSE_ENTRANCE: Connection(
        RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_NEWS_HOUSE, ERGroups.LOGCITY),
    ConnectionName.OVERPASS_UP: Connection(
        RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_SKATE_PARK, ERGroups.LOGCITY),
    ConnectionName.OVERPASS_RIGHT: Connection(
        RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ERGroups.LOGCITY),
    ConnectionName.NEWS_HOUSE_EXIT: Connection(
        RegionName.LOGCITY_NEWS_HOUSE, RegionName.LOGCITY_OVERPASS, ERGroups.LOGCITY),
    ConnectionName.SKATE_PARK_DOWN: Connection(
        RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_OVERPASS, ERGroups.LOGCITY),
    ConnectionName.SKATE_PARK_RIGHT: Connection(
        RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_RATSKULLZ_ALLEY, ERGroups.LOGCITY),
    ConnectionName.SKATE_PARK_TAXI: Connection(
        RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_OUTSIDE_CAFE, ERGroups.LOGCITY),
    ConnectionName.RATSKULLZ_ALLEY_EXIT: Connection(
        RegionName.LOGCITY_RATSKULLZ_ALLEY, RegionName.LOGCITY_SKATE_PARK, ERGroups.LOGCITY),
    ConnectionName.FASHION_SHOW_ENTRANCE: Connection(
        RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_FASHION_SHOW_BOTTOM, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_FASHION_SHOW_DOWN: Connection(
        RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_CLOCK_TOWER, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_FASHION_SHOW_LEFT: Connection(
        RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_OVERPASS, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_FASHION_SHOW_RIGHT: Connection(
        RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_OUTSIDE_GALLERY, ERGroups.LOGCITY),
    ConnectionName.FASHION_SHOW_SECURITY_FROM_TOP: Connection(
        RegionName.LOGCITY_FASHION_SHOW_TOP, RegionName.LOGCITY_FASHION_SHOW_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.REPORTER_HAT) & CanReachRegion(RegionName.LOGCITY_FASHION_SHOW_BOTTOM)),
    ConnectionName.FASHION_SHOW_BACKSTAGE_ENTRANCE: Connection(
        RegionName.LOGCITY_FASHION_SHOW_TOP, RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, ERGroups.LOGCITY),
    ConnectionName.FASHION_SHOW_SECURITY_FROM_BOTTOM: Connection(
        RegionName.LOGCITY_FASHION_SHOW_BOTTOM, RegionName.LOGCITY_FASHION_SHOW_TOP, ERGroups.EXCLUDED,
        Has(ItemName.REPORTER_HAT)),
    ConnectionName.FASHION_SHOW_EXIT: Connection(
        RegionName.LOGCITY_FASHION_SHOW_BOTTOM, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ERGroups.LOGCITY),
    ConnectionName.FASHION_SHOW_BACKSTAGE_EXIT: Connection(
        RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, RegionName.LOGCITY_FASHION_SHOW_TOP, ERGroups.LOGCITY),
    ConnectionName.CAFE_ENTRANCE: Connection(
        RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_CAFE, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_CAFE_LEFT: Connection(
        RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_CLOCK_TOWER, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_CAFE_UP: Connection(
        RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_OUTSIDE_GALLERY, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_CAFE_TAXI: Connection(
        RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_SKATE_PARK, ERGroups.LOGCITY),
    ConnectionName.CAFE_EXIT: Connection(
        RegionName.LOGCITY_CAFE, RegionName.LOGCITY_OUTSIDE_CAFE, ERGroups.LOGCITY),
    ConnectionName.GALLERY_ENTRANCE: Connection(
        RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_GALLERY, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_GALLERY_SHOW_DOWN: Connection(
        RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_OUTSIDE_CAFE, ERGroups.LOGCITY),
    ConnectionName.OUTSIDE_GALLERY_SHOW_LEFT: Connection(
        RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, ERGroups.LOGCITY),
    ConnectionName.GALLERY_EXIT: Connection(
        RegionName.LOGCITY_GALLERY, RegionName.LOGCITY_OUTSIDE_GALLERY, ERGroups.LOGCITY),

    # Kiiruberg
    ConnectionName.MOUNTAIN_TOP_BUS_STOP: Connection(
        RegionName.KIIRUBERG_BUS_STOP, RegionName.MOUNTAIN_TOP_BUS_STOP, ERGroups.EXCLUDED,
        get_stamp_rule(Area.KIIRUBERG)),
    ConnectionName.KIIRUBERG_BUS_STOP_UP: Connection(
        RegionName.KIIRUBERG_BUS_STOP, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_BOTTOM: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.BALLOON_HOUSE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BALLOON_HOUSE, ERGroups.KIIRUBERG),
    ConnectionName.BIRTHDAY_PARTY_DOWN: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_BUS_STOP, ERGroups.KIIRUBERG),
    ConnectionName.BIRTHDAY_PARTY_LEFT: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_FROZEN_POND, ERGroups.KIIRUBERG),
    ConnectionName.BIRTHDAY_PARTY_RIGHT: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, RegionName.KIIRUBERG_SKI_LIFT_BASE, ERGroups.KIIRUBERG),
    ConnectionName.BIRTHDAY_PARTY_ROPE_FROM_TOP: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.BIRTHDAY_PARTY_UP: Connection(
        RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.BALLOON_HOUSE_EXIT: Connection(
        RegionName.KIIRUBERG_BALLOON_HOUSE, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.OLD_MANS_HOUSE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_OLD_MANS_HOUSE, ERGroups.KIIRUBERG),
    ConnectionName.FROZEN_POND_RIGHT: Connection(
        RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.OLD_MANS_HOUSE_EXIT: Connection(
        RegionName.KIIRUBERG_OLD_MANS_HOUSE, RegionName.KIIRUBERG_FROZEN_POND, ERGroups.KIIRUBERG),
    ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_BOTTOM: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.MILITARY_BASE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_MILITARY_BASE, ERGroups.KIIRUBERG),
    ConnectionName.MECKS_HOUSE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_MECKS_HOUSE, ERGroups.KIIRUBERG),
    ConnectionName.SNOWMAN_SQUARE_DOWN: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, ERGroups.KIIRUBERG),
    ConnectionName.SNOWMAN_SQUARE_ROPE_FROM_TOP: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.SNOWMAN_SQUARE_LEFT: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, ERGroups.KIIRUBERG),
    ConnectionName.SNOWMAN_SQUARE_UP: Connection(
        RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, RegionName.KIIRUBERG_CLIFFS_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.MILITARY_BASE_EXIT: Connection(
        RegionName.KIIRUBERG_MILITARY_BASE, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.MECKS_HOUSE_EXIT: Connection(
        RegionName.KIIRUBERG_MECKS_HOUSE, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.WIZARD_TOWER_ENTRANCE: Connection(
        RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, RegionName.KIIRUBERG_WIZARD_TOWER, ERGroups.KIIRUBERG,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.OUTSIDE_WIZARD_TOWER_RIGHT: Connection(
        RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ERGroups.KIIRUBERG,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.WIZARD_PORTAL_ENTRANCE: Connection(
        RegionName.KIIRUBERG_WIZARD_TOWER, RegionName.KIIRUBERG_COSMO_GARDEN, ERGroups.KIIRUBERG,
        CanReachLocation(LocationName.QUEST_ICE_WIZARD)),
    ConnectionName.WIZARD_TOWER_EXIT: Connection(
        RegionName.KIIRUBERG_WIZARD_TOWER, RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, ERGroups.KIIRUBERG),
    ConnectionName.WIZARD_PORTAL_EXIT: Connection(
        RegionName.KIIRUBERG_COSMO_GARDEN, RegionName.KIIRUBERG_WIZARD_TOWER, ERGroups.KIIRUBERG),
    ConnectionName.CLIFFS_DOWN: Connection(
        RegionName.KIIRUBERG_CLIFFS_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, ERGroups.KIIRUBERG),
    ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_BOTTOM: Connection(
        RegionName.KIIRUBERG_CLIFFS_BOTTOM, RegionName.KIIRUBERG_CLIFFS_MIDDLE, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.CLIFFS_RIGHT: Connection(
        RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, ERGroups.KIIRUBERG,
        Has(ItemName.HONK_ATTACHMENT)),
    ConnectionName.CLIFFS_BOTTOM_ROPE_FROM_MIDDLE: Connection(
        RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_CLIFFS_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.CLIFFS_TOP_ROPE_FROM_MIDDLE: Connection(
        RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_CLIFFS_TOP, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.CLIFFS_UP: Connection(
        RegionName.KIIRUBERG_CLIFFS_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.CLIFFS_TOP_ROPE_FROM_TOP: Connection(
        RegionName.KIIRUBERG_CLIFFS_TOP, RegionName.KIIRUBERG_CLIFFS_MIDDLE, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.BLIZZARD_BRIDGE_LEFT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, RegionName.KIIRUBERG_CLIFFS_MIDDLE, ERGroups.KIIRUBERG),
    ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_LEFT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ERGroups.EXCLUDED,
        HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_BOTTOM: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, ERGroups.EXCLUDED,
        HasAll(ItemName.HONK_ATTACHMENT, ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT,
               ItemName.SCARF, ItemName.SKI_GOGGLES)),
    ConnectionName.MAN_CAVE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, RegionName.KIIRUBERG_MAN_CAVE, ERGroups.KIIRUBERG,
        CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)),
    ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_LEFT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ERGroups.EXCLUDED,
        HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    ConnectionName.BLIZZARD_BRIDGE_BREAK_ICE_FROM_TOP: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, ERGroups.EXCLUDED,
        Has(ItemName.HONK_ATTACHMENT)),
    ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_LOWER_RIGHT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.BLIZZARD_BRIDGE_ROPE_FROM_UPPER_RIGHT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, ERGroups.EXCLUDED,
        HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)),
    ConnectionName.BLIZZARD_BRIDGE_RIGHT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_BLIZZARD_MONSTER, ERGroups.KIIRUBERG,
        Has(ItemName.HONK_ATTACHMENT)),
    ConnectionName.MAN_CAVE_EXIT: Connection(
        RegionName.KIIRUBERG_MAN_CAVE, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL, ERGroups.KIIRUBERG),
    ConnectionName.BLIZZARD_MONSTER_EXIT: Connection(
        RegionName.KIIRUBERG_BLIZZARD_MONSTER, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, ERGroups.KIIRUBERG),
    ConnectionName.OBSERVATORY_ENTRANCE: Connection(
        RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP, RegionName.KIIRUBERG_OBSERVATORY, ERGroups.KIIRUBERG),
    ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_TOP: Connection(
        RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.OUTSIDE_OBSERVATORY_ROPE_FROM_BOTTOM: Connection(
        RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP, ERGroups.EXCLUDED,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.OUTSIDE_OBSERVATORY_DOWN: Connection(
        RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, RegionName.KIIRUBERG_CLIFFS_TOP, ERGroups.KIIRUBERG),
    ConnectionName.OUTSIDE_OBSERVATORY_RIGHT: Connection(
        RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, ERGroups.KIIRUBERG),
    ConnectionName.OBSERVATORY_EXIT: Connection(
        RegionName.KIIRUBERG_OBSERVATORY, RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP, ERGroups.KIIRUBERG),
    ConnectionName.SKI_LODGE_ENTRANCE: Connection(
        RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_SKI_LODGE, ERGroups.KIIRUBERG),
    ConnectionName.SKI_LIFT_BASE_LEFT: Connection(
        RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.SKI_LIFT_UP: Connection(
        RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, ERGroups.KIIRUBERG),
    ConnectionName.SKI_LODGE_EXIT: Connection(
        RegionName.KIIRUBERG_SKI_LODGE, RegionName.KIIRUBERG_SKI_LIFT_BASE, ERGroups.KIIRUBERG),
    ConnectionName.SKI_MOUNTAIN_TOP_LEFT: Connection(
        RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, ERGroups.KIIRUBERG),
    ConnectionName.SKI_LIFT_DOWN: Connection(
        RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, RegionName.KIIRUBERG_SKI_LIFT_BASE, ERGroups.KIIRUBERG),

    # Mountain top
    ConnectionName.MOUNTAIN_TOP_BUS_STOP_CLIMB: Connection(
        RegionName.MOUNTAIN_TOP_BUS_STOP, RegionName.MOUNTAIN_TOP_TOEM, ERGroups.MOUNTAIN_TOP,
        Has(ItemName.CLIMBING_BOOTS)),
    ConnectionName.TOEM_DESCEND: Connection(
        RegionName.MOUNTAIN_TOP_TOEM, RegionName.MOUNTAIN_TOP_BUS_STOP, ERGroups.MOUNTAIN_TOP,
        Has(ItemName.CLIMBING_BOOTS)),

    # Basto
    ConnectionName.BASTO_HARBOR_GATE_FROM_TOP: Connection(
        RegionName.BASTO_BUS_STOP_TOP, RegionName.BASTO_BUS_STOP_BOTTOM, ERGroups.EXCLUDED,
        Has(ItemName.WATERGUN)),
    ConnectionName.BASTO_HARBOR_UP: Connection(
        RegionName.BASTO_BUS_STOP_TOP, RegionName.BASTO_LILY_PAD_POND_LEFT, ERGroups.BASTO),
    ConnectionName.BASTO_HARBOR_GATE_FROM_BOTTOM: Connection(
        RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BASTO_BUS_STOP_TOP, ERGroups.EXCLUDED,
        Has(ItemName.WATERGUN)),
    ConnectionName.VIKING_EXPRESS_BASTO_STOP: Connection(
        RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.STANHAMN_DOCKS_LEFT, ERGroups.EXCLUDED,
        Has(ItemName.BASTO_TICKET)),
    ConnectionName.LILY_PAD_POND_DOWN: Connection(
        RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_BUS_STOP_TOP, ERGroups.BASTO),
    ConnectionName.LILY_PAD_POND_LEFT: Connection(
        RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_CAMP, ERGroups.BASTO),
    ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_LEFT: Connection(
        RegionName.BASTO_LILY_PAD_POND_LEFT, RegionName.BASTO_LILY_PAD_POND_RIGHT, ERGroups.EXCLUDED,
        Has(EventName.BASTO_LILY_PAD_POND_LEFT_NIGHT)),
    ConnectionName.LILY_PAD_POND_RIGHT: Connection(
        RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_GHOST_HANGOUT, ERGroups.BASTO),
    ConnectionName.LILY_PAD_POND_UP: Connection(
        RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_OUTSIDE_CASTLE, ERGroups.BASTO),
    ConnectionName.LILY_PAD_POND_NIGHT_BRIDGE_FROM_RIGHT: Connection(
        RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_LILY_PAD_POND_LEFT, ERGroups.EXCLUDED),
    ConnectionName.TENT_ENTRANCE: Connection(
        RegionName.BASTO_CAMP, RegionName.BASTO_TENT, ERGroups.BASTO),
    ConnectionName.CAMPSITE_RIGHT: Connection(
        RegionName.BASTO_CAMP, RegionName.BASTO_LILY_PAD_POND_LEFT, ERGroups.BASTO),
    ConnectionName.TENT_EXIT: Connection(
        RegionName.BASTO_TENT, RegionName.BASTO_CAMP, ERGroups.BASTO),
    ConnectionName.CASTLE_ENTRANCE: Connection(
        RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_CASTLE, ERGroups.BASTO),
    ConnectionName.GYM_HOUSE_ENTRANCE: Connection(
        RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_GYM_HOUSE, ERGroups.BASTO),
    ConnectionName.OUTSIDE_CASTLE_DOWN: Connection(
        RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_LILY_PAD_POND_RIGHT, ERGroups.BASTO),
    ConnectionName.OUTSIDE_CASTLE_LEFT: Connection(
        RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_BONFIRE_TOP, ERGroups.BASTO),
    ConnectionName.CASTLE_EXIT: Connection(
        RegionName.BASTO_CASTLE, RegionName.BASTO_OUTSIDE_CASTLE, ERGroups.BASTO),
    ConnectionName.GYM_HOUSE_EXIT: Connection(
        RegionName.BASTO_GYM_HOUSE, RegionName.BASTO_OUTSIDE_CASTLE, ERGroups.BASTO),
    ConnectionName.BONFIRE_LOWER_RIGHT: Connection(
        RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_OUTSIDE_CASTLE, ERGroups.BASTO),
    ConnectionName.BONFIRE_UPPER_RIGHT: Connection(
        RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_JUNGLE, ERGroups.BASTO),
    ConnectionName.BONFIRE_DAY_BRIDGE_FROM_TOP: Connection(
        RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_BONFIRE_BOTTOM, ERGroups.EXCLUDED),
    ConnectionName.CARNIVAL_ENTRANCE: Connection(
        RegionName.BASTO_BONFIRE_BOTTOM, RegionName.BASTO_CARNIVAL, ERGroups.BASTO),
    ConnectionName.BONFIRE_DAY_BRIDGE_FROM_BOTTOM: Connection(
        RegionName.BASTO_BONFIRE_BOTTOM, RegionName.BASTO_BONFIRE_TOP, ERGroups.EXCLUDED,
        Has(EventName.BASTO_BONFIRE_BOTTOM_DAY)),
    ConnectionName.CARNIVAL_EXIT: Connection(
        RegionName.BASTO_CARNIVAL, RegionName.BASTO_BONFIRE_BOTTOM, ERGroups.BASTO),
    ConnectionName.GHOST_HANGOUT_CAVE_ENTRANCE: Connection(
        RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_CAVE, ERGroups.BASTO),
    ConnectionName.GHOST_HANGOUT_LEFT: Connection(
        RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_LILY_PAD_POND_RIGHT, ERGroups.BASTO),
    ConnectionName.SECRET_CAVE_ROOM_ENTRANCE: Connection(
        RegionName.BASTO_CAVE, RegionName.BASTO_SECRET_CAVE, ERGroups.BASTO,
        HasAll(ItemName.PICKAXE, ItemName.WATERGUN)),
    ConnectionName.GHOST_HANGOUT_CAVE_EXIT: Connection(
        RegionName.BASTO_CAVE, RegionName.BASTO_GHOST_HANGOUT, ERGroups.BASTO),
    ConnectionName.JUNGLE_CAVE_EXIT: Connection(
        RegionName.BASTO_CAVE, RegionName.BASTO_JUNGLE, ERGroups.BASTO),
    ConnectionName.SECRET_CAVE_ROOM_EXIT: Connection(
        RegionName.BASTO_SECRET_CAVE, RegionName.BASTO_CAVE, ERGroups.BASTO),
    ConnectionName.JUNGLE_CAVE_ENTRANCE: Connection(
        RegionName.BASTO_JUNGLE, RegionName.BASTO_CAVE, ERGroups.BASTO),
    ConnectionName.JUNGLE_LEFT: Connection(
        RegionName.BASTO_JUNGLE, RegionName.BASTO_BONFIRE_TOP, ERGroups.BASTO),
}


@dataclass(frozen=True)
class HelperConnection:
    name: str
    dst_region_name: str
    rule: Rule | None = None

helper_region_data: dict[str, list[HelperConnection]] = {
    # Quest connections
    RegionName.FASHION_SHOW: [
        HelperConnection("Fashion show from bottom", RegionName.LOGCITY_FASHION_SHOW_BOTTOM),
        HelperConnection("Fashion show from top", RegionName.LOGCITY_FASHION_SHOW_TOP),
    ],
    RegionName.BALLOON_ANIMAL: [
        HelperConnection("Balloon animal from Birthday party bottom", RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM),
        HelperConnection("Balloon animal from Birthday party top", RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP,
                         HardLogic(True_())),
    ],
    RegionName.ASTEROID: [
        HelperConnection("Asteroid from Snowman square bottom", RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM),
        HelperConnection("Asteroid from Snowman square top", RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
                         HardLogic(True_())),
    ],
    RegionName.BAD_HAIR_DAY: [
        HelperConnection("Bad hair day from Bonfire top", RegionName.BASTO_BONFIRE_TOP),
        HelperConnection("Bad hair day from Bonfire bottom", RegionName.BASTO_BONFIRE_BOTTOM,
                         HardLogic(True_())),
    ],
    RegionName.DRY_SEASON_BUS_STOP: [
        HelperConnection("Dry season from Harbor bottom", RegionName.BASTO_BUS_STOP_BOTTOM),
        HelperConnection("Dry season from Harbor top", RegionName.BASTO_BUS_STOP_TOP,
                         HardLogic(True_())),
    ],

    # Compendium connections
    RegionName.SQUIRRELS: [
        HelperConnection("Squirrel from Ghost cup game", RegionName.OAKLAVILLE_GHOST_CUP_GAME),
        HelperConnection("Squirrels from Hotel elevator", RegionName.OAKLAVILLE_HOTEL_ELEVATOR),
    ],
    RegionName.SERO: [
        HelperConnection("Sero from Graveyard", RegionName.OAKLAVILLE_GRAVEYARD),
        HelperConnection("Sero from Skeleton house balcony", RegionName.OAKLAVILLE_SKELETON_BALCONY,
                         HardLogic(True_())),
    ],
    RegionName.TATO_FLY: [
        HelperConnection("Tato fly from Skeleton house balcony", RegionName.OAKLAVILLE_SKELETON_BALCONY),
        HelperConnection("Tato fly from Graveyard", RegionName.OAKLAVILLE_GRAVEYARD,
                         HardLogic(True_())),
    ],
    RegionName.SEAGULLS: [
        HelperConnection("Seagulls from Stanhamn bus stop", RegionName.STANHAMN_BUS_STOP),
        HelperConnection("Seagulls from Hippo beach", RegionName.STANHAMN_HIPPO_BEACH),
        HelperConnection("Seagulls from Outside lighthouse", RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE),
        HelperConnection("Seagulls from Outside hydroplant (before honking)", RegionName.STANHAMN_OUTSIDE_HYDROPLANT,
                         HardLogic(True_())),
        HelperConnection("Seagulls from Pirate Drawbridge (if sandwich present)", RegionName.STANHAMN_PIRATE_DRAWBRIDGE,
                    HardLogic(Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.STANHAMN_OUTSIDE_HYDROPLANT))),
    ],
    RegionName.SUNDAY_SWAN: [
        HelperConnection("Sunday swan from Docks left", RegionName.STANHAMN_DOCKS_LEFT),
        HelperConnection("Sunday swan from Docks right", RegionName.STANHAMN_DOCKS_RIGHT),
    ],
    RegionName.FIA: [
        HelperConnection("Fia from Docks right", RegionName.STANHAMN_DOCKS_RIGHT),
        HelperConnection("Fia from Docks left", RegionName.STANHAMN_DOCKS_LEFT,
                         HardLogic(True_())),
    ],
    RegionName.FRAS: [
        HelperConnection("Fräs from Docks left", RegionName.STANHAMN_DOCKS_LEFT),
        HelperConnection("Fräs from Docks right", RegionName.STANHAMN_DOCKS_RIGHT,
                         HardLogic(True_())),
    ],
    RegionName.PIGEON: [
        HelperConnection("Pigeon from Clock tower", RegionName.LOGCITY_CLOCK_TOWER),
        HelperConnection("Pigeon from Outside cafe", RegionName.LOGCITY_OUTSIDE_CAFE),
        HelperConnection("Pigeon from Outside gallery", RegionName.LOGCITY_OUTSIDE_GALLERY),
        HelperConnection("Pigeon from Ratskullz alley", RegionName.LOGCITY_RATSKULLZ_ALLEY),
    ],
    RegionName.MOUSE: [
        HelperConnection("Mouse from Overpass", RegionName.LOGCITY_OVERPASS),
        HelperConnection("Mouse from Cafe (before honking)", RegionName.LOGCITY_CAFE,
                         HardLogic(True_())),
    ],
    RegionName.FLUFF: [
        HelperConnection("Fluff ball from Birthday party bottom", RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM),
        HelperConnection("Fluff ball from Birthday party top", RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP,
                         HardLogic(True_())),
    ],
    RegionName.HEDGEHOG: [
        HelperConnection("Hedgehog from Birthday party bottom", RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM),
        HelperConnection("Hedgehog from Birthday party top", RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP,
                         HardLogic(True_())),
    ],
    RegionName.METEOPAL: [
        HelperConnection("Meteopal from Snowman square bottom", RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM),
        HelperConnection("Meteopal from Snowman square top", RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
                         HardLogic(True_())),
    ],
    RegionName.GOAT_BIRTHDAY_PARTY: [
        HelperConnection("Goat from Birthday party bottom", RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM),
        HelperConnection("Goat from Birthday party top", RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP),
    ],
    RegionName.GOAT_CLIFFS: [
        HelperConnection("Goat from Cliffs top", RegionName.KIIRUBERG_CLIFFS_TOP),
        HelperConnection("Goat from Cliffs middle", RegionName.KIIRUBERG_CLIFFS_MIDDLE),
    ],
    RegionName.GOAT: [
        HelperConnection("Goat from Birthday party", RegionName.GOAT_BIRTHDAY_PARTY),
        HelperConnection("Goat from Ski mountain top", RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP),
        HelperConnection("Goat from Cliffs", RegionName.GOAT_CLIFFS),
    ],
    RegionName.OWL: [
        HelperConnection("Owl from Cliffs top", RegionName.KIIRUBERG_CLIFFS_TOP),
        HelperConnection("Owl from Cliffs middle", RegionName.KIIRUBERG_CLIFFS_MIDDLE,
                         HardLogic(True_())),
    ],
    RegionName.BAT: [
        HelperConnection("Bat from Cave", RegionName.BASTO_CAVE),
        HelperConnection("Bat from Bonfire top", RegionName.BASTO_BONFIRE_TOP),
        HelperConnection("Bat from Outside castle", RegionName.BASTO_OUTSIDE_CASTLE),
        HelperConnection("Bat from Bonfire bottom", RegionName.BASTO_BONFIRE_BOTTOM,
                         HardLogic(True_())),
    ],
    RegionName.BEAK_BIRD: [
        HelperConnection("Beak bird from Harbor bottom", RegionName.BASTO_BUS_STOP_BOTTOM),
        HelperConnection("Beak bird from Harbor top", RegionName.BASTO_BUS_STOP_TOP),
        HelperConnection("Beak bird from Lily pad pond left", RegionName.BASTO_LILY_PAD_POND_LEFT),
        HelperConnection("Beak bird from Lily pad pond right", RegionName.BASTO_LILY_PAD_POND_RIGHT),
    ],
    RegionName.BITLING_TATO: [
        HelperConnection("Bitling tato from Harbor bottom", RegionName.BASTO_BUS_STOP_BOTTOM),
        HelperConnection("Bitling tato from Harbor top", RegionName.BASTO_BUS_STOP_TOP),
    ],
    RegionName.DRILL_MOLE: [
        HelperConnection("Drill mole from Bonfire top", RegionName.BASTO_BONFIRE_TOP),
        HelperConnection("Drill mole from Bonfire bottom", RegionName.BASTO_BONFIRE_BOTTOM,
                         HardLogic(True_())),
    ],
    RegionName.NIGHT_LIZARD: [
        HelperConnection("Night lizard from Bonfire top", RegionName.BASTO_BONFIRE_TOP),
        HelperConnection("Night lizard from Bonfire bottom", RegionName.BASTO_BONFIRE_BOTTOM,
                         HardLogic(True_())),
    ],
    RegionName.WATER_STRIDER: [
        HelperConnection("Water strider from Lily pad pond left", RegionName.BASTO_LILY_PAD_POND_LEFT),
        HelperConnection("Water strider from Outside castle", RegionName.BASTO_OUTSIDE_CASTLE),
        HelperConnection("Water strider from Lily pad pond right", RegionName.BASTO_LILY_PAD_POND_RIGHT,
                         HardLogic(True_())),
    ],

    # Item connections
    RegionName.GHOST_GLASSES: [
        HelperConnection("Ghost glasses from Graveyard", RegionName.OAKLAVILLE_GRAVEYARD),
        HelperConnection("Ghost glasses from Skeleton house balcony", RegionName.OAKLAVILLE_SKELETON_BALCONY),
    ],

    # Achievement connections
    RegionName.GOOD_BOY: [
        HelperConnection("Pet Tom", RegionName.OAKLAVILLE_OUTSIDE_HOTEL),
        HelperConnection("Pet Oskar", RegionName.OAKLAVILLE_HOTEL),
        HelperConnection("Pet Sero", RegionName.OAKLAVILLE_GRAVEYARD),
        HelperConnection("Pet the Pet rock", RegionName.OAKLAVILLE_CAMP),
        HelperConnection("Pet Fia", RegionName.STANHAMN_DOCKS_RIGHT),
        HelperConnection("Pet Fräs", RegionName.STANHAMN_DOCKS_LEFT),
        HelperConnection("Pet Willemijn", RegionName.STANHAMN_KING_FISH_BEACH),
        HelperConnection("Pet Portillo", RegionName.LOGCITY_OUTSIDE_CAFE),
        HelperConnection("Pet Mikée or Nariko", RegionName.KIIRUBERG_BALLOON_HOUSE),
        HelperConnection("Pet Teddy", RegionName.KIIRUBERG_MECKS_HOUSE),
    ],
    RegionName.MAXIMUM_VACATION: [
        HelperConnection("Sit on a chair in Lily pad pond left", RegionName.BASTO_LILY_PAD_POND_LEFT),
        HelperConnection("Sit on a chair in Gym house", RegionName.BASTO_GYM_HOUSE),
        HelperConnection("Sit on a chair in Carnival", RegionName.BASTO_CARNIVAL),
        HelperConnection("Sit on a chair in Bonfire top", RegionName.BASTO_BONFIRE_TOP),
        HelperConnection("Sit on a chair in Ghost hangout", RegionName.BASTO_GHOST_HANGOUT),
    ],

    # Cassette connections
    RegionName.BIG_CITY_TAPE: [
        HelperConnection("Visit Logicity bus stop", RegionName.LOGCITY_BUS_STOP),
        HelperConnection("Visit Outside fasion show", RegionName.LOGCITY_OUTSIDE_FASHION_SHOW),
    ],
    RegionName.STORIES_OF_SNOW_TAPE: [
        HelperConnection("Visit Birthday party bottom", RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM),
        HelperConnection("Visit Birthday party top", RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP),
    ],
    RegionName.SONG_OF_THE_SEA: [
        HelperConnection("Visit Harbor bottom", RegionName.BASTO_BUS_STOP_BOTTOM),
        HelperConnection("Visit Harbor top", RegionName.BASTO_BUS_STOP_TOP,
                         HardLogic(True_())),
    ],
}
helper_connections: dict[str, Connection] = {
    helper_connection.name: Connection(helper_connection.dst_region_name, region, rule=helper_connection.rule)
    for region, connection_list in helper_region_data.items()
    for helper_connection in connection_list
}
# Super region connections
for area, region_list in area_lists.items():
    helper_connections.update({f"{region} in {area}": Connection(region, area) for region in region_list})

all_connections = region_connections | helper_connections

connection_name_to_id: dict[str, int] = {name: i for i, name in enumerate(region_connections, start=1)}


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

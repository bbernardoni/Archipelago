from dataclasses import dataclass
from typing import Tuple
from enum import IntEnum
from BaseClasses import Entrance, EntranceType, Region
from entrance_rando import ERPlacementState
from .regions import FullRegionName, RegionName, SubRegionName
from .items import ItemName
from .locations import LocationName

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
    BASTO_CASTLE = 8
    BASTO_DAY = 9
    BASTO_NIGHT = 10

within_region_groups: dict[ERGroups, list[ERGroups]] = {
    ERGroups.HOMELANDA: [ERGroups.HOMELANDA],
    ERGroups.OAKLAVILLE: [ERGroups.OAKLAVILLE],
    ERGroups.STANHAMN: [ERGroups.STANHAMN],
    ERGroups.LOGCITY: [ERGroups.LOGCITY],
    ERGroups.KIIRUBERG: [ERGroups.KIIRUBERG],
    ERGroups.MOUNTAIN_TOP: [ERGroups.MOUNTAIN_TOP],
    ERGroups.BASTO: [ERGroups.BASTO, ERGroups.BASTO_DAY, ERGroups.BASTO_NIGHT, ERGroups.BASTO_CASTLE],
    ERGroups.BASTO_CASTLE: [ERGroups.BASTO, ERGroups.BASTO_CASTLE],
    ERGroups.BASTO_DAY: [ERGroups.BASTO, ERGroups.BASTO_DAY],
    ERGroups.BASTO_NIGHT: [ERGroups.BASTO, ERGroups.BASTO_NIGHT],
}

@dataclass(frozen=True)
class Connection:
    dst_region_name: str
    name: str
    group: int
    requirements: Tuple[str] = ()

region_connections: dict[str, dict[str, list[Connection]]] = {
    RegionName.MENU: {
        SubRegionName.START_MENU: [
            Connection(FullRegionName.HOMELANDA_PLAYER_ROOM, "Start game", ERGroups.EXCLUDED),
        ],
        SubRegionName.BUS_MENU: [
            # requirements are handled as a special case
            Connection(FullRegionName.HOMELANDA_BUS_STOP, "Homelanda bus stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.OAKLAVILLE_BUS_STOP, "Oaklaville bus stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.STANHAMN_BUS_STOP, "Stanhamn bus stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.LOGCITY_BUS_STOP, "Logcity bus stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.KIIRUBERG_BUS_STOP, "Kiiruberg bus stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.MOUNTAIN_TOP_BUS_STOP, "Mountain top bus stop", ERGroups.EXCLUDED),
        ],
    },
    RegionName.HOMELANDA: {
        SubRegionName.HOMELANDA_PLAYER_ROOM: [
            Connection(FullRegionName.HOMELANDA_LIVING_ROOM, "Player room exit", ERGroups.HOMELANDA),
        ],
        SubRegionName.HOMELANDA_LIVING_ROOM: [
            Connection(FullRegionName.HOMELANDA_PLAYER_ROOM, "Player room entrance", ERGroups.HOMELANDA),
            Connection(FullRegionName.HOMELANDA_BUS_STOP, "Homelanda house exit", ERGroups.HOMELANDA),
        ],
        SubRegionName.HOMELANDA_BUS_STOP: [
            Connection(FullRegionName.HOMELANDA_LIVING_ROOM, "Homelanda house entrance", ERGroups.HOMELANDA),
            Connection(FullRegionName.BUS_MENU, "Homelanda bus pickup", ERGroups.EXCLUDED),
        ],
    },
    RegionName.OAKLAVILLE: {
        SubRegionName.OAKLAVILLE_BUS_STOP: [
            Connection(FullRegionName.BUS_MENU, "Oaklaville bus pickup", ERGroups.EXCLUDED),
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, "Oaklaville bus stop exit", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_OUTSIDE_HOTEL: [
            Connection(FullRegionName.OAKLAVILLE_BUS_STOP, "Outside hotel down", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_HOTEL, "Outside hotel left", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, "Outside hotel right", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_CAMP, "Hotel entrance", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_HOTEL: [
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, "Hotel exit", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, "Hotel elevator entrance", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_HOTEL_ELEVATOR: [
            Connection(FullRegionName.OAKLAVILLE_HOTEL, "Hotel elevator exit", ERGroups.OAKLAVILLE, (LocationName.QUEST_HOTEL_CHEF,)),
        ],
        SubRegionName.OAKLAVILLE_GHOST_CUP_GAME: [
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, "Ghost cup game right", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, "Mushroom house entrance", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, "Ghost cup game left", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_MUSHROOM_HOUSE: [
            Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, "Mushroom house exit", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_HIDE_AND_SEEK: [
            Connection(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, "Hide and seek right", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_GRAVEYARD, "Hide and seek left", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_GRAVEYARD: [
            Connection(FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, "Graveyard right", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE, "Skeleton house entrance", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_SKELETON_HOUSE: [
            Connection(FullRegionName.OAKLAVILLE_GRAVEYARD, "Skeleton house exit", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, "Skeleton house balcony exit", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY: [
            Connection(FullRegionName.OAKLAVILLE_SKELETON_HOUSE, "Skeleton house balcony entrance", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_CAMP: [
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, "Scout camp left", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_TRAIL, "Scout camp up", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_PLAYGROUND, "Scout camp right", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_TRAIL: [
            Connection(FullRegionName.OAKLAVILLE_CAMP, "Oaklaville trail down", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_LOOKOUT, "Oaklaville trail up", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_LOOKOUT: [
            Connection(FullRegionName.OAKLAVILLE_TRAIL, "Lookout exit", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_PLAYGROUND: [
            Connection(FullRegionName.OAKLAVILLE_CAMP, "Playground left", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE, "Playground right", ERGroups.OAKLAVILLE),
        ],
        SubRegionName.OAKLAVILLE_OUTSIDE_RAVE: [
            Connection(FullRegionName.OAKLAVILLE_PLAYGROUND, "Outside rave left", ERGroups.OAKLAVILLE),
            Connection(FullRegionName.OAKLAVILLE_RAVE, "Rave entrance", ERGroups.OAKLAVILLE, (ItemName.GHOST_GLASSES,)),
        ],
        SubRegionName.OAKLAVILLE_RAVE: [
            Connection(FullRegionName.OAKLAVILLE_OUTSIDE_RAVE, "Rave exit", ERGroups.OAKLAVILLE),
        ],
    },
    RegionName.STANHAMN: {
        SubRegionName.STANHAMN_BUS_STOP: [
            Connection(FullRegionName.BUS_MENU, "Stanhamn bus pickup", ERGroups.EXCLUDED),
            Connection(FullRegionName.STANHAMN_PHOTO_GUILD_HUT, "Photo guild hut entrance", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, "Bus stop left", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_DOCKS_LEFT, "Bus stop right", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, "Raft up", ERGroups.EXCLUDED, (ItemName.HONK_ATTACHMENT,)),
        ],
        SubRegionName.STANHAMN_PHOTO_GUILD_HUT: [
            Connection(FullRegionName.STANHAMN_BUS_STOP, "Photo guild hut exit", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_PIRATE_DRAWBRIDGE: [
            Connection(FullRegionName.STANHAMN_BUS_STOP, "Pirate Drawbridge right", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_HIPPO_BEACH, "Pirate Drawbridge left", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_HIPPO_BEACH: [
            Connection(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, "Hippo beach right", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_UNDERWATER, "Hippo beach manhole", ERGroups.EXCLUDED, (ItemName.HONK_ATTACHMENT, ItemName.DIVING_HELMET)),
            Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, "Hippo beach left", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_UNDERWATER: [
            Connection(FullRegionName.STANHAMN_HIPPO_BEACH, "Underwater exit", ERGroups.EXCLUDED),
        ],
        SubRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE: [
            Connection(FullRegionName.STANHAMN_HIPPO_BEACH, "Outside lighthouse right", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_KING_FISH_BEACH, "Outside lighthouse up", ERGroups.STANHAMN, (ItemName.HONK_ATTACHMENT,)),
            Connection(FullRegionName.STANHAMN_LIGHTHOUSE, "Lighthouse entrance", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_LIGHTHOUSE: [
            Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, "Lighthouse exit", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, "Lighthouse roof entrance", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_LIGHTHOUSE_ROOF: [
            Connection(FullRegionName.STANHAMN_LIGHTHOUSE, "Lighthouse roof exit", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_KING_FISH_BEACH: [
            Connection(FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, "King fish beach exit", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_DOCKS_LEFT: [
            Connection(FullRegionName.STANHAMN_BUS_STOP, "Docks left exit", ERGroups.STANHAMN),
            Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, "Viking express Stamhamn stop", ERGroups.EXCLUDED, (ItemName.BASTO_TICKET,)),
            Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, "Docks drawbridge from left", ERGroups.EXCLUDED, (LocationName.QUEST_POWER,)),
        ],
        SubRegionName.STANHAMN_DOCKS_RIGHT: [
            Connection(FullRegionName.STANHAMN_FISHING_TOWER, "Docks right exit", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_DOCKS_LEFT, "Docks drawbridge from right", ERGroups.EXCLUDED, (LocationName.QUEST_POWER,)),
        ],
        SubRegionName.STANHAMN_FISHING_TOWER: [
            Connection(FullRegionName.STANHAMN_DOCKS_RIGHT, "Fishing tower left", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, "Fishing tower up", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP: [
            Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, "Ghost drawbridge left", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, "Docks drawbridge from top", ERGroups.EXCLUDED, (LocationName.QUEST_POWER,)),
        ],
        SubRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM: [
            Connection(FullRegionName.STANHAMN_FISHING_TOWER, "Ghost drawbridge down", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, "Docks drawbridge from bottom", ERGroups.EXCLUDED, (LocationName.QUEST_POWER,)),
        ],
        SubRegionName.STANHAMN_OUTSIDE_HYDROPLANT: [
            Connection(FullRegionName.STANHAMN_BUS_STOP, "Raft down", ERGroups.EXCLUDED),
            Connection(FullRegionName.STANHAMN_HYDROPLANT, "Hydroplant entrance", ERGroups.STANHAMN),
            Connection(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, "Outside hydroplant right", ERGroups.STANHAMN),
        ],
        SubRegionName.STANHAMN_HYDROPLANT: [
            Connection(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, "Hydroplant exit", ERGroups.STANHAMN),
        ],
    },
    RegionName.LOGCITY: {
        SubRegionName.LOGCITY_BUS_STOP: [
            Connection(FullRegionName.BUS_MENU, "Logcity bus pickup", ERGroups.EXCLUDED),
            Connection(FullRegionName.LOGCITY_CLOCK_TOWER, "Escalator up", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_CLOCK_TOWER: [
            Connection(FullRegionName.LOGCITY_BUS_STOP, "Bus stop entrance", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_CROSSWALK, "Clock tower left", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, "Clock tower up", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, "Clock tower right", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_CROSSWALK: [
            Connection(FullRegionName.LOGCITY_CLOCK_TOWER, "Cross walk right", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OVERPASS, "Cross walk up", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_OVERPASS: [
            Connection(FullRegionName.LOGCITY_CROSSWALK, "Overpass down", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_NEWS_HOUSE, "News house entrance", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_SKATE_PARK, "Overpass up", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, "Overpass right", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_NEWS_HOUSE: [
            Connection(FullRegionName.LOGCITY_OVERPASS, "News house exit", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_SKATE_PARK: [
            Connection(FullRegionName.LOGCITY_OVERPASS, "Skate park down", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_RATSKULLZ_ALLEY, "Skate park right", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, "Skate park taxi", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_RATSKULLZ_ALLEY: [
            Connection(FullRegionName.LOGCITY_SKATE_PARK, "Ratskullz alley exit", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_OUTSIDE_FASHION_SHOW: [
            Connection(FullRegionName.LOGCITY_FASHION_SHOW, "Fashion show entrance", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_CLOCK_TOWER, "Outside fashion show down", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OVERPASS, "Outside fashion show left", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, "Outside fashion show right", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_FASHION_SHOW: [
            Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, "Fashion show exit", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, "Fashion show backstage entrance", ERGroups.LOGCITY, (ItemName.REPORTER_HAT,)),
        ],
        SubRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE: [
            Connection(FullRegionName.LOGCITY_FASHION_SHOW, "Fashion show backstage exit", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_OUTSIDE_CAFE: [
            Connection(FullRegionName.LOGCITY_CAFE, "Cafe entrance", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_CLOCK_TOWER, "Outside cafe left", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, "Outside cafe up", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_SKATE_PARK, "Outside cafe taxi", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_CAFE: [
            Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, "Cafe exit", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_OUTSIDE_GALLERY: [
            Connection(FullRegionName.LOGCITY_GALLERY, "Gallery entrance", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_CAFE, "Outside gallery show down", ERGroups.LOGCITY),
            Connection(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, "Outside gallery show left", ERGroups.LOGCITY),
        ],
        SubRegionName.LOGCITY_GALLERY: [
            Connection(FullRegionName.LOGCITY_OUTSIDE_GALLERY, "Gallery exit", ERGroups.LOGCITY),
        ],
    },
    RegionName.KIIRUBERG: {
        SubRegionName.KIIRUBERG_BUS_STOP: [
            Connection(FullRegionName.BUS_MENU, "Kiiruberg bus pickup", ERGroups.EXCLUDED),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, "Bus stop up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM: [
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, "Birthday party rope from bottom", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_BALLOON_HOUSE, "Balloon house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BUS_STOP, "Birthday party down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_FROZEN_POND, "Birthday party left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, "Birthday party right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP: [
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, "Birthday party rope from top", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, "Birthday party up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BALLOON_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, "Balloon house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_FROZEN_POND: [
            Connection(FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, "Old man's house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, "Frozen pond right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OLD_MANS_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_FROZEN_POND, "Old man's house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, "Snowman square rope from bottom", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_MILITARY_BASE, "Military base entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_MECKS_HOUSE, "Meck's house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, "Snowman square down", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, "Snowman square rope from top", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, "Snowman square left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, "Snowman square up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_MILITARY_BASE: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, "Military base exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_MECKS_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, "Meck's house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER: [
            Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, "Wizard tower entrance", ERGroups.KIIRUBERG, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, "Outside wizard tower right", ERGroups.KIIRUBERG, (ItemName.CLIMBING_BOOTS,)),
        ],
        SubRegionName.KIIRUBERG_WIZARD_TOWER: [
            Connection(FullRegionName.KIIRUBERG_COSMO_GARDEN, "Wizard portal entrance", ERGroups.KIIRUBERG, (LocationName.QUEST_ICE_WIZARD,)),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, "Wizard tower exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_COSMO_GARDEN: [
            Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, "Wizard portal exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_CLIFFS_BOTTOM: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, "Cliffs down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, "Cliffs bottom rope from bottom", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
        ],
        SubRegionName.KIIRUBERG_CLIFFS_MIDDLE: [
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, "Cliffs right", ERGroups.KIIRUBERG, (ItemName.HONK_ATTACHMENT,)),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, "Cliffs bottom rope from middle", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_TOP, "Cliffs top rope from middle", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
        ],
        SubRegionName.KIIRUBERG_CLIFFS_TOP: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, "Cliffs up", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, "Cliffs top rope from top", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT: [
            Connection(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, "Blizzard bridge left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, "Blizzard bridge rope from lower left", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)), # check warm clothes?
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, "Blizzard bridge break ice from bottom", ERGroups.EXCLUDED, (ItemName.HONK_ATTACHMENT,)),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT: [
            Connection(FullRegionName.KIIRUBERG_MAN_CAVE, "Man cave entrance", ERGroups.KIIRUBERG, (LocationName.QUEST_EXPERIENCE_TOEM,)), # not sure if best req, also check if ice reforms on exit
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, "Blizzard bridge rope from upper left", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, "Blizzard bridge break ice from top", ERGroups.EXCLUDED, (ItemName.HONK_ATTACHMENT,)),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT: [
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, "Blizzard bridge rope from lower right", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, "Blizzard bridge rope from upper right", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_MONSTER, "Blizzard bridge right", ERGroups.KIIRUBERG, (ItemName.HONK_ATTACHMENT,)),
        ],
        SubRegionName.KIIRUBERG_MAN_CAVE: [
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, "Man cave exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_MONSTER: [
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, "Blizzard monster exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP: [
            Connection(FullRegionName.KIIRUBERG_OBSERVATORY, "Observatory entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, "Outside observatory rope from top", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
        ],
        SubRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, "Outside observatory rope from bottom", ERGroups.EXCLUDED, (ItemName.CLIMBING_BOOTS,)),
            Connection(FullRegionName.KIIRUBERG_CLIFFS_TOP, "Outside observatory down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, "Outside observatory right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OBSERVATORY: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, "Observatory exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SKI_LIFT_BASE: [
            Connection(FullRegionName.KIIRUBERG_SKI_LODGE, "Ski lodge entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, "Ski lift base left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, "Ski lift up", ERGroups.EXCLUDED),
        ],
        SubRegionName.KIIRUBERG_SKI_LODGE: [
            Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, "Ski lodge exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, "Ski mountain top left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, "Ski lift down", ERGroups.EXCLUDED),
        ],
    },
    RegionName.MOUNTAIN_TOP: {
        SubRegionName.MOUNTAIN_TOP_BUS_STOP: [
            Connection(FullRegionName.BUS_MENU, "Mountain top bus pickup", ERGroups.EXCLUDED),
            Connection(FullRegionName.MOUNTAIN_TOP_TOEM, "Bus stop climb", ERGroups.MOUNTAIN_TOP),
        ],
        SubRegionName.MOUNTAIN_TOP_TOEM: [
            Connection(FullRegionName.MOUNTAIN_TOP_BUS_STOP, "Toem descend", ERGroups.MOUNTAIN_TOP),
        ],
    },
    RegionName.BASTO: {
        SubRegionName.BASTO_BUS_STOP_TOP_DAY: [
            Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, "Harbor gate from top day", ERGroups.EXCLUDED, (ItemName.WATERGUN,)),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, "Harbor up day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_BUS_STOP_TOP_NIGHT: [
            Connection(FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, "Harbor gate from top night", ERGroups.EXCLUDED, (ItemName.WATERGUN,)),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, "Harbor up night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_BUS_STOP_BOTTOM_DAY: [
            Connection(FullRegionName.BASTO_BUS_STOP_TOP_DAY, "Harbor gate from bottom day", ERGroups.EXCLUDED, (ItemName.WATERGUN,)),
            Connection(FullRegionName.STANHAMN_DOCKS_LEFT, "Viking express Basto stop day", ERGroups.EXCLUDED, (ItemName.BASTO_TICKET,)),
        ],
        SubRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT: [
            Connection(FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, "Harbor gate from bottom night", ERGroups.EXCLUDED, (ItemName.WATERGUN,)),
            Connection(FullRegionName.STANHAMN_DOCKS_LEFT, "Viking express Basto stop night", ERGroups.EXCLUDED, (ItemName.BASTO_TICKET,)),
        ],
        SubRegionName.BASTO_LILY_PAD_POND_LEFT_DAY: [
            Connection(FullRegionName.BASTO_BUS_STOP_TOP_DAY, "Lily pad pond down day", ERGroups.BASTO_DAY),
            Connection(FullRegionName.BASTO_CAMP_DAY, "Lily pad pond left day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT: [
            Connection(FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, "Lily pad pond down night", ERGroups.BASTO_NIGHT),
            Connection(FullRegionName.BASTO_CAMP_NIGHT, "Lily pad pond left night", ERGroups.BASTO_NIGHT),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, "Lily pad pond night bridge from left", ERGroups.EXCLUDED),
        ],
        SubRegionName.BASTO_LILY_PAD_POND_RIGHT: [
            Connection(FullRegionName.BASTO_GHOST_HANGOUT, "Lily pad pond right", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Lily pad pond up", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, "Lily pad pond night bridge from right", ERGroups.EXCLUDED),
        ],
        SubRegionName.BASTO_CAMP_DAY: [
            Connection(FullRegionName.BASTO_TENT, "Tent entrance day", ERGroups.BASTO_DAY),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, "Campsite right day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_CAMP_NIGHT: [
            Connection(FullRegionName.BASTO_TENT, "Tent entrance night", ERGroups.BASTO_NIGHT),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, "Campsite right night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_TENT: [
            Connection(FullRegionName.BASTO_CAMP_DAY, "Tent exit", ERGroups.BASTO), # night entrance handled as special case
        ],
        SubRegionName.BASTO_OUTSIDE_CASTLE: [
            Connection(FullRegionName.BASTO_CASTLE_DAY, "Castle entrance", ERGroups.BASTO_CASTLE),
            Connection(FullRegionName.BASTO_GYM_HOUSE, "Gym house entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, "Outside castle down", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_BONFIRE_TOP, "Outside castle left", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CASTLE_DAY: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Castle exit day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_CASTLE_NIGHT: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Castle exit night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_GYM_HOUSE: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Gym house exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_BONFIRE_TOP: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Bonfire lower right", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_JUNGLE, "Bonfire upper right", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_BONFIRE_BOTTOM_DAY, "Bonfire day bridge from top", ERGroups.EXCLUDED),
        ],
        SubRegionName.BASTO_BONFIRE_BOTTOM_DAY: [
            Connection(FullRegionName.BASTO_CARNIVAL_DAY, "Carnival entrance day", ERGroups.BASTO_DAY),
            Connection(FullRegionName.BASTO_BONFIRE_TOP, "Bonfire day bridge from bottom", ERGroups.EXCLUDED),
        ],
        SubRegionName.BASTO_BONFIRE_BOTTOM_NIGHT: [
            Connection(FullRegionName.BASTO_CARNIVAL_NIGHT, "Carnival entrance night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_CARNIVAL_DAY: [
            Connection(FullRegionName.BASTO_BONFIRE_BOTTOM_DAY, "Carnival exit day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_CARNIVAL_NIGHT: [
            Connection(FullRegionName.BASTO_BONFIRE_BOTTOM_NIGHT, "Carnival exit night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_GHOST_HANGOUT: [
            Connection(FullRegionName.BASTO_CAVE_DAY, "Ghost hangout cave entrance", ERGroups.BASTO), # night entrance handled as special case
            Connection(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, "Ghost hangout left", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CAVE_DAY: [
            Connection(FullRegionName.BASTO_SECRET_CAVE_DAY, "Secret cave room entrance day", ERGroups.BASTO_DAY, (ItemName.PICKAXE, ItemName.WATERGUN)),
            Connection(FullRegionName.BASTO_GHOST_HANGOUT, "Ghost hangout cave exit day", ERGroups.BASTO_DAY),
            Connection(FullRegionName.BASTO_JUNGLE, "Jungle cave exit day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_CAVE_NIGHT: [
            Connection(FullRegionName.BASTO_SECRET_CAVE_NIGHT, "Secret cave room entrance night", ERGroups.BASTO_NIGHT, (ItemName.PICKAXE, ItemName.WATERGUN)),
            Connection(FullRegionName.BASTO_GHOST_HANGOUT, "Ghost hangout cave exit night", ERGroups.BASTO_NIGHT),
            Connection(FullRegionName.BASTO_JUNGLE, "Jungle cave exit night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_SECRET_CAVE_DAY: [
            Connection(FullRegionName.BASTO_CAVE_DAY, "Secret cave room exit day", ERGroups.BASTO_DAY),
        ],
        SubRegionName.BASTO_SECRET_CAVE_NIGHT: [
            Connection(FullRegionName.BASTO_CAVE_NIGHT, "Secret cave room exit night", ERGroups.BASTO_NIGHT),
        ],
        SubRegionName.BASTO_JUNGLE: [
            Connection(FullRegionName.BASTO_CAVE_DAY, "Jungle cave entrance", ERGroups.BASTO), # night entrance handled as special case
            Connection(FullRegionName.BASTO_BONFIRE_TOP, "Jungle left", ERGroups.BASTO),
        ],
    },
}

def generate_entrance_pair(region: Region, name: str, group: int):
    exit = region.create_exit(name)
    exit.randomization_group = group
    exit.randomization_type = EntranceType.TWO_WAY
    er_target = region.create_er_target(name)
    er_target.randomization_group = group
    er_target.randomization_type = EntranceType.TWO_WAY
    return [exit, er_target]

def toem_on_connect(er_state: ERPlacementState, placed_exits: list[Entrance], paired_entrances: list[Entrance]) -> bool:
    def matching_entrance_name(name: str) -> str:
        if name.endswith(' day'):
            return name.replace(' day', ' night')
        else:
            return name.replace(' night', ' day')
        
    if placed_exits[0].randomization_group < ERGroups.BASTO:
        if paired_entrances[0].randomization_group <= ERGroups.BASTO_CASTLE:
            return False
        else:
            return False # TODO full game ER
    elif placed_exits[0].randomization_group <= ERGroups.BASTO_CASTLE:
        if paired_entrances[0].randomization_group <= ERGroups.BASTO_CASTLE:
            return False
        else:
            other_time_target_name = matching_entrance_name(paired_entrances[0].name)
            other_time_target = er_state.entrance_lookup.find_target(other_time_target_name)
            new_pair = generate_entrance_pair(placed_exits[0].parent_region, placed_exits[0].name + " other", placed_exits[0].randomization_group)
            er_state.entrance_lookup.add(new_pair[1])
            er_state.collection_state.blocked_connections[er_state.world.player].add(new_pair[0])
            er_state.connect(new_pair[0], other_time_target)
    else:
        if paired_entrances[0].randomization_group < ERGroups.BASTO:
            return False # TODO full game ER
        elif paired_entrances[0].randomization_group == ERGroups.BASTO:
            new_pair = generate_entrance_pair(paired_entrances[0].connected_region, paired_entrances[0].name + " other", paired_entrances[0].randomization_group)
            er_state.entrance_lookup.add(new_pair[1])
            er_state.collection_state.blocked_connections[er_state.world.player].add(new_pair[0])
            other_time_exit_name = matching_entrance_name(placed_exits[0].name)
            other_time_exit = er_state.world.multiworld.get_entrance(other_time_exit_name, er_state.world.player)
            er_state.connect(other_time_exit, new_pair[1])
        else:
            other_time_exit_name = matching_entrance_name(placed_exits[0].name)
            other_time_exit = er_state.world.multiworld.get_entrance(other_time_exit_name, er_state.world.player)
            other_time_target_name = matching_entrance_name(paired_entrances[0].name)
            other_time_target = er_state.entrance_lookup.find_target(other_time_target_name)
            er_state.connect(other_time_exit, other_time_target)
            
    return True

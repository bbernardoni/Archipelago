from dataclasses import dataclass
from typing import Tuple
from enum import IntEnum
from regions import FullRegionName, RegionName, SubRegionName
from items import ItemName
from locations import LocationName

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

@dataclass(frozen=True)
class Connection:
    dst_region_name: str
    connection_name: str
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
            Connection(FullRegionName.BASTO_BUS_STOP, "Viking express Stamhamn stop", ERGroups.EXCLUDED),
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
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY, "Bus stop up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BIRTHDAY_PARTY: [
            Connection(FullRegionName.KIIRUBERG_BALLOON_HOUSE, "Balloon house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BUS_STOP, "Birthday party down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_FROZEN_POND, "Birthday party left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE, "Birthday party up", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, "Birthday party right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BALLOON_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY, "Balloon house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_FROZEN_POND: [
            Connection(FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, "Old man's house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY, "Frozen pond right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OLD_MANS_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_FROZEN_POND, "Old man's house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SNOWMAN_SQUARE: [
            Connection(FullRegionName.KIIRUBERG_MILITARY_BASE, "Military base entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_MECKS_HOUSE, "Meck's house entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY, "Snowman square down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, "Snowman square left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_CLIFFS, "Snowman square up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_MILITARY_BASE: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE, "Military base exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_MECKS_HOUSE: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE, "Meck's house exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER: [
            Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, "Wizard tower entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE, "Outside wizard tower right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_WIZARD_TOWER: [
            Connection(FullRegionName.KIIRUBERG_COSMO_GARDEN, "Wizard portal entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, "Wizard tower exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_COSMO_GARDEN: [
            Connection(FullRegionName.KIIRUBERG_WIZARD_TOWER, "Wizard portal exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_CLIFFS: [
            Connection(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE, "Cliffs down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE, "Cliffs right", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY, "Cliffs up", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_BRIDGE: [
            Connection(FullRegionName.KIIRUBERG_CLIFFS, "Blizzard bridge left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_MONSTER, "Blizzard bridge right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_BLIZZARD_MONSTER: [
            Connection(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE, "Blizzard monster exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY: [
            Connection(FullRegionName.KIIRUBERG_OBSERVATORY, "Observatory entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_CLIFFS, "Outside observatory down", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, "Outside observatory right", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_OBSERVATORY: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY, "Observatory exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SKI_LIFT_BASE: [
            Connection(FullRegionName.KIIRUBERG_SKI_LODGE, "Ski lodge entrance", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY, "Ski lift base left", ERGroups.KIIRUBERG),
            Connection(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, "Ski lift up", ERGroups.EXCLUDED),
        ],
        SubRegionName.KIIRUBERG_SKI_LODGE: [
            Connection(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, "Ski lodge exit", ERGroups.KIIRUBERG),
        ],
        SubRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP: [
            Connection(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY, "Ski mountain top left", ERGroups.KIIRUBERG),
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
        SubRegionName.BASTO_BUS_STOP: [
            Connection(FullRegionName.STANHAMN_DOCKS_LEFT, "Viking express Basto stop", ERGroups.EXCLUDED),
            Connection(FullRegionName.BASTO_LILY_PAD_POND, "Harbour up", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_LILY_PAD_POND: [
            Connection(FullRegionName.BASTO_BUS_STOP, "Lily pad pond down", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_CAMP, "Lily pad pond left", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_GHOST_HANGOUT, "Lily pad pond right", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CAMP: [
            Connection(FullRegionName.BASTO_TENT, "Tent entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_LILY_PAD_POND, "Campsite right", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_TENT: [
            Connection(FullRegionName.BASTO_CAMP, "Tent exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_OUTSIDE_CASTLE: [
            Connection(FullRegionName.BASTO_CASTLE, "Castle entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_GYM_HOUSE, "Gym house entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_LILY_PAD_POND, "Outside castle down", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_BONFIRE, "Outside castle left", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CASTLE: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Castle exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_GYM_HOUSE: [
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Gym house exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_BONFIRE: [
            Connection(FullRegionName.BASTO_CARNIVAL, "Carnival entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_OUTSIDE_CASTLE, "Bonfire lower right", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_JUNGLE, "Bonfire upper right", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CARNIVAL: [
            Connection(FullRegionName.BASTO_BONFIRE, "Carnival exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_GHOST_HANGOUT: [
            Connection(FullRegionName.BASTO_CAVE, "Ghost hangout cave entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_LILY_PAD_POND, "Ghost hangout left", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_CAVE: [
            Connection(FullRegionName.BASTO_SECRET_CAVE, "Secret cave room entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_GHOST_HANGOUT, "Ghost hangout cave exit", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_JUNGLE, "Jungle cave exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_SECRET_CAVE: [
            Connection(FullRegionName.BASTO_CAVE, "Secret cave room exit", ERGroups.BASTO),
        ],
        SubRegionName.BASTO_JUNGLE: [
            Connection(FullRegionName.BASTO_CAVE, "Jungle cave entrance", ERGroups.BASTO),
            Connection(FullRegionName.BASTO_BONFIRE, "Jungle left", ERGroups.BASTO),
        ],
    },
}

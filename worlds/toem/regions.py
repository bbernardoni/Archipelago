from typing import final


@final
class Area:
    MENU = "Menu"
    HOMELANDA = "Homelanda"
    OAKLAVILLE = "Oaklaville"
    STANHAMN = "Stanhamn"
    LOGCITY = "Logcity"
    KIIRUBERG = "Kiiruberg"
    MOUNTAIN_TOP = "Mountain Top"
    BASTO = "Basto"

gameplay_areas = (
    Area.HOMELANDA, Area.OAKLAVILLE, Area.STANHAMN, Area.LOGCITY, Area.KIIRUBERG, Area.MOUNTAIN_TOP, Area.BASTO
)

@final
class RegionName:
    # Menu
    START_MENU = f"{Area.MENU} - Start menu"
    BUS_MENU = f"{Area.MENU} - Bus menu"

    # Homelanda
    HOMELANDA_PLAYER_ROOM = f"{Area.HOMELANDA} - Player room"
    HOMELANDA_LIVING_ROOM = f"{Area.HOMELANDA} - Living room"
    HOMELANDA_BUS_STOP = f"{Area.HOMELANDA} - Bus stop"

    # Oaklaville
    OAKLAVILLE_BUS_STOP = f"{Area.OAKLAVILLE} - Bus stop"
    OAKLAVILLE_OUTSIDE_HOTEL = f"{Area.OAKLAVILLE} - Outside hotel"
    OAKLAVILLE_HOTEL = f"{Area.OAKLAVILLE} - Hotel"
    OAKLAVILLE_HOTEL_ELEVATOR = f"{Area.OAKLAVILLE} - Hotel elevator"
    OAKLAVILLE_GHOST_CUP_GAME = f"{Area.OAKLAVILLE} - Ghost cup game"
    OAKLAVILLE_MUSHROOM_HOUSE = f"{Area.OAKLAVILLE} - Mushroom house"
    OAKLAVILLE_HIDE_AND_SEEK = f"{Area.OAKLAVILLE} - Hide and seek"
    OAKLAVILLE_GRAVEYARD = f"{Area.OAKLAVILLE} - Graveyard"
    OAKLAVILLE_SKELETON_HOUSE = f"{Area.OAKLAVILLE} - Skeleton house"
    OAKLAVILLE_SKELETON_BALCONY = f"{Area.OAKLAVILLE} - Skeleton house balcony"
    OAKLAVILLE_CAMP = f"{Area.OAKLAVILLE} - Camp"
    OAKLAVILLE_TRAIL_TOP = f"{Area.OAKLAVILLE} - Trail top"
    OAKLAVILLE_TRAIL_BOTTOM = f"{Area.OAKLAVILLE} - Trail bottom"
    OAKLAVILLE_LOOKOUT = f"{Area.OAKLAVILLE} - Lookout"
    OAKLAVILLE_PLAYGROUND = f"{Area.OAKLAVILLE} - Playground"
    OAKLAVILLE_OUTSIDE_RAVE_TOP = f"{Area.OAKLAVILLE} - Outside rave top"
    OAKLAVILLE_OUTSIDE_RAVE_BOTTOM = f"{Area.OAKLAVILLE} - Outside rave bottom"
    OAKLAVILLE_RAVE = f"{Area.OAKLAVILLE} - Rave"

    # Stanhamn
    STANHAMN_BUS_STOP = f"{Area.STANHAMN} - Bus stop"
    STANHAMN_PHOTO_GUILD_HUT = f"{Area.STANHAMN} - Photo guild hut"
    STANHAMN_PIRATE_DRAWBRIDGE = f"{Area.STANHAMN} - Pirate Drawbridge"
    STANHAMN_HIPPO_BEACH = f"{Area.STANHAMN} - Hippo beach"
    STANHAMN_UNDERWATER = f"{Area.STANHAMN} - Underwater"
    STANHAMN_OUTSIDE_LIGHTHOUSE = f"{Area.STANHAMN} - Outside lighthouse"
    STANHAMN_LIGHTHOUSE = f"{Area.STANHAMN} - Lighthouse"
    STANHAMN_LIGHTHOUSE_ROOF = f"{Area.STANHAMN} - Lighthouse roof"
    STANHAMN_KING_FISH_BEACH = f"{Area.STANHAMN} - King fish beach"
    STANHAMN_DOCKS_LEFT = f"{Area.STANHAMN} - Docks left"
    STANHAMN_DOCKS_RIGHT = f"{Area.STANHAMN} - Docks right"
    STANHAMN_FISHING_TOWER = f"{Area.STANHAMN} - Fishing tower"
    STANHAMN_GHOST_DRAWBRIDGE_TOP = f"{Area.STANHAMN} - Ghost drawbridge top"
    STANHAMN_GHOST_DRAWBRIDGE_BOTTOM = f"{Area.STANHAMN} - Ghost drawbridge bottom"
    STANHAMN_OUTSIDE_HYDROPLANT = f"{Area.STANHAMN} - Outside hydroplant"
    STANHAMN_HYDROPLANT = f"{Area.STANHAMN} - Hydroplant"

    # Logcity
    LOGCITY_BUS_STOP = f"{Area.LOGCITY} - Bus stop"
    LOGCITY_CLOCK_TOWER = f"{Area.LOGCITY} - Clock tower"
    LOGCITY_CROSSWALK = f"{Area.LOGCITY} - Cross walk"
    LOGCITY_OVERPASS = f"{Area.LOGCITY} - Overpass"
    LOGCITY_NEWS_HOUSE = f"{Area.LOGCITY} - News house"
    LOGCITY_SKATE_PARK = f"{Area.LOGCITY} - Skate park"
    LOGCITY_RATSKULLZ_ALLEY = f"{Area.LOGCITY} - Ratskullz alley"
    LOGCITY_OUTSIDE_FASHION_SHOW = f"{Area.LOGCITY} - Outside fashion show"
    LOGCITY_FASHION_SHOW_TOP = f"{Area.LOGCITY} - Fashion show top"
    LOGCITY_FASHION_SHOW_BOTTOM = f"{Area.LOGCITY} - Fashion show bottom"
    LOGCITY_FASHION_SHOW_BACKSTAGE = f"{Area.LOGCITY} - Fashion show backstage"
    LOGCITY_OUTSIDE_CAFE = f"{Area.LOGCITY} - Outside cafe"
    LOGCITY_CAFE = f"{Area.LOGCITY} - Cafe"
    LOGCITY_OUTSIDE_GALLERY = f"{Area.LOGCITY} - Outside gallery"
    LOGCITY_GALLERY = f"{Area.LOGCITY} - Gallery"

    # Kiiruberg
    KIIRUBERG_BUS_STOP = f"{Area.KIIRUBERG} - Bus stop"
    KIIRUBERG_BIRTHDAY_PARTY_BOTTOM = f"{Area.KIIRUBERG} - Birthday party bottom"
    KIIRUBERG_BIRTHDAY_PARTY_TOP = f"{Area.KIIRUBERG} - Birthday party top"
    KIIRUBERG_BALLOON_HOUSE = f"{Area.KIIRUBERG} - Balloon house"
    KIIRUBERG_FROZEN_POND = f"{Area.KIIRUBERG} - Frozen pond"
    KIIRUBERG_OLD_MANS_HOUSE = f"{Area.KIIRUBERG} - Old man's house"
    KIIRUBERG_SNOWMAN_SQUARE_BOTTOM = f"{Area.KIIRUBERG} - Snowman square bottom"
    KIIRUBERG_SNOWMAN_SQUARE_TOP = f"{Area.KIIRUBERG} - Snowman square top"
    KIIRUBERG_MILITARY_BASE = f"{Area.KIIRUBERG} - Military base"
    KIIRUBERG_MECKS_HOUSE = f"{Area.KIIRUBERG} - Meck's house"
    KIIRUBERG_OUTSIDE_WIZARD_TOWER = f"{Area.KIIRUBERG} - Outside wizard tower"
    KIIRUBERG_WIZARD_TOWER = f"{Area.KIIRUBERG} - Wizard tower"
    KIIRUBERG_COSMO_GARDEN = f"{Area.KIIRUBERG} - Cosmo Garden"
    KIIRUBERG_CLIFFS_BOTTOM = f"{Area.KIIRUBERG} - Cliffs bottom"
    KIIRUBERG_CLIFFS_MIDDLE = f"{Area.KIIRUBERG} - Cliffs middle"
    KIIRUBERG_CLIFFS_TOP = f"{Area.KIIRUBERG} - Cliffs top"
    KIIRUBERG_BLIZZARD_BRIDGE_DL = f"{Area.KIIRUBERG} - Blizzard bridge lower left"
    KIIRUBERG_BLIZZARD_BRIDGE_UL = f"{Area.KIIRUBERG} - Blizzard bridge upper left"
    KIIRUBERG_BLIZZARD_BRIDGE_RIGHT = f"{Area.KIIRUBERG} - Blizzard bridge right"
    KIIRUBERG_MAN_CAVE = f"{Area.KIIRUBERG} - Man cave"
    KIIRUBERG_BLIZZARD_MONSTER = f"{Area.KIIRUBERG} - Blizzard monster"
    KIIRUBERG_OUTSIDE_OBSERV_TOP = f"{Area.KIIRUBERG} - Outside observatory top"
    KIIRUBERG_OUTSIDE_OBSERV_BOTTOM = f"{Area.KIIRUBERG} - Outside observatory bottom"
    KIIRUBERG_OBSERVATORY = f"{Area.KIIRUBERG} - Observatory"
    KIIRUBERG_SKI_LIFT_BASE = f"{Area.KIIRUBERG} - Ski lift base"
    KIIRUBERG_SKI_LODGE = f"{Area.KIIRUBERG} - Ski lodge"
    KIIRUBERG_SKI_MOUNTAIN_TOP = f"{Area.KIIRUBERG} - Ski mountain top"

    # Mountain Top
    MOUNTAIN_TOP_BUS_STOP = f"{Area.MOUNTAIN_TOP} - Bus stop"
    MOUNTAIN_TOP_TOEM = f"{Area.MOUNTAIN_TOP} - Toem"

    # Basto
    BASTO_BUS_STOP_TOP = f"{Area.BASTO} - Harbor top"
    BASTO_BUS_STOP_BOTTOM = f"{Area.BASTO} - Harbor bottom"
    BASTO_LILY_PAD_POND_LEFT = f"{Area.BASTO} - Lily pad pond left"
    BASTO_LILY_PAD_POND_RIGHT = f"{Area.BASTO} - Lily pad pond right"
    BASTO_CAMP = f"{Area.BASTO} - Campsite"
    BASTO_TENT = f"{Area.BASTO} - Tent"
    BASTO_OUTSIDE_CASTLE = f"{Area.BASTO} - Outside castle"
    BASTO_CASTLE = f"{Area.BASTO} - Castle"
    BASTO_GYM_HOUSE = f"{Area.BASTO} - Gym house"
    BASTO_BONFIRE_TOP = f"{Area.BASTO} - Bonfire top"
    BASTO_BONFIRE_BOTTOM = f"{Area.BASTO} - Bonfire bottom"
    BASTO_CARNIVAL = f"{Area.BASTO} - Carnival"
    BASTO_GHOST_HANGOUT = f"{Area.BASTO} - Ghost hangout"
    BASTO_CAVE = f"{Area.BASTO} - Cave"
    BASTO_SECRET_CAVE = f"{Area.BASTO} - Secret cave room"
    BASTO_JUNGLE = f"{Area.BASTO} - Jungle"

    # Helper regions
    # Super regions
    OAKLAVILLE = Area.OAKLAVILLE
    STANHAMN = Area.STANHAMN
    LOGCITY = Area.LOGCITY
    KIIRUBERG = Area.KIIRUBERG
    MOUNTAIN_TOP = Area.MOUNTAIN_TOP
    BASTO = Area.BASTO
    # Question regions
    FASHION_SHOW = f"{Area.LOGCITY} - Fashion show"
    BALLOON_ANIMAL = f"{Area.KIIRUBERG} - Balloon animal"
    ASTEROID = f"{Area.KIIRUBERG} - Asteroid"
    # Compendium regions
    SQUIRRELS = f"{Area.OAKLAVILLE} - Squirrels"
    SERO = f"{Area.OAKLAVILLE} - Sero"
    TATO_FLY = f"{Area.OAKLAVILLE} - Tato fly"
    SEAGULLS = f"{Area.STANHAMN} - Seagulls"
    SUNDAY_SWAN = f"{Area.STANHAMN} - Sunday Swan"
    FIA = f"{Area.STANHAMN} - Fia"
    FRAS = f"{Area.STANHAMN} - Fräs"
    PIGEON = f"{Area.LOGCITY} - Pigeon"
    MOUSE = f"{Area.LOGCITY} - Mouse"
    FLUFF = f"{Area.KIIRUBERG} - Fluff ball"
    HEDGEHOG = f"{Area.KIIRUBERG} - Hedgehog"
    METEOPAL = f"{Area.KIIRUBERG} - Meteopal"
    GOAT_BIRTHDAY_PARTY = f"{Area.KIIRUBERG} - Goat (Birthday party)"
    GOAT_CLIFFS = f"{Area.KIIRUBERG} - Goat (Cliffs)"
    GOAT = f"{Area.KIIRUBERG} - Goat"
    OWL = f"{Area.KIIRUBERG} - Owl"
    BAT = f"{Area.BASTO} - Bat"
    BEAK_BIRD = f"{Area.BASTO} - Beak Bird"
    BITLING_TATO = f"{Area.BASTO} - Bitling Tato"
    WATER_STRIDER = f"{Area.BASTO} - Water Strider"
    # Item regions
    GHOST_GLASSES = f"{Area.OAKLAVILLE} - Ghost glasses"
    # Achievement regions
    GOOD_BOY = "Pet a pet"
    MAXIMUM_VACATION = f"{Area.BASTO} - Maximum Vacation"
    # Cassette regions
    BIG_CITY_TAPE = f"{Area.LOGCITY} - Big City cassette"
    STORIES_OF_SNOW_TAPE = f"{Area.KIIRUBERG} - Stories of snow cassette"

oaklaville_regions = (
    RegionName.OAKLAVILLE_BUS_STOP, RegionName.OAKLAVILLE_OUTSIDE_HOTEL, RegionName.OAKLAVILLE_HOTEL,
    RegionName.OAKLAVILLE_HOTEL_ELEVATOR, RegionName.OAKLAVILLE_GHOST_CUP_GAME,
    RegionName.OAKLAVILLE_MUSHROOM_HOUSE, RegionName.OAKLAVILLE_HIDE_AND_SEEK,
    RegionName.OAKLAVILLE_GRAVEYARD, RegionName.OAKLAVILLE_SKELETON_HOUSE,
    RegionName.OAKLAVILLE_SKELETON_BALCONY, RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_TRAIL_TOP,
    RegionName.OAKLAVILLE_TRAIL_BOTTOM, RegionName.OAKLAVILLE_LOOKOUT, RegionName.OAKLAVILLE_PLAYGROUND,
    RegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, RegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM,
    RegionName.OAKLAVILLE_RAVE
)
stanhamn_regions = (
    RegionName.STANHAMN_BUS_STOP, RegionName.STANHAMN_PHOTO_GUILD_HUT,
    RegionName.STANHAMN_PIRATE_DRAWBRIDGE, RegionName.STANHAMN_HIPPO_BEACH, RegionName.STANHAMN_UNDERWATER,
    RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE,
    RegionName.STANHAMN_LIGHTHOUSE_ROOF, RegionName.STANHAMN_KING_FISH_BEACH,
    RegionName.STANHAMN_DOCKS_LEFT, RegionName.STANHAMN_DOCKS_RIGHT, RegionName.STANHAMN_FISHING_TOWER,
    RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM,
    RegionName.STANHAMN_OUTSIDE_HYDROPLANT, RegionName.STANHAMN_HYDROPLANT
)
logcity_regions = (
    RegionName.LOGCITY_BUS_STOP, RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_CROSSWALK,
    RegionName.LOGCITY_OVERPASS, RegionName.LOGCITY_NEWS_HOUSE, RegionName.LOGCITY_SKATE_PARK,
    RegionName.LOGCITY_RATSKULLZ_ALLEY, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
    RegionName.LOGCITY_FASHION_SHOW_TOP, RegionName.LOGCITY_FASHION_SHOW_BOTTOM,
    RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_CAFE,
    RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_GALLERY
)
kiiruberg_regions = (
    RegionName.KIIRUBERG_BUS_STOP, RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM,
    RegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, RegionName.KIIRUBERG_BALLOON_HOUSE,
    RegionName.KIIRUBERG_FROZEN_POND, RegionName.KIIRUBERG_OLD_MANS_HOUSE,
    RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP,
    RegionName.KIIRUBERG_MILITARY_BASE, RegionName.KIIRUBERG_MECKS_HOUSE,
    RegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, RegionName.KIIRUBERG_WIZARD_TOWER,
    RegionName.KIIRUBERG_COSMO_GARDEN, RegionName.KIIRUBERG_CLIFFS_BOTTOM,
    RegionName.KIIRUBERG_CLIFFS_MIDDLE, RegionName.KIIRUBERG_CLIFFS_TOP,
    RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, RegionName.KIIRUBERG_BLIZZARD_BRIDGE_UL,
    RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.KIIRUBERG_MAN_CAVE,
    RegionName.KIIRUBERG_BLIZZARD_MONSTER, RegionName.KIIRUBERG_OUTSIDE_OBSERV_TOP,
    RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, RegionName.KIIRUBERG_OBSERVATORY,
    RegionName.KIIRUBERG_SKI_LIFT_BASE, RegionName.KIIRUBERG_SKI_LODGE,
    RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP
)
mountain_top_regions = (RegionName.MOUNTAIN_TOP_BUS_STOP, RegionName.MOUNTAIN_TOP_TOEM)
basto_regions = (
    RegionName.BASTO_BUS_STOP_TOP, RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BASTO_LILY_PAD_POND_LEFT,
    RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_CAMP, RegionName.BASTO_TENT,
    RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_CASTLE, RegionName.BASTO_GYM_HOUSE,
    RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_BONFIRE_BOTTOM, RegionName.BASTO_CARNIVAL,
    RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_CAVE, RegionName.BASTO_SECRET_CAVE,
    RegionName.BASTO_JUNGLE
)

area_lists = {
    Area.OAKLAVILLE: oaklaville_regions,
    Area.STANHAMN: stanhamn_regions,
    Area.LOGCITY: logcity_regions,
    Area.KIIRUBERG: kiiruberg_regions,
    Area.MOUNTAIN_TOP: mountain_top_regions,
    Area.BASTO: basto_regions,
}

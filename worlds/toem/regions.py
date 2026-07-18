from typing import final

@final
class RegionName:
    MENU = "Menu"
    HOMELANDA = "Homelanda"
    OAKLAVILLE = "Oaklaville"
    STANHAMN = "Stanhamn"
    LOGCITY = "Logcity"
    KIIRUBERG = "Kiiruberg"
    MOUNTAIN_TOP = "Mountain Top"
    BASTO = "Basto"

@final
class FullRegionName:
    # Menu
    START_MENU = f"{RegionName.MENU} - Start menu"
    BUS_MENU = f"{RegionName.MENU} - Bus menu"

    # Homelanda
    HOMELANDA_PLAYER_ROOM = f"{RegionName.HOMELANDA} - Player room"
    HOMELANDA_LIVING_ROOM = f"{RegionName.HOMELANDA} - Living room"
    HOMELANDA_BUS_STOP = f"{RegionName.HOMELANDA} - Bus stop"

    # Oaklaville
    OAKLAVILLE_BUS_STOP = f"{RegionName.OAKLAVILLE} - Bus stop"
    OAKLAVILLE_OUTSIDE_HOTEL = f"{RegionName.OAKLAVILLE} - Outside hotel"
    OAKLAVILLE_HOTEL = f"{RegionName.OAKLAVILLE} - Hotel"
    OAKLAVILLE_HOTEL_ELEVATOR = f"{RegionName.OAKLAVILLE} - Hotel elevator"
    OAKLAVILLE_GHOST_CUP_GAME = f"{RegionName.OAKLAVILLE} - Ghost cup game"
    OAKLAVILLE_MUSHROOM_HOUSE = f"{RegionName.OAKLAVILLE} - Mushroom house"
    OAKLAVILLE_HIDE_AND_SEEK = f"{RegionName.OAKLAVILLE} - Hide and seek"
    OAKLAVILLE_GRAVEYARD = f"{RegionName.OAKLAVILLE} - Graveyard"
    OAKLAVILLE_SKELETON_HOUSE = f"{RegionName.OAKLAVILLE} - Skeleton house"
    OAKLAVILLE_SKELETON_HOUSE_BALCONY = f"{RegionName.OAKLAVILLE} - Skeleton house balcony"
    OAKLAVILLE_CAMP = f"{RegionName.OAKLAVILLE} - Camp"
    OAKLAVILLE_TRAIL_TOP = f"{RegionName.OAKLAVILLE} - Trail top"
    OAKLAVILLE_TRAIL_BOTTOM = f"{RegionName.OAKLAVILLE} - Trail bottom"
    OAKLAVILLE_LOOKOUT = f"{RegionName.OAKLAVILLE} - Lookout"
    OAKLAVILLE_PLAYGROUND = f"{RegionName.OAKLAVILLE} - Playground"
    OAKLAVILLE_OUTSIDE_RAVE_TOP = f"{RegionName.OAKLAVILLE} - Outside rave top"
    OAKLAVILLE_OUTSIDE_RAVE_BOTTOM = f"{RegionName.OAKLAVILLE} - Outside rave bottom"
    OAKLAVILLE_RAVE = f"{RegionName.OAKLAVILLE} - Rave"

    # Stanhamn
    STANHAMN_BUS_STOP = f"{RegionName.STANHAMN} - Bus stop"
    STANHAMN_PHOTO_GUILD_HUT = f"{RegionName.STANHAMN} - Photo guild hut"
    STANHAMN_PIRATE_DRAWBRIDGE = f"{RegionName.STANHAMN} - Pirate Drawbridge"
    STANHAMN_HIPPO_BEACH = f"{RegionName.STANHAMN} - Hippo beach"
    STANHAMN_UNDERWATER = f"{RegionName.STANHAMN} - Underwater"
    STANHAMN_OUTSIDE_LIGHTHOUSE = f"{RegionName.STANHAMN} - Outside lighthouse"
    STANHAMN_LIGHTHOUSE = f"{RegionName.STANHAMN} - Lighthouse"
    STANHAMN_LIGHTHOUSE_ROOF = f"{RegionName.STANHAMN} - Lighthouse roof"
    STANHAMN_KING_FISH_BEACH = f"{RegionName.STANHAMN} - King fish beach"
    STANHAMN_DOCKS_LEFT = f"{RegionName.STANHAMN} - Docks left"
    STANHAMN_DOCKS_RIGHT = f"{RegionName.STANHAMN} - Docks right"
    STANHAMN_FISHING_TOWER = f"{RegionName.STANHAMN} - Fishing tower"
    STANHAMN_GHOST_DRAWBRIDGE_TOP = f"{RegionName.STANHAMN} - Ghost drawbridge top"
    STANHAMN_GHOST_DRAWBRIDGE_BOTTOM = f"{RegionName.STANHAMN} - Ghost drawbridge bottom"
    STANHAMN_OUTSIDE_HYDROPLANT = f"{RegionName.STANHAMN} - Outside hydroplant"
    STANHAMN_HYDROPLANT = f"{RegionName.STANHAMN} - Hydroplant"

    # Logcity
    LOGCITY_BUS_STOP = f"{RegionName.LOGCITY} - Bus stop"
    LOGCITY_CLOCK_TOWER = f"{RegionName.LOGCITY} - Clock tower"
    LOGCITY_CROSSWALK = f"{RegionName.LOGCITY} - Cross walk"
    LOGCITY_OVERPASS = f"{RegionName.LOGCITY} - Overpass"
    LOGCITY_NEWS_HOUSE = f"{RegionName.LOGCITY} - News house"
    LOGCITY_SKATE_PARK = f"{RegionName.LOGCITY} - Skate park"
    LOGCITY_RATSKULLZ_ALLEY = f"{RegionName.LOGCITY} - Ratskullz alley"
    LOGCITY_OUTSIDE_FASHION_SHOW = f"{RegionName.LOGCITY} - Outside fashion show"
    LOGCITY_FASHION_SHOW_TOP = f"{RegionName.LOGCITY} - Fashion show top"
    LOGCITY_FASHION_SHOW_BOTTOM = f"{RegionName.LOGCITY} - Fashion show bottom"
    LOGCITY_FASHION_SHOW_BACKSTAGE = f"{RegionName.LOGCITY} - Fashion show backstage"
    LOGCITY_OUTSIDE_CAFE = f"{RegionName.LOGCITY} - Outside cafe"
    LOGCITY_CAFE = f"{RegionName.LOGCITY} - Cafe"
    LOGCITY_OUTSIDE_GALLERY = f"{RegionName.LOGCITY} - Outside gallery"
    LOGCITY_GALLERY = f"{RegionName.LOGCITY} - Gallery"

    # Kiiruberg
    KIIRUBERG_BUS_STOP = f"{RegionName.KIIRUBERG} - Bus stop"
    KIIRUBERG_BIRTHDAY_PARTY_BOTTOM = f"{RegionName.KIIRUBERG} - Birthday party bottom"
    KIIRUBERG_BIRTHDAY_PARTY_TOP = f"{RegionName.KIIRUBERG} - Birthday party top"
    KIIRUBERG_BALLOON_HOUSE = f"{RegionName.KIIRUBERG} - Balloon house"
    KIIRUBERG_FROZEN_POND = f"{RegionName.KIIRUBERG} - Frozen pond"
    KIIRUBERG_OLD_MANS_HOUSE = f"{RegionName.KIIRUBERG} - Old man's house"
    KIIRUBERG_SNOWMAN_SQUARE_BOTTOM = f"{RegionName.KIIRUBERG} - Snowman square bottom"
    KIIRUBERG_SNOWMAN_SQUARE_TOP = f"{RegionName.KIIRUBERG} - Snowman square top"
    KIIRUBERG_MILITARY_BASE = f"{RegionName.KIIRUBERG} - Military base"
    KIIRUBERG_MECKS_HOUSE = f"{RegionName.KIIRUBERG} - Meck's house"
    KIIRUBERG_OUTSIDE_WIZARD_TOWER = f"{RegionName.KIIRUBERG} - Outside wizard tower"
    KIIRUBERG_WIZARD_TOWER = f"{RegionName.KIIRUBERG} - Wizard tower"
    KIIRUBERG_COSMO_GARDEN = f"{RegionName.KIIRUBERG} - Cosmo Garden"
    KIIRUBERG_CLIFFS_BOTTOM = f"{RegionName.KIIRUBERG} - Cliffs bottom"
    KIIRUBERG_CLIFFS_MIDDLE = f"{RegionName.KIIRUBERG} - Cliffs middle"
    KIIRUBERG_CLIFFS_TOP = f"{RegionName.KIIRUBERG} - Cliffs top"
    KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT = f"{RegionName.KIIRUBERG} - Blizzard bridge lower left"
    KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT = f"{RegionName.KIIRUBERG} - Blizzard bridge upper left"
    KIIRUBERG_BLIZZARD_BRIDGE_RIGHT = f"{RegionName.KIIRUBERG} - Blizzard bridge right"
    KIIRUBERG_MAN_CAVE = f"{RegionName.KIIRUBERG} - Man cave"
    KIIRUBERG_BLIZZARD_MONSTER = f"{RegionName.KIIRUBERG} - Blizzard monster"
    KIIRUBERG_OUTSIDE_OBSERVATORY_TOP = f"{RegionName.KIIRUBERG} - Outside observatory top"
    KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM = f"{RegionName.KIIRUBERG} - Outside observatory bottom"
    KIIRUBERG_OBSERVATORY = f"{RegionName.KIIRUBERG} - Observatory"
    KIIRUBERG_SKI_LIFT_BASE = f"{RegionName.KIIRUBERG} - Ski lift base"
    KIIRUBERG_SKI_LODGE = f"{RegionName.KIIRUBERG} - Ski lodge"
    KIIRUBERG_SKI_MOUNTAIN_TOP = f"{RegionName.KIIRUBERG} - Ski mountain top"

    # Mountain Top
    MOUNTAIN_TOP_BUS_STOP = f"{RegionName.MOUNTAIN_TOP} - Bus stop"
    MOUNTAIN_TOP_TOEM = f"{RegionName.MOUNTAIN_TOP} - Toem"

    # Basto
    BASTO_BUS_STOP_TOP = f"{RegionName.BASTO} - Harbor top"
    BASTO_BUS_STOP_BOTTOM = f"{RegionName.BASTO} - Harbor bottom"
    BASTO_LILY_PAD_POND_LEFT = f"{RegionName.BASTO} - Lily pad pond left"
    BASTO_LILY_PAD_POND_RIGHT = f"{RegionName.BASTO} - Lily pad pond right"
    BASTO_CAMP = f"{RegionName.BASTO} - Campsite"
    BASTO_TENT = f"{RegionName.BASTO} - Tent"
    BASTO_OUTSIDE_CASTLE = f"{RegionName.BASTO} - Outside castle"
    BASTO_CASTLE = f"{RegionName.BASTO} - Castle"
    BASTO_GYM_HOUSE = f"{RegionName.BASTO} - Gym house"
    BASTO_BONFIRE_TOP = f"{RegionName.BASTO} - Bonfire top"
    BASTO_BONFIRE_BOTTOM = f"{RegionName.BASTO} - Bonfire bottom"
    BASTO_CARNIVAL = f"{RegionName.BASTO} - Carnival"
    BASTO_GHOST_HANGOUT = f"{RegionName.BASTO} - Ghost hangout"
    BASTO_CAVE = f"{RegionName.BASTO} - Cave"
    BASTO_SECRET_CAVE = f"{RegionName.BASTO} - Secret cave room"
    BASTO_JUNGLE = f"{RegionName.BASTO} - Jungle"

    # Helper regions
    # Super regions
    OAKLAVILLE = RegionName.OAKLAVILLE
    STANHAMN = RegionName.STANHAMN
    LOGCITY = RegionName.LOGCITY
    KIIRUBERG = RegionName.KIIRUBERG
    MOUNTAIN_TOP = RegionName.MOUNTAIN_TOP
    BASTO = RegionName.BASTO
    # Compendium regions
    SQUIRRELS = "Squirrels"
    SEAGULLS = "Seagulls"
    SUNDAY_SWAN = "Sunday Swan"
    PIGEON = "Pigeon"
    GOAT = "Goat"
    BAT = f"{RegionName.BASTO} - Bat"
    BEAK_BIRD = f"{RegionName.BASTO} - Beak Bird"
    BITLING_TATO = f"{RegionName.BASTO} - Bitling Tato"
    WATER_STRIDER = f"{RegionName.BASTO} - Water Strider"
    # Achievement regions
    GOOD_BOY = "Pet a pet"
    MAXIMUM_VACATION = f"{RegionName.BASTO} - Maximum Vacation"
    # Cassette regions
    BIG_CITY_TAPE = "Big City cassette"
    STORIES_OF_SNOW_TAPE = "Stories of snow cassette"

oaklaville_regions = (
    FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_HOTEL, 
    FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, 
    FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, FullRegionName.OAKLAVILLE_GRAVEYARD, FullRegionName.OAKLAVILLE_SKELETON_HOUSE, 
    FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_TRAIL_TOP,
    FullRegionName.OAKLAVILLE_TRAIL_BOTTOM, FullRegionName.OAKLAVILLE_LOOKOUT, FullRegionName.OAKLAVILLE_PLAYGROUND,
    FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_TOP, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE_BOTTOM, FullRegionName.OAKLAVILLE_RAVE
)
stanhamn_regions = (
    FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_PHOTO_GUILD_HUT, FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, 
    FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_UNDERWATER, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, 
    FullRegionName.STANHAMN_LIGHTHOUSE, FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, FullRegionName.STANHAMN_KING_FISH_BEACH, 
    FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.STANHAMN_FISHING_TOWER, 
    FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, 
    FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, FullRegionName.STANHAMN_HYDROPLANT
)
logcity_regions = (
    FullRegionName.LOGCITY_BUS_STOP, FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_CROSSWALK, FullRegionName.LOGCITY_OVERPASS,
    FullRegionName.LOGCITY_NEWS_HOUSE, FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_RATSKULLZ_ALLEY, 
    FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_FASHION_SHOW_TOP, FullRegionName.LOGCITY_FASHION_SHOW_BOTTOM,
    FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_CAFE,
    FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_GALLERY
)
kiiruberg_regions = (
    FullRegionName.KIIRUBERG_BUS_STOP, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, 
    FullRegionName.KIIRUBERG_BALLOON_HOUSE, FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, 
    FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_TOP, FullRegionName.KIIRUBERG_MILITARY_BASE, 
    FullRegionName.KIIRUBERG_MECKS_HOUSE, FullRegionName.KIIRUBERG_OUTSIDE_WIZARD_TOWER, FullRegionName.KIIRUBERG_WIZARD_TOWER, 
    FullRegionName.KIIRUBERG_COSMO_GARDEN, FullRegionName.KIIRUBERG_CLIFFS_BOTTOM, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, 
    FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_LOWER_LEFT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_UPPER_LEFT, 
    FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.KIIRUBERG_MAN_CAVE, FullRegionName.KIIRUBERG_BLIZZARD_MONSTER, 
    FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_TOP, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, FullRegionName.KIIRUBERG_OBSERVATORY, 
    FullRegionName.KIIRUBERG_SKI_LIFT_BASE, FullRegionName.KIIRUBERG_SKI_LODGE, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP
)
mountain_top_regions = (FullRegionName.MOUNTAIN_TOP_BUS_STOP, FullRegionName.MOUNTAIN_TOP_TOEM)
basto_regions = (
    FullRegionName.BASTO_BUS_STOP_TOP, FullRegionName.BASTO_BUS_STOP_BOTTOM, FullRegionName.BASTO_LILY_PAD_POND_LEFT,
    FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_CAMP, FullRegionName.BASTO_TENT, 
    FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_CASTLE, FullRegionName.BASTO_GYM_HOUSE, 
    FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_BONFIRE_BOTTOM, FullRegionName.BASTO_CARNIVAL,
    FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_CAVE, FullRegionName.BASTO_SECRET_CAVE, 
    FullRegionName.BASTO_JUNGLE
)

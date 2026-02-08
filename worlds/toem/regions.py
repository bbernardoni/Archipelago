from typing import final, ClassVar
from BaseClasses import Region, Entrance
from entrance_rando import ERPlacementState

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

class ToemEntrance(Entrance):
    def can_connect_to(self, other: Entrance, dead_end: bool, er_state: "ERPlacementState") -> bool:
        """
        """
        living_room_entrances = {"Player room exit", "Homelanda house entrance"}
        if self.name in living_room_entrances and other.name in living_room_entrances:
            return False
        if not dead_end:
            if other.name in {"Oaklaville trail up", "Rave entrance", "Fashion show backstage entrance"}:
                return False
            required_regions = {
                "Oaklaville trail down": (FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.OAKLAVILLE_HOTEL),
                "Hotel exit": (FullRegionName.OAKLAVILLE_LOOKOUT,),
                "Docks left exit": (FullRegionName.STANHAMN_HYDROPLANT,),
                "Docks right exit": (FullRegionName.STANHAMN_HYDROPLANT,),
                "Ghost drawbridge left": (FullRegionName.STANHAMN_HYDROPLANT,),
                "Ghost drawbridge down": (FullRegionName.STANHAMN_HYDROPLANT,),
                "Wizard tower exit": (FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,),
            }
            if other.name in required_regions:
                if not all(er_state.world.get_region(region) in er_state.placed_regions for region in required_regions[other.name]):
                    return False
            if other.name == "Hydroplant exit":
                stanhamn_exits = [ex for region in er_state.world.multiworld.get_regions(er_state.world.player) if region.name.startswith(RegionName.STANHAMN)
                                for ex in region.exits if not ex.connected_region]
                placeable_stanhamn_exits = er_state.find_placeable_exits(True, stanhamn_exits)
                if len(placeable_stanhamn_exits) <= 1:
                    return False
            if other.name == "Lookout exit":
                oaklaville_exits = [ex for region in er_state.world.multiworld.get_regions(er_state.world.player) if region.name.startswith(RegionName.OAKLAVILLE)
                                for ex in region.exits if not ex.connected_region]
                placeable_oaklaville_exits = er_state.find_placeable_exits(True, oaklaville_exits)
                if len(placeable_oaklaville_exits) <= 1:
                    return False
        
        # Run the regular Entrance class's method and return its result like normal.
        return super().can_connect_to(other, dead_end, er_state)

class ToemRegion(Region):
    entrance_type: ClassVar[type[ToemEntrance]] = ToemEntrance

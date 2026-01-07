from dataclasses import dataclass
from itertools import groupby
from typing import final

from BaseClasses import Item, ItemClassification

from .constants import GAME_NAME
from .regions import RegionName


@final
class ItemGroup:
    STAMP = "Stamp"
    PHOTO = "Photo"
    ITEM = "Item"
    CASSETTE = "Cassette"


@final
class ItemName:
    HOMELANDA_STAMP = "Homelanda stamp"
    OAKLAVILLE_STAMP = "Oaklaville stamp"
    STANHAMN_STAMP = "Stanhamn stamp"
    LOGCITY_STAMP = "Logcity stamp"
    KIIRUBERG_STAMP = "Kiiruberg stamp"
    BASTO_STAMP = "Basto stamp"
    PROGRESSIVE_STAMP = "Progressive stamp"

    COW_PHOTO = "Cow photo"
    FLIES_PHOTO = "Flies photo"
    HOME_BIRD_PHOTO = "Home bird photo"
    TATO_PHOTO = "Tato photo"
    ANT_PHOTO = "Ant photo"
    BEEHIVE_PHOTO = "Beehive photo"
    BUTTERFLY_PHOTO = "Butterfly photo"
    OSKAR_PHOTO = "Oskar photo"
    SERO_PHOTO = "Sero photo"
    FOREST_BIRD_PHOTO = "Forest bird photo"
    LADYBUG_PHOTO = "Ladybug photo"
    TOM_PHOTO = "Tom photo"
    NESTWORM_PHOTO = "Nestworm photo"
    PET_ROCK_PHOTO = "Pet rock photo"
    SNAIL_PHOTO = "Snail photo"
    SQUIRREL_PHOTO = "Squirrel photo"
    STAG_BEETLE_PHOTO = "Stag beetle photo"
    TATO_BUG_PHOTO = "Tato bug photo"
    TATO_FLY_PHOTO = "Tato fly photo"
    BUBBLE_FLY_PHOTO = "Bubble fly photo"
    FIA_PHOTO = "Fia photo"
    FRAS_PHOTO = "Fräs photo"
    WILLEMIJN_PHOTO = "Willemijn photo"
    CRAB_PHOTO = "Crab photo"
    DRAGONFLY_PHOTO = "Dragonfly photo"
    HAPPY_CARP_PHOTO = "Happy carp photo"
    JELLYFISH_PHOTO = "Jellyfish photo"
    KING_FISH_PHOTO = "King fish photo"
    SEAGULL_PHOTO = "Seagull photo"
    SEAHORSE_PHOTO = "Seahorse photo"
    SUNDAY_SWAN_PHOTO = "Sunday swan photo"
    TATO_SCUBA_PHOTO = "Tato scuba photo"
    TATO_SWIM_PHOTO = "Tato swim photo"
    TOAD_PHOTO = "Toad photo"
    BUSINESS_PIGEON_PHOTO = "Business pigeon photo"
    PORTILLO_PHOTO = "Portillo photo"
    MOUSE_PHOTO = "Mouse photo"
    PIGEON_PHOTO = "Pigeon photo"
    PUNK_PARROT_PHOTO = "Punky parrot photo"
    TATO_SKATEBOARD_PHOTO = "Tato skateboard photo"
    TATO_TOURIST_PHOTO = "Tato tourist photo"
    TURTLE_PHOTO = "Turtle photo"
    MIKEE_PHOTO = "Mikée photo"
    NARIKO_PHOTO = "Nariko photo"
    COSMO_DEER_PHOTO = "Cosmo deer photo"
    TEDDY_PHOTO = "Teddy photo"
    FLUFF_PHOTO = "Fluff ball photo"
    HEDGEHOG_PHOTO = "Hedgehog photo"
    METEOPAL_PHOTO = "Meteopal photo"
    GOAT_PHOTO = "Mountain goat photo"
    OWL_PHOTO = "Owl photo"
    SNOW_BIRD_PHOTO = "Snow bird photo"
    TATO_ALIEN_PHOTO = "Tato alien photo"
    TATO_SKI_PHOTO = "Tato ski photo"
    BAT_PHOTO = "Bat photo"
    SNAKE_PHOTO = "Beach snake photo"
    BEAK_BIRD_PHOTO = "Beak bird photo"
    BITLING_FROG_PHOTO = "Bitling frog photo"
    BITLING_MOUSE_PHOTO = "Bitling mouse photo"
    BITLING_SNAIL_PHOTO = "Bitling snail photo"
    BITLING_TATO_PHOTO = "Bitling tato photo"
    COCO_CRAB_PHOTO = "Coco crab photo"
    DAY_LIZARD_PHOTO = "Day lizard photo"
    DRILL_MOLE_PHOTO = "Drill mole photo"
    EGGERT_PHOTO = "Eggert photo"
    FIRE_FLY_PHOTO = "Fire fly photo"
    GLOW_WORM_PHOTO = "Glow worm photo"
    ITSY_BITSY_PHOTO = "Itsy bitsy photo"
    MUD_FROG_PHOTO = "Mud frog photo"
    NIGHT_LIZARD_PHOTO = "Night lizard photo"
    SNOUT_BUG_PHOTO = "Snout bug photo"
    TATO_COCO_PHOTO = "Tato coco photo"
    TATO_KING_PHOTO = "Tato king photo"
    WATER_STRIDER_PHOTO = "Water strider photo"

    CLOGS = "Clogs"
    AWARD_MASK = "Award Mask"
    FINGER = "Foam finger"
    TRIPOD = "Tripod"
    COWBOY_HAT = "Cowboy hat"
    WET_SOCKS = "Pair of wet socks"
    FJALLBJORN_HAT = "Fjällbjörn hat"
    GHOST_GLASSES = "Ghost glasses"
    SOAKED_SOCK = "Soaked sock"
    MONSTER_MASK = "Monster mask"
    FRAMES_FILTERS = "Frames & filters"
    FISHING_HAT = "Fishing hat"
    HONK_ATTACHMENT = "Honk attachment"
    UMBRELLA = "Umbrella"
    OLD_KEY = "Old key"
    HARD_HAT = "Hard hat"
    DIVING_HELMET = "Diving helmet"
    RUBBER_BOOTS = "Rubber boots"
    SANDWICH = "Supreme deluxe sandwich"
    PIRATE_HAT = "Pirate hat"
    PAPER_HAT = "Paper hat"
    FLAG = "Photo challenger flag"
    HOTBEAN_HAT = "Hotbean hat"
    REPORTER_HAT = "Reporter hat"
    SNEAKERS = "Sneakers"
    CINNAMON_BUN = "Cinnamon bun"
    FRISBEE = "Frisbee"
    CLIMBING_BOOTS = "Climbing boots"
    PUFFER_HAT = "Puffer hat"
    SCARF = "Scarf"
    SKI_GOGGLES = "Ski goggles"
    SPACE_HELMET = "Space helmet"
    WATERGUN = "Water popper attachment"
    SUN_HAT = "Sun hat"
    MELONEAR = "Melonear"
    BANAKIN = "Banakin"
    ORANGANAS = "Oranganas"
    BEANUT = "Beanut"
    PICKAXE = "Pickaxe"
    SUN_CAP = "Sun cap"
    FLIP_FLOPS = "Flip-flops"
    ICE_CREAM = "Ice cream"
    ROYAL_CAPE = "Royal cape"
    MINIGAME_TICKET = "Minigame ticket"
    LEI = "Lei"
    VACATION_SHIRT = "Vacation shirt"
    ROYAL_CANE = "Royal cane"
    EMPTY_BOTTLE = "Empty bottle"
    VIKING_HELMET = "Viking helmet"
    FOOT_CAST = "Foot cast"
    BERET = "Beret"
    ROYAL_CROWN = "Royal crown"

    PHOTO_OF_HOME_TAPE = "Jamal Green - Photo of Home"
    SUMMER_BREEZE_TAPE = "Jamal Green - Summer Breeze"
    SQUIRREL_HOTEL_TAPE = "Jamal Green - The Grand Squirrel Hotel"
    PINE_NEEDLES_TAPE = "Launchable Socks - Pine Needles"
    SQUIRREL_PHOTO_TAPE = "Launchable Socks - Squirrel Photography"
    FISHERMANS_WHISTLE_TAPE = "Fisherman's Whistle"
    SMILING_HUNTSMAN_TAPE = "JG+LS - The Smiling Huntsman"
    NAUT_TAPE = "Jamal Green - NAUT"
    PLACE_IN_SUN_TAPE = "Launchable Socks - A Place In The Sun"
    FISHERMANS_TUNE_TAPE = "Launchable Socks - Fisherman's Tune"
    RATSKULLZ_THEME_TAPE = "Anes Sabanovic - Ratskullz Theme"
    BIG_CITY_TAPE = "JG+LS - The Big City"
    HUSTLE_BUSTLE_TAPE = "Jamal Green - Hustle Bustle Shuffle"
    HOP_SKIP_STEP_TAPE = "Launchable Socks - Hop Skip Step"
    ON_THE_HOUR_TAPE = "Launchable Socks - On The Hour"
    LIFE_THROUGH_LENS_TAPE = "Jamal Green - Life Through a Lens"
    PETTING_DEER_TAPE = "Jamal Green - The Petting of a Sacred Deer"
    STORIES_OF_SNOW_TAPE = "Launchable Socks - Stories Of Snow"
    TALL_SHY_TAPE = "Launchable Socks - Tall & Shy"
    NIGHT_JAM_TAPE = "JG+LS - Night Jam"
    WARM_DAYS_NIGHT_TAPE = "Jamal Green - A Warm Days Night"
    ONE_BY_ONE_TAPE = "Jamal Green - One By One"
    HAMMOCK_DAYS_TAPE = "Launchable Socks - Hammock Days"
    SAILORS_TUNE_TAPE = "Launchable Socks - Sailor's Tune"
    SONG_OF_THE_SEA_TAPE = "Launchable Socks - Song Of The Sea"


class ToemItem(Item):
    game: str = GAME_NAME


@dataclass(frozen=True)
class ItemData:
    classification: ItemClassification
    quantity: int
    group: str
    parent_region: str

progression_useful = ItemClassification.progression | ItemClassification.useful

item_table: dict[str, ItemData] = {
    ItemName.HOMELANDA_STAMP: ItemData(progression_useful, 3, ItemGroup.STAMP, RegionName.HOMELANDA),
    ItemName.OAKLAVILLE_STAMP: ItemData(ItemClassification.progression, 15, ItemGroup.STAMP, RegionName.OAKLAVILLE),
    ItemName.STANHAMN_STAMP: ItemData(ItemClassification.progression, 16, ItemGroup.STAMP, RegionName.STANHAMN),
    ItemName.LOGCITY_STAMP: ItemData(ItemClassification.progression, 18, ItemGroup.STAMP, RegionName.LOGCITY),
    ItemName.KIIRUBERG_STAMP: ItemData(ItemClassification.progression, 13, ItemGroup.STAMP, RegionName.KIIRUBERG),
    ItemName.BASTO_STAMP: ItemData(ItemClassification.progression, 20, ItemGroup.STAMP, RegionName.BASTO),
    ItemName.COW_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.HOMELANDA),
    ItemName.FLIES_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.HOMELANDA),
    ItemName.HOME_BIRD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.HOMELANDA),
    ItemName.TATO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.HOMELANDA),
    ItemName.ANT_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.BEEHIVE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.BUTTERFLY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.OSKAR_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.SERO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.FOREST_BIRD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.LADYBUG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.TOM_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.NESTWORM_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.PET_ROCK_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.SNAIL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.SQUIRREL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.STAG_BEETLE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.TATO_BUG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.TATO_FLY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.OAKLAVILLE),
    ItemName.BUBBLE_FLY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.FIA_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.FRAS_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.WILLEMIJN_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.CRAB_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.DRAGONFLY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.HAPPY_CARP_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.JELLYFISH_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.KING_FISH_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.SEAGULL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.SEAHORSE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.SUNDAY_SWAN_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.TATO_SCUBA_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.TATO_SWIM_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.TOAD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.STANHAMN),
    ItemName.BUSINESS_PIGEON_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.PORTILLO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.MOUSE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.PIGEON_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.PUNK_PARROT_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.TATO_SKATEBOARD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.TATO_TOURIST_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.TURTLE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.LOGCITY),
    ItemName.MIKEE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.NARIKO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.COSMO_DEER_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.TEDDY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.FLUFF_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.HEDGEHOG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.METEOPAL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.GOAT_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.OWL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.SNOW_BIRD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.TATO_ALIEN_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.TATO_SKI_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.KIIRUBERG),
    ItemName.BAT_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.SNAKE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.BEAK_BIRD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.BITLING_FROG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.BITLING_MOUSE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.BITLING_SNAIL_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.BITLING_TATO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.COCO_CRAB_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.DAY_LIZARD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.DRILL_MOLE_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.EGGERT_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.FIRE_FLY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.GLOW_WORM_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.ITSY_BITSY_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.MUD_FROG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.NIGHT_LIZARD_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.SNOUT_BUG_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.TATO_COCO_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.TATO_KING_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.WATER_STRIDER_PHOTO: ItemData(ItemClassification.filler, 1, ItemGroup.PHOTO, RegionName.BASTO),
    ItemName.CLOGS: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.HOMELANDA),
    ItemName.AWARD_MASK: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.HOMELANDA),
    ItemName.FINGER: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.TRIPOD: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.COWBOY_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.WET_SOCKS: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.FJALLBJORN_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.GHOST_GLASSES: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.SOAKED_SOCK: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.MONSTER_MASK: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.OAKLAVILLE),
    ItemName.FRAMES_FILTERS: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.FISHING_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.HONK_ATTACHMENT: ItemData(progression_useful, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.UMBRELLA: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.OLD_KEY: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.HARD_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.DIVING_HELMET: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.RUBBER_BOOTS: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.SANDWICH: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.PIRATE_HAT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.PAPER_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.FLAG: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.STANHAMN),
    ItemName.HOTBEAN_HAT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.LOGCITY),
    ItemName.REPORTER_HAT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.LOGCITY),
    ItemName.SNEAKERS: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.LOGCITY),
    ItemName.CINNAMON_BUN: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.LOGCITY),
    ItemName.FRISBEE: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.LOGCITY),
    ItemName.CLIMBING_BOOTS: ItemData(progression_useful, 1, ItemGroup.ITEM, RegionName.KIIRUBERG),
    ItemName.PUFFER_HAT: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.KIIRUBERG),
    ItemName.SCARF: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.KIIRUBERG),
    ItemName.SKI_GOGGLES: ItemData(ItemClassification.progression_deprioritized_skip_balancing, 1, ItemGroup.ITEM, RegionName.KIIRUBERG),
    ItemName.SPACE_HELMET: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.KIIRUBERG),
    ItemName.WATERGUN: ItemData(progression_useful, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.SUN_HAT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.MELONEAR: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.BANAKIN: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.ORANGANAS: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.BEANUT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.PICKAXE: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.SUN_CAP: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.FLIP_FLOPS: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.ICE_CREAM: ItemData(ItemClassification.progression, 4, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.ROYAL_CAPE: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.MINIGAME_TICKET: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.LEI: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.VACATION_SHIRT: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.ROYAL_CANE: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.EMPTY_BOTTLE: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.VIKING_HELMET: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.FOOT_CAST: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.BERET: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.ROYAL_CROWN: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM, RegionName.BASTO),
    ItemName.PHOTO_OF_HOME_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.HOMELANDA),
    ItemName.SUMMER_BREEZE_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.OAKLAVILLE),
    ItemName.SQUIRREL_HOTEL_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.OAKLAVILLE),
    ItemName.PINE_NEEDLES_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.OAKLAVILLE),
    ItemName.SQUIRREL_PHOTO_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.OAKLAVILLE),
    ItemName.FISHERMANS_WHISTLE_TAPE: ItemData(ItemClassification.progression, 1, ItemGroup.CASSETTE, RegionName.STANHAMN),
    ItemName.SMILING_HUNTSMAN_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.STANHAMN),
    ItemName.NAUT_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.STANHAMN),
    ItemName.PLACE_IN_SUN_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.STANHAMN),
    ItemName.FISHERMANS_TUNE_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.STANHAMN),
    ItemName.RATSKULLZ_THEME_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.LOGCITY),
    ItemName.BIG_CITY_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.LOGCITY),
    ItemName.HUSTLE_BUSTLE_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.LOGCITY),
    ItemName.HOP_SKIP_STEP_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.LOGCITY),
    ItemName.ON_THE_HOUR_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.LOGCITY),
    ItemName.LIFE_THROUGH_LENS_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.KIIRUBERG),
    ItemName.PETTING_DEER_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.KIIRUBERG),
    ItemName.STORIES_OF_SNOW_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.KIIRUBERG),
    ItemName.TALL_SHY_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.KIIRUBERG),
    ItemName.NIGHT_JAM_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.WARM_DAYS_NIGHT_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.ONE_BY_ONE_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.HAMMOCK_DAYS_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.SAILORS_TUNE_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.SONG_OF_THE_SEA_TAPE: ItemData(ItemClassification.filler, 1, ItemGroup.CASSETTE, RegionName.BASTO),
    ItemName.PROGRESSIVE_STAMP: ItemData(progression_useful, 85, ItemGroup.STAMP, RegionName.MENU),
}

item_name_to_id: dict[str, int] = {name: i for i, name in enumerate(item_table, start=1)}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def get_item_area(location_name: str) -> str:
    return item_table[location_name].parent_region


item_name_groups: dict[str, set[str]] = {
    group: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}
item_name_groups.update(
    {group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_area), get_item_area) if group != RegionName.MENU}
)


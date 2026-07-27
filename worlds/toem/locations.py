from dataclasses import dataclass
from itertools import groupby
from typing import TYPE_CHECKING, final

from typing_extensions import override

from BaseClasses import CollectionState, Location
from NetUtils import JSONMessagePart
from rule_builder.field_resolvers import FromOption, FromWorldAttr
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, CanReachRegion, Has, HasAll, HasAny, Rule, True_

from .constants import GAME_NAME
from .items import HardLogic, ItemName
from .options import (
    BastoStampRequirement,
    HomelandaStampRequirement,
    IncludeBasto,
    KiirubergStampRequirement,
    LogcityStampRequirement,
    OaklavilleStampRequirement,
    ProgressiveStamps,
    StanhamnStampRequirement,
)
from .regions import Area, RegionName, gameplay_areas

if TYPE_CHECKING:
    from . import ToemWorld

@final
class EventName:
    TOEM_EXPERIENCED = "TOEM Experienced"
    BASTO_BONFIRE = "Basto Bonfire"
    BASTO_LILY_PAD_POND_LEFT_DAY = "Basto - Lily pad pond left day"
    BASTO_LILY_PAD_POND_LEFT_NIGHT = "Basto - Lily pad pond left night"
    BASTO_CAMP_DAY = "Basto - Camp day"
    BASTO_CAMP_NIGHT = "Basto - Camp night"
    BASTO_BONFIRE_BOTTOM_DAY = "Basto - Bonfire bottom day"


@dataclass(frozen=True)
class EventData:
    region: str
    is_day: bool

event_table: dict[str, EventData] = {
    EventName.BASTO_LILY_PAD_POND_LEFT_DAY: EventData(RegionName.BASTO_LILY_PAD_POND_LEFT, True),
    EventName.BASTO_LILY_PAD_POND_LEFT_NIGHT: EventData(RegionName.BASTO_LILY_PAD_POND_LEFT, False),
    EventName.BASTO_CAMP_DAY: EventData(RegionName.BASTO_CAMP, True),
    EventName.BASTO_CAMP_NIGHT: EventData(RegionName.BASTO_CAMP, False),
    EventName.BASTO_BONFIRE_BOTTOM_DAY: EventData(RegionName.BASTO_BONFIRE_BOTTOM, True),
}


@final
class LocationGroup:
    QUEST = "Quest"
    COMPENDIUM = "Compendium"
    ITEM = "Item"
    CASSETTE = "Cassette"
    ACHIEVEMENT = "Achievement"


@final
class LocationName:
    # Homelanda
    QUEST_PHOTO_OF_NANA = "Quest - Take a photo of Nana!"
    QUEST_HIDDEN_GIFT = "Quest - A hidden gift"
    QUEST_EXPERIENCE_TOEM = "Quest - Experience TOEM"

    COMP_COW = "Compendium - Cow"
    COMP_FLIES = "Compendium - Flies"
    COMP_HOME_BIRD = "Compendium - Home bird"
    COMP_TATO = "Compendium - Tato"

    ITEM_CLOGS = "Item - Clogs"
    ITEM_AWARD_MASK = "Item - Award Mask"

    TAPE_PHOTO_OF_HOME = "Cassette - Jamal Green - Photo of Home"

    CHEEVO_BEGINNING = "Achievement - The beginning"
    CHEEVO_HOME_SWEET_HOME = "Achievement - Home sweet home"

    # Oaklaville
    QUEST_SUS_FOREST = "Quest - Suspicious activity - forest"
    QUEST_MONSTERS = "Quest - Monster spotting"
    QUEST_SOCKS = "Quest - Missing socks"
    QUEST_SCOUTS = "Quest - Become a scout"
    QUEST_HIDE_AND_SEEK = "Quest - Hide-and-seek"
    QUEST_LOG_JAM = "Quest - Log blocking a path"
    QUEST_CHALLENGE_1 = "Quest - Photo challenge #1"
    QUEST_CHALLENGE_2 = "Quest - Photo challenge #2"
    QUEST_PAPARAZZI = "Quest - Become a paparazzi"
    QUEST_CAPTURE_HOTEL = "Quest - Capture the hotel's beauty"
    QUEST_HOTEL_CHEF = "Quest - Hotel chef"
    QUEST_STALLION = "Quest - A courageous stallion"
    QUEST_GHOST_HELPER = "Quest - Ghost helper!"
    QUEST_CUP_CHAMP = "Quest - Cup champion"
    QUEST_FLOWER = "Quest - Become a flower"

    COMP_ANT = "Compendium - Ant"
    COMP_BEEHIVE = "Compendium - Beehive"
    COMP_BUTTERFLY = "Compendium - Butterfly"
    COMP_OSKAR = "Compendium - Oskar"
    COMP_SERO = "Compendium - Sero"
    COMP_FOREST_BIRD = "Compendium - Forest bird"
    COMP_LADYBUG = "Compendium - Ladybug"
    COMP_TOM = "Compendium - Tom"
    COMP_NESTWORM = "Compendium - Nestworm"
    COMP_PET_ROCK = "Compendium - Pet rock"
    COMP_SNAIL = "Compendium - Snail"
    COMP_SQUIRREL = "Compendium - Squirrel"
    COMP_STAG_BEETLE = "Compendium - Stag beetle"
    COMP_TATO_BUG = "Compendium - Tato bug"
    COMP_TATO_FLY = "Compendium - Tato fly"

    ITEM_FINGER = "Item - Foam finger"
    ITEM_TRIPOD = "Item - Tripod"
    ITEM_COWBOY_HAT = "Item - Cowboy hat"
    ITEM_WET_SOCKS = "Item - Pair of wet socks"
    ITEM_FJALLBJORN_HAT = "Item - Fjällbjörn hat"
    ITEM_GHOST_GLASSES = "Item - Ghost glasses"
    ITEM_SOAKED_SOCK = "Item - Soaked sock"
    ITEM_MONSTER_MASK = "Item - Monster mask"

    TAPE_SUMMER_BREEZE = "Cassette - Jamal Green - Summer Breeze"
    TAPE_SQUIRREL_HOTEL = "Cassette - Jamal Green - The Grand Squirrel Hotel"
    TAPE_PINE_NEEDLES = "Cassette - Launchable Socks - Pine Needles"
    TAPE_SQUIRREL_PHOTO = "Cassette - Launchable Socks - Squirrel Photography"

    CHEEVO_CALM_FOREST = "Achievement - The calm forest"
    CHEEVO_MAJESTIC_HOTEL = "Achievement - A majestic hotel"
    CHEEVO_SLOW_AND_STEADY = "Achievement - Slow and steady"
    CHEEVO_NATURE_SHOWSTOPPER = "Achievement - Nature's show-stopper"
    CHEEVO_STRONG_AS_AN_OAK = "Achievement - Strong as an oak"
    CHEEVO_CALMED_DOWN = "Achievement - Calmed down"
    CHEEVO_JUST_A_SOCK = "Achievement - Just a sock"
    CHEEVO_YOU_FOUND_US = "Achievement - You found us!"

    # Stanhamn
    QUEST_KING_FISH = "Quest - The king of fishes"
    QUEST_GOOD_SPOT = "Quest - A good spot with no sun"
    QUEST_SUS_HARBOR = "Quest - Suspicious activity - harbor"
    QUEST_PAPER_HATS = "Quest - Queen of paper hats"
    QUEST_CHALLENGE_3 = "Quest - Photo challenge #3"
    QUEST_CHALLENGE_4 = "Quest - Photo challenge #4"
    QUEST_FRAMES_FILTERS = "Quest - Frames & filters!"
    QUEST_TAKE_A_BATH = "Quest - Make someone take a bath"
    QUEST_LOST_DOG = "Quest - A lost dog"
    QUEST_POWER = "Quest - Power shortage?!"
    QUEST_CHAOS = "Quest - Solve the chaos"
    QUEST_FLAME = "Quest - Scorching flame?"
    QUEST_SANDWICH = "Quest - Supreme deluxe sandwich?!"
    QUEST_GARBAGE = "Quest - Ocean garbage"
    QUEST_WHISTLING = "Quest - A whistling dilemma"
    QUEST_MELODY = "Quest - A layered melody"

    COMP_BUBBLE_FLY = "Compendium - Bubble fly"
    COMP_FIA = "Compendium - Fia"
    COMP_FRAS = "Compendium - Fräs"
    COMP_WILLEMIJN = "Compendium - Willemijn"
    COMP_CRAB = "Compendium - Crab"
    COMP_DRAGONFLY = "Compendium - Dragonfly"
    COMP_HAPPY_CARP = "Compendium - Happy carp"
    COMP_JELLYFISH = "Compendium - Jellyfish"
    COMP_KING_FISH = "Compendium - King fish"
    COMP_SEAGULL = "Compendium - Seagull"
    COMP_SEAHORSE = "Compendium - Seahorse"
    COMP_SUNDAY_SWAN = "Compendium - Sunday swan"
    COMP_TATO_SCUBA = "Compendium - Tato scuba"
    COMP_TATO_SWIM = "Compendium - Tato swim"
    COMP_TOAD = "Compendium - Toad"

    ITEM_FRAMES_FILTERS = "Item - Frames & filters"
    ITEM_FISHING_HAT = "Item - Fishing hat"
    ITEM_HONK_ATTACHMENT = "Item - Honk attachment"
    ITEM_UMBRELLA = "Item - Umbrella"
    ITEM_OLD_KEY = "Item - Old key"
    ITEM_HARD_HAT = "Item - Hard hat"
    ITEM_DIVING_HELMET = "Item - Diving helmet"
    ITEM_RUBBER_BOOTS = "Item - Rubber boots"
    ITEM_SANDWICH = "Item - Supreme deluxe sandwich"
    ITEM_PIRATE_HAT = "Item - Pirate hat"
    ITEM_PAPER_HAT = "Item - Paper hat"
    ITEM_FLAG = "Item - Photo challenger flag"

    TAPE_FISHERMANS_WHISTLE = "Cassette - Fisherman's Whistle"
    TAPE_SMILING_HUNTSMAN = "Cassette - JG+LS - The Smiling Huntsman"
    TAPE_NAUT = "Cassette - Jamal Green - NAUT"
    TAPE_PLACE_IN_SUN = "Cassette - Launchable Socks - A Place In The Sun"
    TAPE_FISHERMANS_TUNE = "Cassette - Launchable Socks - Fisherman's Tune"

    CHEEVO_SET_SAIL = "Achievement - Set sail for good weather"
    CHEEVO_VOYAGE_UNDERWATER = "Achievement - A voyage underwater"
    CHEEVO_EMPLOYEE_OF_THE_MONTH = "Achievement - Employee of the month"
    CHEEVO_CALM_AS_SEA = "Achievement - Calm as the sea"
    CHEEVO_SEAWORTHY = "Achievement - Seaworthy"
    CHEEVO_FLIGHT_READY = "Achievement - Flight ready"
    CHEEVO_SPARKLING_JUMP = "Achievement - A sparkling jump"
    CHEEVO_GOOD_BOY = "Achievement - Who's a good boy?!"

    # Logcity
    QUEST_SUS_CITY = "Quest - Suspicious activity - city"
    QUEST_RATSKULLZ = "Quest - Ratskullz crew"
    QUEST_PUNK_ROCKER = "Quest - Punk rocker bread crumbs"
    QUEST_CHALLENGE_5 = "Quest - Photo challenge #5"
    QUEST_CHALLENGE_6 = "Quest - Photo challenge #6"
    QUEST_NEWS = "Quest - Press-ing news"
    QUEST_SEWER = "Quest - Sewer stumble!"
    QUEST_HOTBEAN = "Quest - Super Hotbean Bros."
    QUEST_HANG_IN_THERE = "Quest - Hang in there, buddy"
    QUEST_SCARY_CITY = "Quest - Spooky scary city"
    QUEST_DATE = "Quest - A ghostly date"
    QUEST_ART = "Quest - Art exhibition"
    QUEST_INFLUENCER = "Quest - Young and inspiring!"
    QUEST_FASHION = "Quest - A design problem"
    QUEST_CLEANING = "Quest - Cleaning away the stress"
    QUEST_GRANNY = "Quest - Always tumbled granny"
    QUEST_MICE = "Quest - A mouse bakery"
    QUEST_CROW = "Quest - A thieving crow"

    COMP_BUSINESS_PIGEON = "Compendium - Business pigeon"
    COMP_PORTILLO = "Compendium - Portillo"
    COMP_MOUSE = "Compendium - Mouse"
    COMP_PIGEON = "Compendium - Pigeon"
    COMP_PUNK_PARROT = "Compendium - Punky parrot"
    COMP_TATO_SKATEBOARD = "Compendium - Tato skateboard"
    COMP_TATO_TOURIST = "Compendium - Tato tourist"
    COMP_TURTLE = "Compendium - Turtle"

    ITEM_HOTBEAN_HAT = "Item - Hotbean hat"
    ITEM_REPORTER_HAT = "Item - Reporter hat"
    ITEM_SNEAKERS = "Item - Sneakers"
    ITEM_CINNAMON_BUN = "Item - Cinnamon bun"
    ITEM_FRISBEE = "Item - Frisbee"

    TAPE_RATSKULLZ_THEME = "Cassette - Anes Sabanovic - Ratskullz Theme"
    TAPE_BIG_CITY = "Cassette - JG+LS - The Big City"
    TAPE_HUSTLE_BUSTLE = "Cassette - Jamal Green - Hustle Bustle Shuffle"
    TAPE_HOP_SKIP_STEP = "Cassette - Launchable Socks - Hop Skip Step"
    TAPE_ON_THE_HOUR = "Cassette - Launchable Socks - On The Hour"

    CHEEVO_BIG_CITY = "Achievement - The big city"
    CHEEVO_CLOCKTOWER = "Achievement - The grand clock tower"
    CHEEVO_PROFESSIONAL = "Achievement - City professional"
    CHEEVO_BUSINESS = "Achievement - Business executed"
    CHEEVO_FOLLOWERS = "Achievement - 100 followers!"
    CHEEVO_NEW_JOB = "Achievement - A new job"

    # Kiiruberg
    QUEST_YETI_CUTE = "Quest - Yeti cuteness"
    QUEST_ICE_WIZARD = "Quest - Ice wizard's research"
    QUEST_MILITARY_SUS = "Quest - Military suspicions"
    QUEST_ASTRONAUT = "Quest - Play astronaut"
    QUEST_CHALLENGE_7 = "Quest - Photo challenge #7"
    QUEST_CHALLENGE_8 = "Quest - Photo challenge #8"
    QUEST_ASTEROID = "Quest - Locating an asteroid"
    QUEST_GOAT_CHOIR = "Quest - Listen to the goat choir"
    QUEST_SNOWBALL = "Quest - Snowball memories"
    QUEST_BIRTHDAY = "Quest - Birthday in distress"
    QUEST_PAINTINGS = "Quest - Ancient paintings"
    QUEST_BECOME_YETI = "Quest - Become a yeti"
    QUEST_SNOWMAN = "Quest - Assemble a snowman"

    COMP_MIKEE = "Compendium - Mikée"
    COMP_NARIKO = "Compendium - Nariko"
    COMP_COSMO_DEER = "Compendium - Cosmo deer"
    COMP_TEDDY = "Compendium - Teddy"
    COMP_FLUFF = "Compendium - Fluff ball"
    COMP_HEDGEHOG = "Compendium - Hedgehog"
    COMP_METEOPAL = "Compendium - Meteopal"
    COMP_GOAT = "Compendium - Mountain goat"
    COMP_OWL = "Compendium - Owl"
    COMP_SNOW_BIRD = "Compendium - Snow bird"
    COMP_TATO_ALIEN = "Compendium - Tato alien"
    COMP_TATO_SKI = "Compendium - Tato ski"

    ITEM_CLIMBING_BOOTS = "Item - Climbing boots"
    ITEM_PUFFER_HAT = "Item - Puffer hat"
    ITEM_SCARF = "Item - Scarf"
    ITEM_SKI_GOGGLES = "Item - Ski goggles"
    ITEM_SPACE_HELMET = "Item - Space helmet"

    TAPE_LIFE_THROUGH_LENS = "Cassette - Jamal Green - Life Through a Lens"
    TAPE_PETTING_DEER = "Cassette - Jamal Green - The Petting of a Sacred Deer"
    TAPE_STORIES_OF_SNOW = "Cassette - Launchable Socks - Stories Of Snow"
    TAPE_TALL_SHY = "Cassette - Launchable Socks - Tall & Shy"

    CHEEVO_SNOWY_PEAKS = "Achievement - Snowy peaks"
    CHEEVO_GEARED_UP = "Achievement - All geared up"
    CHEEVO_HURDLE = "Achievement - The biggest hurdle"
    CHEEVO_FIGHTER = "Achievement - Ice fighter"
    CHEEVO_YOUTH = "Achievement - Happy youth"
    CHEEVO_STORY = "Achievement - A great story"

    # Mountain Top
    CHEEVO_CLOSE = "Achievement - So close now!"
    CHEEVO_TOEM = "Achievement - Experience TOEM"

    # Overall
    CHEEVO_CUTIES = "Achievement - Look at those cuties"
    CHEEVO_COLLECT_EM_ALL = "Achievement - Collect them all"
    CHEEVO_GOING_LONG = "Achievement - Going long!"
    CHEEVO_COSPLAYER = "Achievement - Cosplayer"
    CHEEVO_COMPLETIONIST = "Achievement - A true completionist"

    # Basto
    QUEST_BALLOONS = "Quest - Basto's hidden balloons"
    QUEST_ARTHUR = "Quest - Arthur hunter"
    QUEST_BAD_HAIR_DAY = "Quest - Bad hair day"
    QUEST_TAKE_A_NAP = "Quest - Take a nap!"
    QUEST_SPOOKY_STORIES = "Quest - Spooky stories"
    QUEST_PORTRAITS = "Quest - Painterly portrait"
    QUEST_CINEMA = "Quest - Night-time cinema"
    QUEST_NIGHT_LIGHTS = "Quest - Night lights"
    QUEST_JET_SKI = "Quest - Jet-ski tricks"
    QUEST_FRUITS = "Quest - Fruit shortage"
    QUEST_BRAIN_FREEZE = "Quest - Brain freeze"
    QUEST_SWEET_TOOTH = "Quest - Sweet tooth"
    QUEST_IN_YOUR_FACE = "Quest - In your face"
    QUEST_BROKEN_DREAMS = "Quest - Broken dreams"
    QUEST_DRY_SEASON = "Quest - Dry season"
    QUEST_MUSCLES = "Quest - Dehydrated muscles"
    QUEST_SAND_CASTLE = "Quest - Sand castle competition"
    QUEST_CARNIVAL = "Quest - Play a carnival game"
    QUEST_BATS = "Quest - Book of bats"
    QUEST_BITLING = "Quest - Bitling collector"

    COMP_BAT = "Compendium - Bat"
    COMP_SNAKE = "Compendium - Beach snake"
    COMP_BEAK_BIRD = "Compendium - Beak bird"
    COMP_BITLING_FROG = "Compendium - Bitling frog"
    COMP_BITLING_MOUSE = "Compendium - Bitling mouse"
    COMP_BITLING_SNAIL = "Compendium - Bitling snail"
    COMP_BITLING_TATO = "Compendium - Bitling tato"
    COMP_COCO_CRAB = "Compendium - Coco crab"
    COMP_DAY_LIZARD = "Compendium - Day lizard"
    COMP_DRILL_MOLE = "Compendium - Drill mole"
    COMP_EGGERT = "Compendium - Eggert"
    COMP_FIRE_FLY = "Compendium - Fire fly"
    COMP_GLOW_WORM = "Compendium - Glow worm"
    COMP_ITSY_BITSY = "Compendium - Itsy bitsy"
    COMP_MUD_FROG = "Compendium - Mud frog"
    COMP_NIGHT_LIZARD = "Compendium - Night lizard"
    COMP_SNOUT_BUG = "Compendium - Snout bug"
    COMP_TATO_COCO = "Compendium - Tato coco"
    COMP_TATO_KING = "Compendium - Tato king"
    COMP_WATER_STRIDER = "Compendium - Water strider"

    ITEM_BASTO_TICKET = "Item - Viking Express Ticket"
    ITEM_WATERGUN = "Item - Water popper attachment"
    ITEM_SUN_HAT = "Item - Sun hat"
    ITEM_MELONEAR = "Item - Melonear"
    ITEM_BANAKIN = "Item - Banakin"
    ITEM_ORANGANAS = "Item - Oranganas"
    ITEM_BEANUT = "Item - Beanut"
    ITEM_PICKAXE = "Item - Pickaxe"
    ITEM_SUN_CAP = "Item - Sun cap"
    ITEM_FLIP_FLOPS = "Item - Flip-flops"
    ITEM_ICE_CREAM_BANAKIN = "Item - Ice cream (Banakin)"
    ITEM_ICE_CREAM_MELONEAR = "Item - Ice cream (Melonear)"
    ITEM_ICE_CREAM_BEANUT = "Item - Ice cream (Beanut)"
    ITEM_ICE_CREAM_ORANGANAS = "Item - Ice cream (Oranganas)"
    ITEM_ROYAL_CAPE = "Item - Royal cape"
    ITEM_MINIGAME_TICKET = "Item - minigame ticket"
    ITEM_LEI = "Item - Lei"
    ITEM_VACATION_SHIRT = "Item - Vacation shirt"
    ITEM_ROYAL_CANE = "Item - Royal cane"
    ITEM_EMPTY_BOTTLE = "Item - Empty bottle"
    ITEM_VIKING_HELMET = "Item - Viking helmet"
    ITEM_FOOT_CAST = "Item - Foot cast"
    ITEM_BERET = "Item - Beret"
    ITEM_ROYAL_CROWN = "Item - Royal crown"

    TAPE_NIGHT_JAM = "Cassette - JG+LS - Night Jam"
    TAPE_WARM_DAYS_NIGHT = "Cassette - Jamal Green - A Warm Days Night"
    TAPE_ONE_BY_ONE = "Cassette - Jamal Green - One By One"
    TAPE_HAMMOCK_DAYS = "Cassette - Launchable Socks - Hammock Days"
    TAPE_SAILORS_TUNE = "Cassette - Launchable Socks - Sailor's Tune"
    TAPE_SONG_OF_THE_SEA = "Cassette - Launchable Socks - Song Of The Sea"

    CHEEVO_TOPICAL_PARADISE = "Achievement - Tropical paradise"
    CHEEVO_MAXIMUM_VACATION = "Achievement - Maximum vacation"
    CHEEVO_KINGS_SHIRT = "Achievement - King's new shirt"
    CHEEVO_MOONLIT_BEAUTY = "Achievement - Moonlit beauty"
    CHEEVO_SELF_PORTRAIT = "Achievement - Self portrait"
    CHEEVO_WAZZUUPPP = "Achievement - Wazzuuppp"
    CHEEVO_PRO_GAMER = "Achievement - Pro gamer"
    CHEEVO_SPLISH_SPLASH = "Achievement - Splish-splash"
    CHEEVO_ROYAL_CASTLE = "Achievement - The Royal Castle"
    CHEEVO_SOME_MORE = "Achievement - And some more"
    CHEEVO_VIKINGS_HOLIDAY = "Achievement - A Viking's holiday"


class ToemLocation(Location):
    game: str = GAME_NAME


@dataclass(frozen=True)
class LocationData:
    region: str
    group: str
    rule: Rule | None = None

def CanReachAllRegions(*regions: str) -> Rule:  # noqa: N802
    rule = CanReachRegion(regions[0])
    for region in regions[1:]:
        rule = rule & CanReachRegion(region)
    return rule

def CanReachAnyRegion(*regions: str) -> Rule:  # noqa: N802
    rule = CanReachRegion(regions[0])
    for region in regions[1:]:
        rule = rule | CanReachRegion(region)
    return rule

def CanReachAllLocations(*locations: str) -> Rule:  # noqa: N802
    rule = CanReachLocation(locations[0])
    for location in locations[1:]:
        rule = rule & CanReachLocation(location)
    return rule

def CanReachAnyLocation(*locations: str) -> Rule:  # noqa: N802
    rule = CanReachLocation(locations[0])
    for location in locations[1:]:
        rule = rule | CanReachLocation(location)
    return rule

oaklaville_quests = (
    LocationName.QUEST_SUS_FOREST, LocationName.QUEST_MONSTERS, LocationName.QUEST_SOCKS, LocationName.QUEST_SCOUTS,
    LocationName.QUEST_HIDE_AND_SEEK, LocationName.QUEST_LOG_JAM, LocationName.QUEST_CHALLENGE_1,
    LocationName.QUEST_CHALLENGE_2, LocationName.QUEST_PAPARAZZI, LocationName.QUEST_CAPTURE_HOTEL,
    LocationName.QUEST_HOTEL_CHEF, LocationName.QUEST_STALLION, LocationName.QUEST_GHOST_HELPER,
    LocationName.QUEST_CUP_CHAMP, LocationName.QUEST_FLOWER
)
stanhamn_quests = (
    LocationName.QUEST_KING_FISH, LocationName.QUEST_GOOD_SPOT, LocationName.QUEST_SUS_HARBOR,
    LocationName.QUEST_PAPER_HATS, LocationName.QUEST_CHALLENGE_3, LocationName.QUEST_CHALLENGE_4,
    LocationName.QUEST_FRAMES_FILTERS, LocationName.QUEST_TAKE_A_BATH, LocationName.QUEST_LOST_DOG,
    LocationName.QUEST_POWER, LocationName.QUEST_CHAOS, LocationName.QUEST_FLAME, LocationName.QUEST_SANDWICH,
    LocationName.QUEST_GARBAGE, LocationName.QUEST_WHISTLING, LocationName.QUEST_MELODY
)
logcity_quests = (
    LocationName.QUEST_RATSKULLZ, LocationName.QUEST_PUNK_ROCKER, LocationName.QUEST_CHALLENGE_5,
    LocationName.QUEST_CHALLENGE_6, LocationName.QUEST_NEWS, LocationName.QUEST_SEWER, LocationName.QUEST_HOTBEAN,
    LocationName.QUEST_HANG_IN_THERE, LocationName.QUEST_SCARY_CITY, LocationName.QUEST_DATE, LocationName.QUEST_ART,
    LocationName.QUEST_INFLUENCER, LocationName.QUEST_FASHION, LocationName.QUEST_CLEANING, LocationName.QUEST_GRANNY,
    LocationName.QUEST_MICE, LocationName.QUEST_CROW
)
kiiruberg_quests = (
    LocationName.QUEST_YETI_CUTE, LocationName.QUEST_ICE_WIZARD, LocationName.QUEST_MILITARY_SUS,
    LocationName.QUEST_ASTRONAUT, LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8,
    LocationName.QUEST_ASTEROID, LocationName.QUEST_GOAT_CHOIR, LocationName.QUEST_SNOWBALL,
    LocationName.QUEST_BIRTHDAY, LocationName.QUEST_PAINTINGS, LocationName.QUEST_BECOME_YETI,
    LocationName.QUEST_SNOWMAN
)
dev_animals = (
    LocationName.COMP_OSKAR, LocationName.COMP_SERO, LocationName.COMP_PET_ROCK, LocationName.COMP_FIA,
    LocationName.COMP_FRAS, LocationName.COMP_WILLEMIJN, LocationName.COMP_PORTILLO, LocationName.COMP_MIKEE,
    LocationName.COMP_NARIKO, LocationName.COMP_TEDDY
)
base_animals = (
    LocationName.COMP_COW, LocationName.COMP_FLIES, LocationName.COMP_HOME_BIRD, LocationName.COMP_TATO,
    LocationName.COMP_ANT, LocationName.COMP_BEEHIVE, LocationName.COMP_BUTTERFLY, LocationName.COMP_OSKAR,
    LocationName.COMP_SERO, LocationName.COMP_FOREST_BIRD, LocationName.COMP_LADYBUG, LocationName.COMP_TOM,
    LocationName.COMP_NESTWORM, LocationName.COMP_PET_ROCK, LocationName.COMP_SNAIL, LocationName.COMP_SQUIRREL,
    LocationName.COMP_STAG_BEETLE, LocationName.COMP_TATO_BUG, LocationName.COMP_TATO_FLY, LocationName.COMP_BUBBLE_FLY,
    LocationName.COMP_FIA, LocationName.COMP_FRAS, LocationName.COMP_WILLEMIJN, LocationName.COMP_CRAB,
    LocationName.COMP_DRAGONFLY, LocationName.COMP_HAPPY_CARP, LocationName.COMP_JELLYFISH, LocationName.COMP_KING_FISH,
    LocationName.COMP_SEAGULL, LocationName.COMP_SEAHORSE, LocationName.COMP_SUNDAY_SWAN, LocationName.COMP_TATO_SCUBA,
    LocationName.COMP_TATO_SWIM, LocationName.COMP_TOAD, LocationName.COMP_BUSINESS_PIGEON, LocationName.COMP_PORTILLO,
    LocationName.COMP_MOUSE, LocationName.COMP_PIGEON, LocationName.COMP_PUNK_PARROT, LocationName.COMP_TATO_SKATEBOARD,
    LocationName.COMP_TATO_TOURIST, LocationName.COMP_TURTLE, LocationName.COMP_MIKEE, LocationName.COMP_NARIKO,
    LocationName.COMP_COSMO_DEER, LocationName.COMP_TEDDY, LocationName.COMP_FLUFF, LocationName.COMP_HEDGEHOG,
    LocationName.COMP_METEOPAL, LocationName.COMP_GOAT, LocationName.COMP_OWL, LocationName.COMP_SNOW_BIRD,
    LocationName.COMP_TATO_ALIEN, LocationName.COMP_TATO_SKI
)
fashionable_hats = ( # does not accept reporter hat, diving helmet, or space helmet
    ItemName.FJALLBJORN_HAT, ItemName.COWBOY_HAT, ItemName.FISHING_HAT, ItemName.HARD_HAT, ItemName.PIRATE_HAT,
    ItemName.PAPER_HAT, ItemName.HOTBEAN_HAT, ItemName.PUFFER_HAT
)
fashionable_hats_basto = (
    ItemName.SUN_HAT,  ItemName.SUN_CAP,  ItemName.BERET,  ItemName.ROYAL_CROWN, ItemName.VIKING_HELMET
)
clothing_items = (
    ItemName.CLOGS, ItemName.FINGER, ItemName.GHOST_GLASSES, ItemName.SOAKED_SOCK, ItemName.FJALLBJORN_HAT,
    ItemName.COWBOY_HAT, ItemName.FISHING_HAT, ItemName.UMBRELLA, ItemName.HARD_HAT, ItemName.DIVING_HELMET,
    ItemName.PIRATE_HAT, ItemName.PAPER_HAT, ItemName.RUBBER_BOOTS, ItemName.HOTBEAN_HAT, ItemName.REPORTER_HAT,
    ItemName.SNEAKERS, ItemName.CLIMBING_BOOTS, ItemName.SCARF, ItemName.PUFFER_HAT, ItemName.SKI_GOGGLES,
    ItemName.MONSTER_MASK, ItemName.FLAG, ItemName.SPACE_HELMET
)
completionist_reqs = (
    LocationName.QUEST_PHOTO_OF_NANA, LocationName.QUEST_HIDDEN_GIFT, LocationName.QUEST_EXPERIENCE_TOEM,
    LocationName.CHEEVO_STRONG_AS_AN_OAK, LocationName.CHEEVO_SEAWORTHY, LocationName.CHEEVO_BUSINESS,
    LocationName.CHEEVO_FIGHTER
)
warm_clothes = HasAll(ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)
photo_challenges = (
    LocationName.QUEST_CHALLENGE_1, LocationName.QUEST_CHALLENGE_2, LocationName.QUEST_CHALLENGE_3,
    LocationName.QUEST_CHALLENGE_4, LocationName.QUEST_CHALLENGE_5, LocationName.QUEST_CHALLENGE_6,
    LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8
)
basto_animals = (
    LocationName.COMP_BAT, LocationName.COMP_SNAKE, LocationName.COMP_BEAK_BIRD, LocationName.COMP_BITLING_FROG,
    LocationName.COMP_BITLING_MOUSE, LocationName.COMP_BITLING_SNAIL, LocationName.COMP_BITLING_TATO,
    LocationName.COMP_COCO_CRAB, LocationName.COMP_DAY_LIZARD, LocationName.COMP_DRILL_MOLE, LocationName.COMP_EGGERT,
    LocationName.COMP_FIRE_FLY, LocationName.COMP_GLOW_WORM, LocationName.COMP_ITSY_BITSY, LocationName.COMP_MUD_FROG,
    LocationName.COMP_NIGHT_LIZARD, LocationName.COMP_SNOUT_BUG, LocationName.COMP_TATO_COCO,
    LocationName.COMP_TATO_KING, LocationName.COMP_WATER_STRIDER
)
basto_quests = (
    LocationName.QUEST_BALLOONS, LocationName.QUEST_ARTHUR, LocationName.QUEST_BAD_HAIR_DAY,
    LocationName.QUEST_TAKE_A_NAP, LocationName.QUEST_SPOOKY_STORIES, LocationName.QUEST_PORTRAITS,
    LocationName.QUEST_CINEMA, LocationName.QUEST_NIGHT_LIGHTS, LocationName.QUEST_JET_SKI, LocationName.QUEST_FRUITS,
    LocationName.QUEST_BRAIN_FREEZE, LocationName.QUEST_SWEET_TOOTH, LocationName.QUEST_IN_YOUR_FACE,
    LocationName.QUEST_BROKEN_DREAMS, LocationName.QUEST_DRY_SEASON, LocationName.QUEST_MUSCLES,
    LocationName.QUEST_SAND_CASTLE, LocationName.QUEST_CARNIVAL, LocationName.QUEST_BATS, LocationName.QUEST_BITLING
)
portrait_locations = (
    LocationName.CHEEVO_CALMED_DOWN, LocationName.CHEEVO_JUST_A_SOCK, LocationName.CHEEVO_SPARKLING_JUMP,
    LocationName.CHEEVO_FLIGHT_READY, LocationName.CHEEVO_FOLLOWERS, LocationName.CHEEVO_NEW_JOB,
    LocationName.CHEEVO_YOUTH, LocationName.CHEEVO_STORY, LocationName.CHEEVO_MOONLIT_BEAUTY,
    LocationName.CHEEVO_KINGS_SHIRT
)

def get_stamp_rule(region: str) -> Rule:
    stamp_option = {
        Area.HOMELANDA: HomelandaStampRequirement,
        Area.OAKLAVILLE: OaklavilleStampRequirement,
        Area.STANHAMN: StanhamnStampRequirement,
        Area.LOGCITY: LogcityStampRequirement,
        Area.KIIRUBERG: KiirubergStampRequirement,
        Area.BASTO: BastoStampRequirement,
    }[region]
    stamp_item = {
        Area.HOMELANDA: ItemName.HOMELANDA_STAMP,
        Area.OAKLAVILLE: ItemName.OAKLAVILLE_STAMP,
        Area.STANHAMN: ItemName.STANHAMN_STAMP,
        Area.LOGCITY: ItemName.LOGCITY_STAMP,
        Area.KIIRUBERG: ItemName.KIIRUBERG_STAMP,
        Area.BASTO: ItemName.BASTO_STAMP,
    }[region]
    return (
        Has(ItemName.PROGRESSIVE_STAMP, FromWorldAttr(f"progressive_stamp_requirements.{region}"),
            options=[OptionFilter(ProgressiveStamps, ProgressiveStamps.option_true)]) |
        Has(stamp_item, FromOption(stamp_option),
            options=[OptionFilter(ProgressiveStamps, ProgressiveStamps.option_false)])
    )

bonfire_rule = Has(ItemName.WATERGUN) & get_stamp_rule(Area.BASTO)

ratskullz_regions = (
    RegionName.LOGCITY_CLOCK_TOWER, RegionName.LOGCITY_CROSSWALK, RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
    RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_RATSKULLZ_ALLEY, RegionName.LOGCITY_OVERPASS,
    RegionName.LOGCITY_OUTSIDE_CAFE, RegionName.LOGCITY_OUTSIDE_GALLERY, RegionName.LOGCITY_OUTSIDE_GALLERY,
    RegionName.LOGCITY_BUS_STOP
)

@dataclass()
class RatskullzRule(Rule["ToemWorld"], game=GAME_NAME):
    @override
    def _instantiate(self, world: "ToemWorld") -> Rule.Resolved:
        return self.Resolved(player=world.player, caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return sum(state.can_reach_region(region, self.player) for region in ratskullz_regions) >= 5

        @override
        def region_dependencies(self) -> dict[str, set[int]]:
            return {region: {id(self)} for region in ratskullz_regions}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            messages: list[JSONMessagePart] = []
            if state is None:
                messages = [
                    {"type": "text", "text": "Can reach "},
                    {"type": "color", "color": "cyan", "text": "5"},
                    {"type": "text", "text": "x regions from ("},
                ]
                for i, region in enumerate(ratskullz_regions):
                    if i > 0:
                        messages.append({"type": "text", "text": ", "})
                    messages.append({"type": "color", "color": "yellow", "text": region})
                messages.append({"type": "text", "text": ")"})
                return messages

            found_count = sum(state.can_reach_region(region, self.player) for region in ratskullz_regions)
            found = [region for region in ratskullz_regions if state.can_reach_region(region, self.player)]
            missing = [region for region in ratskullz_regions if region not in found]
            color = "green" if found_count >= 5 else "salmon"
            messages = [
                {"type": "text", "text": "Reached "},
                {
                    "type": "color",
                    "color": color,
                    "text": f"{found_count}/5",
                },
                {"type": "text", "text": " regions from ("},
            ]
            if found:
                messages.append({"type": "text", "text": "Reached: "})
                for i, region in enumerate(found):
                    if i > 0:
                        messages.append({"type": "text", "text": ", "})
                    messages.append({"type": "color", "color": "green", "text": region})
                if missing:
                    messages.append({"type": "text", "text": "; "})

            if missing:
                messages.append({"type": "text", "text": "Cannot reach: "})
                for i, region in enumerate(missing):
                    if i > 0:
                        messages.append({"type": "text", "text": ", "})
                    messages.append({"type": "color", "color": "salmon", "text": region})
            messages.append({"type": "text", "text": ")"})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            found_count = sum(state.can_reach_region(region, self.player) for region in ratskullz_regions)
            found = [region for region in ratskullz_regions if state.can_reach_region(region, self.player)]
            missing = [region for region in ratskullz_regions if region not in found]
            found_str = f"Reached: {', '.join(found)}" if found else ""
            missing_str = f"Cannot reach: {', '.join(missing)}" if missing else ""
            infix = "; " if found and missing else ""
            return f"Reached {found_count}/5 regions from ({found_str}{infix}{missing_str})"

        @override
        def __str__(self) -> str:
            return f"Can reach 5x regions from ({', '.join(ratskullz_regions)})"

location_table: dict[str, LocationData] = {
    LocationName.QUEST_PHOTO_OF_NANA: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.QUEST),
    LocationName.QUEST_HIDDEN_GIFT: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.QUEST,
            Has(ItemName.CLOGS)),
    LocationName.QUEST_EXPERIENCE_TOEM: LocationData(RegionName.HOMELANDA_LIVING_ROOM, LocationGroup.QUEST,
            Has(ItemName.CLIMBING_BOOTS) & CanReachRegion(RegionName.MOUNTAIN_TOP_TOEM)),
    LocationName.COMP_COW: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_FLIES: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_HOME_BIRD: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.ITEM_CLOGS: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.ITEM),
    LocationName.ITEM_AWARD_MASK: LocationData(RegionName.HOMELANDA_PLAYER_ROOM, LocationGroup.ITEM,
            Has(ItemName.HONK_ATTACHMENT)),
    LocationName.TAPE_PHOTO_OF_HOME: LocationData(RegionName.HOMELANDA_LIVING_ROOM, LocationGroup.CASSETTE),
    LocationName.CHEEVO_BEGINNING: LocationData(RegionName.HOMELANDA_LIVING_ROOM, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_HOME_SWEET_HOME: LocationData(RegionName.HOMELANDA_BUS_STOP, LocationGroup.ACHIEVEMENT),
    LocationName.QUEST_SUS_FOREST: LocationData(RegionName.OAKLAVILLE_TRAIL_BOTTOM, LocationGroup.QUEST,
            CanReachRegion(RegionName.OAKLAVILLE_HIDE_AND_SEEK)),
    LocationName.QUEST_MONSTERS: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST,
            (HasAll(ItemName.TRIPOD, ItemName.HONK_ATTACHMENT) | HardLogic(True_())) &
            CanReachAllRegions(RegionName.OAKLAVILLE_PLAYGROUND, RegionName.STANHAMN_HIPPO_BEACH,
                               RegionName.LOGCITY_SKATE_PARK, RegionName.KIIRUBERG_BLIZZARD_MONSTER)),
    LocationName.QUEST_SOCKS: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.QUEST,
            Has(ItemName.WET_SOCKS)),
    LocationName.QUEST_SCOUTS: LocationData(RegionName.OAKLAVILLE_CAMP, LocationGroup.QUEST,
            CanReachAllRegions(RegionName.OAKLAVILLE_LOOKOUT, RegionName.OAKLAVILLE_BUS_STOP) &
            CanReachAnyRegion(RegionName.OAKLAVILLE_PLAYGROUND, RegionName.OAKLAVILLE_MUSHROOM_HOUSE)),
    LocationName.QUEST_HIDE_AND_SEEK: LocationData(RegionName.OAKLAVILLE_HIDE_AND_SEEK, LocationGroup.QUEST),
    LocationName.QUEST_LOG_JAM: LocationData(RegionName.OAKLAVILLE_TRAIL_BOTTOM, LocationGroup.QUEST,
            CanReachAllRegions(RegionName.OAKLAVILLE_CAMP, RegionName.OAKLAVILLE_BUS_STOP,
                               RegionName.OAKLAVILLE_HOTEL)),
    LocationName.QUEST_CHALLENGE_1: LocationData(RegionName.OAKLAVILLE_TRAIL_BOTTOM, LocationGroup.QUEST,
            CanReachRegion(RegionName.OAKLAVILLE_CAMP)),
    LocationName.QUEST_CHALLENGE_2: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.QUEST,
            CanReachRegion(RegionName.OAKLAVILLE_TRAIL_BOTTOM)),
    LocationName.QUEST_PAPARAZZI: LocationData(RegionName.OAKLAVILLE_RAVE, LocationGroup.QUEST),
    LocationName.QUEST_CAPTURE_HOTEL: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST,
            CanReachRegion(RegionName.OAKLAVILLE_LOOKOUT)),
    LocationName.QUEST_HOTEL_CHEF: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST,
            CanReachRegion(RegionName.OAKLAVILLE_LOOKOUT)),
    LocationName.QUEST_STALLION: LocationData(RegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.QUEST,
            Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.OAKLAVILLE_HOTEL)),
    LocationName.QUEST_GHOST_HELPER: LocationData(RegionName.OAKLAVILLE_SKELETON_HOUSE, LocationGroup.QUEST,
            CanReachAllLocations(LocationName.QUEST_CUP_CHAMP, LocationName.QUEST_STALLION, LocationName.QUEST_SANDWICH,
                                 LocationName.QUEST_FLAME, LocationName.QUEST_DATE, LocationName.QUEST_SCARY_CITY)),
    LocationName.QUEST_CUP_CHAMP: LocationData(RegionName.OAKLAVILLE_GHOST_CUP_GAME, LocationGroup.QUEST,
            Has(ItemName.GHOST_GLASSES)),
    LocationName.QUEST_FLOWER: LocationData(RegionName.OAKLAVILLE_PLAYGROUND, LocationGroup.QUEST),
    LocationName.COMP_ANT: LocationData(RegionName.OAKLAVILLE_TRAIL_BOTTOM, LocationGroup.COMPENDIUM),
    LocationName.COMP_BEEHIVE: LocationData(RegionName.OAKLAVILLE_PLAYGROUND, LocationGroup.COMPENDIUM),
    LocationName.COMP_BUTTERFLY: LocationData(RegionName.OAKLAVILLE_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_OSKAR: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_SERO: LocationData(RegionName.SERO, LocationGroup.COMPENDIUM),
    LocationName.COMP_FOREST_BIRD: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_LADYBUG: LocationData(RegionName.OAKLAVILLE_CAMP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TOM: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_NESTWORM: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_PET_ROCK: LocationData(RegionName.OAKLAVILLE_CAMP, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNAIL: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_SQUIRREL: LocationData(RegionName.SQUIRRELS, LocationGroup.COMPENDIUM),
    LocationName.COMP_STAG_BEETLE: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_BUG: LocationData(RegionName.OAKLAVILLE_MUSHROOM_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_FLY: LocationData(RegionName.TATO_FLY, LocationGroup.COMPENDIUM),
    LocationName.ITEM_FINGER: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ITEM),
    LocationName.ITEM_TRIPOD: LocationData(RegionName.START_MENU, LocationGroup.ITEM,
            CanReachAnyLocation(*photo_challenges)),
    LocationName.ITEM_COWBOY_HAT: LocationData(RegionName.OAKLAVILLE_MUSHROOM_HOUSE, LocationGroup.ITEM),
    LocationName.ITEM_WET_SOCKS: LocationData(RegionName.OAKLAVILLE_GHOST_CUP_GAME, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_CUP_CHAMP)),
    LocationName.ITEM_FJALLBJORN_HAT: LocationData(RegionName.OAKLAVILLE_CAMP, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_SCOUTS)),
    LocationName.ITEM_GHOST_GLASSES: LocationData(RegionName.GHOST_GLASSES, LocationGroup.ITEM),
    LocationName.ITEM_SOAKED_SOCK: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_SOCKS)),
    LocationName.ITEM_MONSTER_MASK: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_MONSTERS)),
    LocationName.TAPE_SUMMER_BREEZE: LocationData(RegionName.OAKLAVILLE_HIDE_AND_SEEK, LocationGroup.CASSETTE),
    LocationName.TAPE_SQUIRREL_HOTEL: LocationData(RegionName.OAKLAVILLE_HOTEL_ELEVATOR, LocationGroup.CASSETTE),
    LocationName.TAPE_PINE_NEEDLES: LocationData(RegionName.OAKLAVILLE_LOOKOUT, LocationGroup.CASSETTE),
    LocationName.TAPE_SQUIRREL_PHOTO: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.CASSETTE),
    LocationName.CHEEVO_CALM_FOREST: LocationData(RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_MAJESTIC_HOTEL: LocationData(RegionName.OAKLAVILLE_LOOKOUT, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SLOW_AND_STEADY: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_NATURE_SHOWSTOPPER: LocationData(RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(LocationName.QUEST_CHALLENGE_1, LocationName.QUEST_CHALLENGE_2)),
    LocationName.CHEEVO_STRONG_AS_AN_OAK: LocationData(RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*oaklaville_quests)),
    LocationName.CHEEVO_CALMED_DOWN: LocationData(RegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_JUST_A_SOCK: LocationData(RegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_SOCKS)),
    LocationName.CHEEVO_YOU_FOUND_US: LocationData(RegionName.OAKLAVILLE_HOTEL, LocationGroup.ACHIEVEMENT),
    LocationName.QUEST_KING_FISH: LocationData(RegionName.STANHAMN_BUS_STOP, LocationGroup.QUEST,
            CanReachLocation(LocationName.COMP_KING_FISH)),
    LocationName.QUEST_GOOD_SPOT: LocationData(RegionName.STANHAMN_HIPPO_BEACH, LocationGroup.QUEST),
    LocationName.QUEST_SUS_HARBOR: LocationData(RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, LocationGroup.QUEST,
            CanReachRegion(RegionName.STANHAMN_BUS_STOP)),
    LocationName.QUEST_PAPER_HATS: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.QUEST,
            HasAll(ItemName.HONK_ATTACHMENT, ItemName.PIRATE_HAT)),
    LocationName.QUEST_CHALLENGE_3: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.QUEST,
            CanReachRegion(RegionName.STANHAMN_HIPPO_BEACH)),
    LocationName.QUEST_CHALLENGE_4: LocationData(RegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, LocationGroup.QUEST,
            CanReachRegion(RegionName.STANHAMN_HIPPO_BEACH)),
    LocationName.QUEST_FRAMES_FILTERS: LocationData(RegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.QUEST,
            Has(ItemName.FRAMES_FILTERS)),
    LocationName.QUEST_TAKE_A_BATH: LocationData(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.QUEST,
            Has(ItemName.HONK_ATTACHMENT) & CanReachRegion(RegionName.STANHAMN_HYDROPLANT)),
    LocationName.QUEST_LOST_DOG: LocationData(RegionName.STANHAMN_DOCKS_RIGHT, LocationGroup.QUEST,
            CanReachRegion(RegionName.STANHAMN_HIPPO_BEACH)),
    LocationName.QUEST_POWER: LocationData(RegionName.STANHAMN_HYDROPLANT, LocationGroup.QUEST),
    LocationName.QUEST_CHAOS: LocationData(RegionName.STANHAMN_LIGHTHOUSE_ROOF, LocationGroup.QUEST,
            CanReachAllRegions(RegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, RegionName.STANHAMN_LIGHTHOUSE)),
    LocationName.QUEST_FLAME: LocationData(RegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, LocationGroup.QUEST,
            Has(ItemName.GHOST_GLASSES)),
    LocationName.QUEST_SANDWICH: LocationData(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.QUEST,
            HasAll(ItemName.GHOST_GLASSES, ItemName.SANDWICH)),
    LocationName.QUEST_GARBAGE: LocationData(RegionName.STANHAMN_FISHING_TOWER, LocationGroup.QUEST),
    LocationName.QUEST_WHISTLING: LocationData(RegionName.STANHAMN_DOCKS_LEFT, LocationGroup.QUEST,
            CanReachRegion(RegionName.STANHAMN_BUS_STOP)),
    LocationName.QUEST_MELODY: LocationData(RegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.QUEST,
            Has(ItemName.FISHERMANS_WHISTLE_TAPE)),
    LocationName.COMP_BUBBLE_FLY: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.COMPENDIUM),
    LocationName.COMP_FIA: LocationData(RegionName.FIA, LocationGroup.COMPENDIUM),
    LocationName.COMP_FRAS: LocationData(RegionName.FRAS, LocationGroup.COMPENDIUM),
    LocationName.COMP_WILLEMIJN: LocationData(RegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.COMPENDIUM),
    LocationName.COMP_CRAB: LocationData(RegionName.STANHAMN_HIPPO_BEACH, LocationGroup.COMPENDIUM),
    LocationName.COMP_DRAGONFLY: LocationData(RegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.COMPENDIUM),
    LocationName.COMP_HAPPY_CARP: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_JELLYFISH: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_KING_FISH: LocationData(RegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.COMPENDIUM,
            CanReachLocation(LocationName.QUEST_MELODY)),
    LocationName.COMP_SEAGULL: LocationData(RegionName.SEAGULLS, LocationGroup.COMPENDIUM),
    LocationName.COMP_SEAHORSE: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_SUNDAY_SWAN: LocationData(RegionName.SUNDAY_SWAN, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_SCUBA: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_SWIM: LocationData(RegionName.STANHAMN_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TOAD: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.COMPENDIUM),
    LocationName.ITEM_FRAMES_FILTERS: LocationData(RegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.ITEM),
    LocationName.ITEM_FISHING_HAT: LocationData(RegionName.STANHAMN_LIGHTHOUSE, LocationGroup.ITEM),
    LocationName.ITEM_HONK_ATTACHMENT: LocationData(RegionName.STANHAMN_LIGHTHOUSE_ROOF, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_CHAOS)),
    LocationName.ITEM_UMBRELLA: LocationData(RegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.ITEM),
    LocationName.ITEM_OLD_KEY: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.ITEM,
            Has(ItemName.HONK_ATTACHMENT)),
    LocationName.ITEM_HARD_HAT: LocationData(RegionName.STANHAMN_HYDROPLANT, LocationGroup.ITEM),
    LocationName.ITEM_DIVING_HELMET: LocationData(RegionName.STANHAMN_FISHING_TOWER, LocationGroup.ITEM),
    LocationName.ITEM_RUBBER_BOOTS: LocationData(RegionName.STANHAMN_DOCKS_RIGHT, LocationGroup.ITEM),
    LocationName.ITEM_SANDWICH: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.ITEM,
            Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.STANHAMN_OUTSIDE_HYDROPLANT)),
    LocationName.ITEM_PIRATE_HAT: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.ITEM,
            Has(ItemName.OLD_KEY)),
    LocationName.ITEM_PAPER_HAT: LocationData(RegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.ITEM,
            HasAll(ItemName.HONK_ATTACHMENT, ItemName.PIRATE_HAT)),
    LocationName.ITEM_FLAG: LocationData(RegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.ITEM,
            CanReachAllLocations(*photo_challenges)),
    LocationName.TAPE_FISHERMANS_WHISTLE: LocationData(RegionName.STANHAMN_DOCKS_LEFT, LocationGroup.CASSETTE,
            CanReachLocation(LocationName.QUEST_WHISTLING)),
    LocationName.TAPE_SMILING_HUNTSMAN: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.CASSETTE),
    LocationName.TAPE_NAUT: LocationData(RegionName.STANHAMN_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_PLACE_IN_SUN: LocationData(RegionName.STANHAMN, LocationGroup.CASSETTE,
            (CanReachRegion(RegionName.STANHAMN_HIPPO_BEACH) & CanReachLocation(LocationName.QUEST_CHAOS)) |
            (CanReachRegion(RegionName.STANHAMN_DOCKS_LEFT) & CanReachLocation(LocationName.QUEST_POWER))),
    LocationName.TAPE_FISHERMANS_TUNE: LocationData(RegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.CASSETTE,
            CanReachLocation(LocationName.QUEST_MELODY)),
    LocationName.CHEEVO_SET_SAIL: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_VOYAGE_UNDERWATER: LocationData(RegionName.STANHAMN_UNDERWATER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_EMPLOYEE_OF_THE_MONTH: LocationData(RegionName.STANHAMN_HYDROPLANT, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_CALM_AS_SEA: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(LocationName.QUEST_CHALLENGE_3, LocationName.QUEST_CHALLENGE_4)),
    LocationName.CHEEVO_SEAWORTHY: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*stanhamn_quests)),
    LocationName.CHEEVO_FLIGHT_READY: LocationData(RegionName.STANHAMN_FISHING_TOWER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SPARKLING_JUMP: LocationData(RegionName.STANHAMN_BUS_STOP, LocationGroup.ACHIEVEMENT,
            Has(ItemName.HONK_ATTACHMENT)),
    LocationName.CHEEVO_GOOD_BOY: LocationData(RegionName.GOOD_BOY, LocationGroup.ACHIEVEMENT),
    LocationName.QUEST_SUS_CITY: LocationData(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST,
            CanReachRegion(RegionName.LOGCITY_CROSSWALK)),
    LocationName.QUEST_RATSKULLZ: LocationData(RegionName.LOGCITY_RATSKULLZ_ALLEY, LocationGroup.QUEST,
            RatskullzRule()),
    LocationName.QUEST_PUNK_ROCKER: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST,
            Has(ItemName.CINNAMON_BUN)),
    LocationName.QUEST_CHALLENGE_5: LocationData(RegionName.LOGCITY_OVERPASS, LocationGroup.QUEST,
            CanReachAllRegions(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_SKATE_PARK)),
    LocationName.QUEST_CHALLENGE_6: LocationData(RegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.QUEST,
            CanReachRegion(RegionName.LOGCITY_CROSSWALK)),
    LocationName.QUEST_NEWS: LocationData(RegionName.LOGCITY_NEWS_HOUSE, LocationGroup.QUEST,
            Has(ItemName.REPORTER_HAT) & CanReachLocation(LocationName.QUEST_FASHION)),
    LocationName.QUEST_SEWER: LocationData(RegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.QUEST),
    LocationName.QUEST_HOTBEAN: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST,
            Has(ItemName.HOTBEAN_HAT) & CanReachAllRegions(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW,
                                            RegionName.LOGCITY_SKATE_PARK, RegionName.LOGCITY_CROSSWALK)),
    LocationName.QUEST_HANG_IN_THERE: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST),
    LocationName.QUEST_SCARY_CITY: LocationData(RegionName.LOGCITY_CROSSWALK, LocationGroup.QUEST,
            Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.OAKLAVILLE)),
    LocationName.QUEST_DATE: LocationData(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST,
            Has(ItemName.GHOST_GLASSES) & CanReachRegion(RegionName.LOGCITY_OUTSIDE_GALLERY)),
    LocationName.QUEST_ART: LocationData(RegionName.LOGCITY_GALLERY, LocationGroup.QUEST,
            Has(ItemName.FRAMES_FILTERS) | CanReachRegion(RegionName.LOGCITY_RATSKULLZ_ALLEY)),
    LocationName.QUEST_INFLUENCER: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST,
            CanReachRegion(RegionName.LOGCITY_OUTSIDE_CAFE)),
    LocationName.QUEST_FASHION: LocationData(RegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, LocationGroup.QUEST,
            CanReachRegion(RegionName.FASHION_SHOW) & (HasAny(*fashionable_hats) |
            HasAny(*fashionable_hats_basto, options=[OptionFilter(IncludeBasto, IncludeBasto.option_true)]))),
    LocationName.QUEST_CLEANING: LocationData(RegionName.LOGCITY_BUS_STOP, LocationGroup.QUEST,
            CanReachRegion(RegionName.LOGCITY_RATSKULLZ_ALLEY)),
    LocationName.QUEST_GRANNY: LocationData(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST),
    LocationName.QUEST_MICE: LocationData(RegionName.LOGCITY_CAFE, LocationGroup.QUEST,
            Has(ItemName.HONK_ATTACHMENT)),
    LocationName.QUEST_CROW: LocationData(RegionName.LOGCITY_OUTSIDE_CAFE, LocationGroup.QUEST,
            Has(ItemName.FRISBEE)),
    LocationName.COMP_BUSINESS_PIGEON: LocationData(RegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.COMPENDIUM),
    LocationName.COMP_PORTILLO: LocationData(RegionName.LOGCITY_OUTSIDE_CAFE, LocationGroup.COMPENDIUM),
    LocationName.COMP_MOUSE: LocationData(RegionName.MOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_PIGEON: LocationData(RegionName.PIGEON, LocationGroup.COMPENDIUM),
    LocationName.COMP_PUNK_PARROT: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.COMPENDIUM,
            Has(ItemName.CINNAMON_BUN)),
    LocationName.COMP_TATO_SKATEBOARD: LocationData(RegionName.LOGCITY_SKATE_PARK, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_TOURIST: LocationData(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.COMPENDIUM),
    LocationName.COMP_TURTLE: LocationData(RegionName.LOGCITY_CROSSWALK, LocationGroup.COMPENDIUM),
    LocationName.ITEM_HOTBEAN_HAT: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ITEM),
    LocationName.ITEM_REPORTER_HAT: LocationData(RegionName.LOGCITY_NEWS_HOUSE, LocationGroup.ITEM),
    LocationName.ITEM_SNEAKERS: LocationData(RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.ITEM),
    LocationName.ITEM_CINNAMON_BUN: LocationData(RegionName.LOGCITY_CAFE, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_MICE)),
    LocationName.ITEM_FRISBEE: LocationData(RegionName.LOGCITY_CROSSWALK, LocationGroup.ITEM,
            Has(ItemName.HONK_ATTACHMENT) & CanReachRegion(RegionName.LOGCITY_OUTSIDE_CAFE)),
    LocationName.TAPE_RATSKULLZ_THEME: LocationData(RegionName.LOGCITY_RATSKULLZ_ALLEY, LocationGroup.CASSETTE,
            CanReachLocation(LocationName.QUEST_RATSKULLZ)),
    LocationName.TAPE_BIG_CITY: LocationData(RegionName.BIG_CITY_TAPE, LocationGroup.CASSETTE),
    LocationName.TAPE_HUSTLE_BUSTLE: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.CASSETTE),
    LocationName.TAPE_HOP_SKIP_STEP: LocationData(RegionName.LOGCITY_CROSSWALK, LocationGroup.CASSETTE),
    LocationName.TAPE_ON_THE_HOUR: LocationData(RegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.CASSETTE),
    LocationName.CHEEVO_BIG_CITY: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_CLOCKTOWER: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_PROFESSIONAL: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(LocationName.QUEST_CHALLENGE_5, LocationName.QUEST_CHALLENGE_6)),
    LocationName.CHEEVO_BUSINESS: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*logcity_quests)),
    LocationName.CHEEVO_FOLLOWERS: LocationData(RegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_INFLUENCER)),
    LocationName.CHEEVO_NEW_JOB: LocationData(RegionName.LOGCITY_BUS_STOP, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_CLEANING)),
    LocationName.QUEST_YETI_CUTE: LocationData(RegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.QUEST,
            CanReachLocation(LocationName.COMP_FLUFF)),
    LocationName.QUEST_ICE_WIZARD: LocationData(RegionName.KIIRUBERG_WIZARD_TOWER, LocationGroup.QUEST,
            warm_clothes & Has(ItemName.HONK_ATTACHMENT) &
            CanReachAllRegions(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, RegionName.OAKLAVILLE_GHOST_CUP_GAME,
                               RegionName.OAKLAVILLE_CAMP, RegionName.STANHAMN_HIPPO_BEACH,
                               RegionName.LOGCITY_OUTSIDE_FASHION_SHOW, RegionName.LOGCITY_OUTSIDE_GALLERY)),
    LocationName.QUEST_MILITARY_SUS: LocationData(RegionName.KIIRUBERG_MILITARY_BASE, LocationGroup.QUEST,
            CanReachAllLocations(LocationName.QUEST_SUS_FOREST, LocationName.QUEST_SUS_HARBOR,
                                 LocationName.QUEST_SUS_CITY)),
    LocationName.QUEST_ASTRONAUT: LocationData(RegionName.KIIRUBERG_OBSERVATORY, LocationGroup.QUEST,
            Has(ItemName.SPACE_HELMET)),
    LocationName.QUEST_CHALLENGE_7: LocationData(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.QUEST,
            Has(ItemName.CLIMBING_BOOTS) & CanReachRegion(RegionName.BALLOON_ANIMAL)),
    LocationName.QUEST_CHALLENGE_8: LocationData(RegionName.KIIRUBERG_CLIFFS_TOP, LocationGroup.QUEST,
            CanReachAnyRegion(RegionName.KIIRUBERG_OBSERVATORY, RegionName.KIIRUBERG_MILITARY_BASE,
                              RegionName.KIIRUBERG_WIZARD_TOWER)),
    LocationName.QUEST_ASTEROID: LocationData(RegionName.KIIRUBERG_OBSERVATORY, LocationGroup.QUEST,
            CanReachRegion(RegionName.ASTEROID)),
    LocationName.QUEST_GOAT_CHOIR: LocationData(RegionName.KIIRUBERG_FROZEN_POND, LocationGroup.QUEST,
            CanReachAllRegions(RegionName.GOAT_BIRTHDAY_PARTY, RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP,
                               RegionName.GOAT_CLIFFS)),
    LocationName.QUEST_SNOWBALL: LocationData(RegionName.KIIRUBERG_FROZEN_POND, LocationGroup.QUEST,
            Has(ItemName.CLIMBING_BOOTS) | HardLogic(True_())),
    LocationName.QUEST_BIRTHDAY: LocationData(RegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, LocationGroup.QUEST,
            warm_clothes & CanReachRegion(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT)),
    LocationName.QUEST_PAINTINGS: LocationData(RegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.QUEST,
            Has(ItemName.CLIMBING_BOOTS) & CanReachAllRegions(RegionName.KIIRUBERG_FROZEN_POND,
                RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,
                RegionName.MOUNTAIN_TOP_TOEM)),
    LocationName.QUEST_BECOME_YETI: LocationData(RegionName.KIIRUBERG_SKI_LIFT_BASE, LocationGroup.QUEST),
    LocationName.QUEST_SNOWMAN: LocationData(RegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.QUEST,
            Has(ItemName.HONK_ATTACHMENT) & CanReachAllRegions(RegionName.KIIRUBERG_SKI_LIFT_BASE,
                                                               RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP)),
    LocationName.COMP_MIKEE: LocationData(RegionName.KIIRUBERG_BALLOON_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_NARIKO: LocationData(RegionName.KIIRUBERG_BALLOON_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_COSMO_DEER: LocationData(RegionName.KIIRUBERG_COSMO_GARDEN, LocationGroup.COMPENDIUM),
    LocationName.COMP_TEDDY: LocationData(RegionName.KIIRUBERG_MECKS_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_FLUFF: LocationData(RegionName.FLUFF, LocationGroup.COMPENDIUM),
    LocationName.COMP_HEDGEHOG: LocationData(RegionName.HEDGEHOG, LocationGroup.COMPENDIUM),
    LocationName.COMP_METEOPAL: LocationData(RegionName.METEOPAL, LocationGroup.COMPENDIUM,
            CanReachRegion(RegionName.KIIRUBERG_OBSERVATORY)),
    LocationName.COMP_GOAT: LocationData(RegionName.GOAT, LocationGroup.COMPENDIUM,
            CanReachRegion(RegionName.KIIRUBERG_FROZEN_POND) | HardLogic(True_())),
    LocationName.COMP_OWL: LocationData(RegionName.OWL, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNOW_BIRD: LocationData(RegionName.KIIRUBERG_SKI_LIFT_BASE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_ALIEN: LocationData(RegionName.KIIRUBERG_OBSERVATORY, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_SKI: LocationData(RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, LocationGroup.COMPENDIUM),
    LocationName.ITEM_CLIMBING_BOOTS: LocationData(RegionName.KIIRUBERG_FROZEN_POND, LocationGroup.ITEM),
    LocationName.ITEM_PUFFER_HAT: LocationData(RegionName.KIIRUBERG_FROZEN_POND, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_SNOWBALL)),
    LocationName.ITEM_SCARF: LocationData(RegionName.KIIRUBERG_SKI_LODGE, LocationGroup.ITEM),
    LocationName.ITEM_SKI_GOGGLES: LocationData(RegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, LocationGroup.ITEM),
    LocationName.ITEM_SPACE_HELMET: LocationData(RegionName.KIIRUBERG_OUTSIDE_OBSERV_BOTTOM, LocationGroup.ITEM),
    LocationName.TAPE_LIFE_THROUGH_LENS: LocationData(RegionName.KIIRUBERG_OBSERVATORY, LocationGroup.CASSETTE),
    LocationName.TAPE_PETTING_DEER: LocationData(RegionName.KIIRUBERG_COSMO_GARDEN, LocationGroup.CASSETTE),
    LocationName.TAPE_STORIES_OF_SNOW: LocationData(RegionName.STORIES_OF_SNOW_TAPE, LocationGroup.CASSETTE),
    LocationName.TAPE_TALL_SHY: LocationData(RegionName.KIIRUBERG_BLIZZARD_BRIDGE_DL, LocationGroup.CASSETTE,
            warm_clothes),
    LocationName.CHEEVO_SNOWY_PEAKS: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_GEARED_UP: LocationData(RegionName.START_MENU, LocationGroup.ACHIEVEMENT,
            warm_clothes),
    LocationName.CHEEVO_HURDLE: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8)),
    LocationName.CHEEVO_FIGHTER: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*kiiruberg_quests)),
    LocationName.CHEEVO_YOUTH: LocationData(RegionName.KIIRUBERG_OLD_MANS_HOUSE, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_SNOWBALL)),
    LocationName.CHEEVO_STORY: LocationData(RegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_PAINTINGS)),
    LocationName.CHEEVO_CLOSE: LocationData(RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_TOEM: LocationData(RegionName.MOUNTAIN_TOP_TOEM, LocationGroup.ACHIEVEMENT,
            Has(ItemName.CLIMBING_BOOTS)),
    LocationName.CHEEVO_CUTIES: LocationData(RegionName.START_MENU, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*dev_animals)),
    LocationName.CHEEVO_COLLECT_EM_ALL: LocationData(RegionName.START_MENU, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*base_animals)),
    LocationName.CHEEVO_GOING_LONG: LocationData(RegionName.MOUNTAIN_TOP_TOEM, LocationGroup.ACHIEVEMENT), # TODO revisit soft logic  # noqa: E501
    LocationName.CHEEVO_COSPLAYER: LocationData(RegionName.START_MENU, LocationGroup.ACHIEVEMENT,
            HasAll(*clothing_items)),
    LocationName.CHEEVO_COMPLETIONIST: LocationData(RegionName.START_MENU, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*completionist_reqs)),
    LocationName.QUEST_BALLOONS: LocationData(RegionName.BASTO_BUS_STOP_BOTTOM, LocationGroup.QUEST,
            Has(ItemName.WATERGUN) & CanReachAllRegions(RegionName.BASTO_LILY_PAD_POND_LEFT,
                RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_CAMP,
                RegionName.BASTO_OUTSIDE_CASTLE, RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_CARNIVAL,
                RegionName.BASTO_JUNGLE, RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_CASTLE)),
    LocationName.QUEST_ARTHUR: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            Has(ItemName.PICKAXE) & CanReachAllRegions(RegionName.BASTO_OUTSIDE_CASTLE,
                                                       RegionName.BASTO_BUS_STOP_TOP)),
    LocationName.QUEST_BAD_HAIR_DAY: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            Has(ItemName.WATERGUN)),
    LocationName.QUEST_TAKE_A_NAP: LocationData(RegionName.BASTO_TENT, LocationGroup.QUEST),
    LocationName.QUEST_SPOOKY_STORIES: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            Has(ItemName.WATERGUN) & CanReachRegion(RegionName.BASTO_JUNGLE)),
    LocationName.QUEST_PORTRAITS: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.QUEST),
    LocationName.QUEST_CINEMA: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            Has(ItemName.WATERGUN)),
    LocationName.QUEST_NIGHT_LIGHTS: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            CanReachLocation(LocationName.COMP_FIRE_FLY)),
    LocationName.QUEST_JET_SKI: LocationData(RegionName.BASTO_LILY_PAD_POND_LEFT, LocationGroup.QUEST),
    LocationName.QUEST_FRUITS: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.QUEST,
            HasAll(ItemName.BANAKIN, ItemName.MELONEAR, ItemName.BEANUT, ItemName.ORANGANAS)),
    LocationName.QUEST_BRAIN_FREEZE: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST,
            Has(ItemName.ICE_CREAM, 4) & Has(ItemName.PICKAXE)),
    LocationName.QUEST_SWEET_TOOTH: LocationData(RegionName.BASTO_CAVE, LocationGroup.QUEST,
            Has(ItemName.ICE_CREAM, 4) & CanReachLocation(LocationName.QUEST_BATS)),
    LocationName.QUEST_IN_YOUR_FACE: LocationData(RegionName.BASTO_CASTLE, LocationGroup.QUEST,
            Has(ItemName.ICE_CREAM, 4)),
    LocationName.QUEST_BROKEN_DREAMS: LocationData(RegionName.BASTO_LILY_PAD_POND_LEFT, LocationGroup.QUEST,
            Has(ItemName.ICE_CREAM, 4) & Has(EventName.BASTO_LILY_PAD_POND_LEFT_DAY)),
    LocationName.QUEST_DRY_SEASON: LocationData(RegionName.BASTO_LILY_PAD_POND_LEFT, LocationGroup.QUEST,
            Has(ItemName.WATERGUN) & CanReachAllRegions(RegionName.BASTO_BUS_STOP_BOTTOM, RegionName.BASTO_CAMP,
                RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_CARNIVAL, RegionName.BASTO_JUNGLE,
                RegionName.BASTO_CAVE, RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_CASTLE,
                RegionName.BASTO_GYM_HOUSE)),
    LocationName.QUEST_MUSCLES: LocationData(RegionName.BASTO_GYM_HOUSE, LocationGroup.QUEST,
            Has(ItemName.EMPTY_BOTTLE) & CanReachAllRegions(RegionName.BASTO_GHOST_HANGOUT,
                RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_OUTSIDE_CASTLE)),
    LocationName.QUEST_SAND_CASTLE: LocationData(RegionName.BASTO_CASTLE, LocationGroup.QUEST,
            CanReachLocation(LocationName.QUEST_IN_YOUR_FACE)),
    LocationName.QUEST_CARNIVAL: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.QUEST,
            HasAny(ItemName.WATERGUN, ItemName.HONK_ATTACHMENT)),
    LocationName.QUEST_BATS: LocationData(RegionName.BASTO_CAVE, LocationGroup.QUEST,
            HasAny(ItemName.WATERGUN, ItemName.HONK_ATTACHMENT) & CanReachAllRegions(RegionName.BASTO_BONFIRE_TOP,
                                                                                     RegionName.BASTO_OUTSIDE_CASTLE)),
    LocationName.QUEST_BITLING: LocationData(RegionName.BASTO_JUNGLE, LocationGroup.QUEST,
            CanReachAllLocations(LocationName.COMP_BITLING_FROG, LocationName.COMP_BITLING_MOUSE,
                                 LocationName.COMP_BITLING_SNAIL, LocationName.COMP_BITLING_TATO)),
    LocationName.COMP_BAT: LocationData(RegionName.BAT, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNAKE: LocationData(RegionName.BASTO_CAMP, LocationGroup.COMPENDIUM),
    LocationName.COMP_BEAK_BIRD: LocationData(RegionName.BEAK_BIRD, LocationGroup.COMPENDIUM),
    LocationName.COMP_BITLING_FROG: LocationData(RegionName.BASTO_BONFIRE_BOTTOM, LocationGroup.COMPENDIUM),
    LocationName.COMP_BITLING_MOUSE: LocationData(RegionName.BASTO_CASTLE, LocationGroup.COMPENDIUM,
            CanReachLocation(LocationName.QUEST_IN_YOUR_FACE)),
    LocationName.COMP_BITLING_SNAIL: LocationData(RegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_BITLING_TATO: LocationData(RegionName.BITLING_TATO, LocationGroup.COMPENDIUM),
    LocationName.COMP_COCO_CRAB: LocationData(RegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_DAY_LIZARD: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_DRILL_MOLE: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_EGGERT: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_FIRE_FLY: LocationData(RegionName.BASTO_GHOST_HANGOUT, LocationGroup.COMPENDIUM),
    LocationName.COMP_GLOW_WORM: LocationData(RegionName.BASTO_CAVE, LocationGroup.COMPENDIUM),
    LocationName.COMP_ITSY_BITSY: LocationData(RegionName.BASTO_SECRET_CAVE, LocationGroup.COMPENDIUM),
    LocationName.COMP_MUD_FROG: LocationData(RegionName.BASTO_CAMP, LocationGroup.COMPENDIUM,
            Has(EventName.BASTO_CAMP_NIGHT)),
    LocationName.COMP_NIGHT_LIZARD: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNOUT_BUG: LocationData(RegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_COCO: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.COMPENDIUM,
            Has(ItemName.WATERGUN)),
    LocationName.COMP_TATO_KING: LocationData(RegionName.BASTO_SECRET_CAVE, LocationGroup.COMPENDIUM,
            Has(ItemName.WATERGUN)),
    LocationName.COMP_WATER_STRIDER: LocationData(RegionName.WATER_STRIDER, LocationGroup.COMPENDIUM),
    LocationName.ITEM_BASTO_TICKET: LocationData(RegionName.HOMELANDA_LIVING_ROOM, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_EXPERIENCE_TOEM)),
    LocationName.ITEM_WATERGUN: LocationData(RegionName.BASTO_BUS_STOP_BOTTOM, LocationGroup.ITEM),
    LocationName.ITEM_SUN_HAT: LocationData(RegionName.BASTO_TENT, LocationGroup.ITEM),
    LocationName.ITEM_MELONEAR: LocationData(RegionName.BASTO_LILY_PAD_POND_RIGHT, LocationGroup.ITEM,
            Has(ItemName.WATERGUN)),
    LocationName.ITEM_BANAKIN: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            Has(ItemName.WATERGUN)),
    LocationName.ITEM_ORANGANAS: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM,
            Has(ItemName.WATERGUN)),
    LocationName.ITEM_BEANUT: LocationData(RegionName.BASTO_CAMP, LocationGroup.ITEM,
            HasAll(ItemName.WATERGUN, EventName.BASTO_CAMP_DAY)),
    LocationName.ITEM_PICKAXE: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM),
    LocationName.ITEM_SUN_CAP: LocationData(RegionName.BASTO_CAVE, LocationGroup.ITEM,
            Has(ItemName.PICKAXE)),
    LocationName.ITEM_FLIP_FLOPS: LocationData(RegionName.BASTO_GHOST_HANGOUT, LocationGroup.ITEM,
            Has(ItemName.PICKAXE)),
    LocationName.ITEM_ICE_CREAM_BANAKIN: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            Has(ItemName.BANAKIN)),
    LocationName.ITEM_ICE_CREAM_MELONEAR: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            Has(ItemName.MELONEAR)),
    LocationName.ITEM_ICE_CREAM_BEANUT: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            Has(ItemName.BEANUT)),
    LocationName.ITEM_ICE_CREAM_ORANGANAS: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            Has(ItemName.ORANGANAS)),
    LocationName.ITEM_ROYAL_CAPE: LocationData(RegionName.BASTO_CASTLE, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_SAND_CASTLE)),
    LocationName.ITEM_MINIGAME_TICKET: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.ITEM,
            HasAny(ItemName.WATERGUN, ItemName.HONK_ATTACHMENT)),
    LocationName.ITEM_LEI: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.ITEM,
            Has(ItemName.MINIGAME_TICKET)),
    LocationName.ITEM_VACATION_SHIRT: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.ITEM,
            Has(ItemName.MINIGAME_TICKET)),
    LocationName.ITEM_ROYAL_CANE: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.ITEM,
            Has(ItemName.MINIGAME_TICKET)),
    LocationName.ITEM_EMPTY_BOTTLE: LocationData(RegionName.BASTO_GHOST_HANGOUT, LocationGroup.ITEM),
    LocationName.ITEM_VIKING_HELMET: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_BRAIN_FREEZE)),
    LocationName.ITEM_FOOT_CAST: LocationData(RegionName.BASTO_LILY_PAD_POND_LEFT, LocationGroup.ITEM,
            CanReachLocation(LocationName.QUEST_BROKEN_DREAMS)),
    LocationName.ITEM_BERET: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM,
            CanReachAllLocations(*portrait_locations)),
    LocationName.ITEM_ROYAL_CROWN: LocationData(RegionName.BASTO_CASTLE, LocationGroup.ITEM,
            Has(ItemName.PICKAXE) & CanReachLocation(LocationName.COMP_TATO_KING)),
    LocationName.TAPE_NIGHT_JAM: LocationData(RegionName.BASTO_CAMP, LocationGroup.CASSETTE,
            CanReachLocation(LocationName.QUEST_TAKE_A_NAP)),
    LocationName.TAPE_WARM_DAYS_NIGHT: LocationData(RegionName.BASTO_CAMP, LocationGroup.CASSETTE,
            CanReachLocation(LocationName.QUEST_TAKE_A_NAP)),
    LocationName.TAPE_ONE_BY_ONE: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.CASSETTE,
            Has(ItemName.WATERGUN)),
    LocationName.TAPE_HAMMOCK_DAYS: LocationData(RegionName.BASTO_JUNGLE, LocationGroup.CASSETTE,
            Has(ItemName.WATERGUN)),
    LocationName.TAPE_SAILORS_TUNE: LocationData(RegionName.BASTO_BUS_STOP_BOTTOM, LocationGroup.CASSETTE,
            bonfire_rule),
    LocationName.TAPE_SONG_OF_THE_SEA: LocationData(RegionName.BASTO_BUS_STOP_BOTTOM, LocationGroup.CASSETTE,
            Has(ItemName.WATERGUN)),
    LocationName.CHEEVO_TOPICAL_PARADISE: LocationData(RegionName.BASTO, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_MAXIMUM_VACATION: LocationData(RegionName.MAXIMUM_VACATION, LocationGroup.ACHIEVEMENT,
            HasAll(ItemName.VACATION_SHIRT, ItemName.FLIP_FLOPS, ItemName.SUN_HAT)),
    LocationName.CHEEVO_KINGS_SHIRT: LocationData(RegionName.BASTO_CASTLE, LocationGroup.ACHIEVEMENT,
            Has(ItemName.ROYAL_CAPE)),
    LocationName.CHEEVO_MOONLIT_BEAUTY: LocationData(RegionName.BASTO_BONFIRE_TOP, LocationGroup.ACHIEVEMENT,
            CanReachLocation(LocationName.QUEST_BAD_HAIR_DAY)),
    LocationName.CHEEVO_SELF_PORTRAIT: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_WAZZUUPPP: LocationData(RegionName.BASTO, LocationGroup.ACHIEVEMENT,
            Has(ItemName.FRAMES_FILTERS) & (
                HasAny(EventName.BASTO_LILY_PAD_POND_LEFT_NIGHT, EventName.BASTO_CAMP_NIGHT) |
                CanReachAnyRegion(RegionName.BASTO_LILY_PAD_POND_RIGHT, RegionName.BASTO_OUTSIDE_CASTLE,
                    RegionName.BASTO_BONFIRE_TOP, RegionName.BASTO_GHOST_HANGOUT, RegionName.BASTO_JUNGLE)
            )), # FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, EventName.BASTO_BONFIRE_BOTTOM_NIGHT  # noqa: E501
    LocationName.CHEEVO_PRO_GAMER: LocationData(RegionName.BASTO_CARNIVAL, LocationGroup.ACHIEVEMENT,
            HasAll(ItemName.WATERGUN, ItemName.HONK_ATTACHMENT)),
    LocationName.CHEEVO_SPLISH_SPLASH: LocationData(RegionName.BASTO_GHOST_HANGOUT, LocationGroup.ACHIEVEMENT,
            Has(ItemName.WATERGUN) & CanReachLocation(LocationName.QUEST_TAKE_A_BATH)),
    LocationName.CHEEVO_ROYAL_CASTLE: LocationData(RegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SOME_MORE: LocationData(RegionName.BASTO, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*basto_animals)),
    LocationName.CHEEVO_VIKINGS_HOLIDAY: LocationData(RegionName.BASTO, LocationGroup.ACHIEVEMENT,
            CanReachAllLocations(*basto_quests)),
}

location_to_item_name: dict[str, str] = {
    LocationName.ITEM_CLOGS: ItemName.CLOGS,
    LocationName.ITEM_AWARD_MASK: ItemName.AWARD_MASK,
    LocationName.ITEM_FINGER: ItemName.FINGER,
    LocationName.ITEM_TRIPOD: ItemName.TRIPOD,
    LocationName.ITEM_COWBOY_HAT: ItemName.COWBOY_HAT,
    LocationName.ITEM_WET_SOCKS: ItemName.WET_SOCKS,
    LocationName.ITEM_FJALLBJORN_HAT: ItemName.FJALLBJORN_HAT,
    LocationName.ITEM_GHOST_GLASSES: ItemName.GHOST_GLASSES,
    LocationName.ITEM_SOAKED_SOCK: ItemName.SOAKED_SOCK,
    LocationName.ITEM_MONSTER_MASK: ItemName.MONSTER_MASK,
    LocationName.ITEM_FRAMES_FILTERS: ItemName.FRAMES_FILTERS,
    LocationName.ITEM_FISHING_HAT: ItemName.FISHING_HAT,
    LocationName.ITEM_HONK_ATTACHMENT: ItemName.HONK_ATTACHMENT,
    LocationName.ITEM_UMBRELLA: ItemName.UMBRELLA,
    LocationName.ITEM_OLD_KEY: ItemName.OLD_KEY,
    LocationName.ITEM_HARD_HAT: ItemName.HARD_HAT,
    LocationName.ITEM_DIVING_HELMET: ItemName.DIVING_HELMET,
    LocationName.ITEM_RUBBER_BOOTS: ItemName.RUBBER_BOOTS,
    LocationName.ITEM_SANDWICH: ItemName.SANDWICH,
    LocationName.ITEM_PIRATE_HAT: ItemName.PIRATE_HAT,
    LocationName.ITEM_PAPER_HAT: ItemName.PAPER_HAT,
    LocationName.ITEM_FLAG: ItemName.FLAG,
    LocationName.ITEM_HOTBEAN_HAT: ItemName.HOTBEAN_HAT,
    LocationName.ITEM_REPORTER_HAT: ItemName.REPORTER_HAT,
    LocationName.ITEM_SNEAKERS: ItemName.SNEAKERS,
    LocationName.ITEM_CINNAMON_BUN: ItemName.CINNAMON_BUN,
    LocationName.ITEM_FRISBEE: ItemName.FRISBEE,
    LocationName.ITEM_CLIMBING_BOOTS: ItemName.CLIMBING_BOOTS,
    LocationName.ITEM_PUFFER_HAT: ItemName.PUFFER_HAT,
    LocationName.ITEM_SCARF: ItemName.SCARF,
    LocationName.ITEM_SKI_GOGGLES: ItemName.SKI_GOGGLES,
    LocationName.ITEM_SPACE_HELMET: ItemName.SPACE_HELMET,
    LocationName.ITEM_BASTO_TICKET: ItemName.BASTO_TICKET,
    LocationName.ITEM_WATERGUN: ItemName.WATERGUN,
    LocationName.ITEM_SUN_HAT: ItemName.SUN_HAT,
    LocationName.ITEM_MELONEAR: ItemName.MELONEAR,
    LocationName.ITEM_BANAKIN: ItemName.BANAKIN,
    LocationName.ITEM_ORANGANAS: ItemName.ORANGANAS,
    LocationName.ITEM_BEANUT: ItemName.BEANUT,
    LocationName.ITEM_PICKAXE: ItemName.PICKAXE,
    LocationName.ITEM_SUN_CAP: ItemName.SUN_CAP,
    LocationName.ITEM_FLIP_FLOPS: ItemName.FLIP_FLOPS,
    LocationName.ITEM_ICE_CREAM_BANAKIN: ItemName.ICE_CREAM,
    LocationName.ITEM_ICE_CREAM_MELONEAR: ItemName.ICE_CREAM,
    LocationName.ITEM_ICE_CREAM_BEANUT: ItemName.ICE_CREAM,
    LocationName.ITEM_ICE_CREAM_ORANGANAS: ItemName.ICE_CREAM,
    LocationName.ITEM_ROYAL_CAPE: ItemName.ROYAL_CAPE,
    LocationName.ITEM_MINIGAME_TICKET: ItemName.MINIGAME_TICKET,
    LocationName.ITEM_LEI: ItemName.LEI,
    LocationName.ITEM_VACATION_SHIRT: ItemName.VACATION_SHIRT,
    LocationName.ITEM_ROYAL_CANE: ItemName.ROYAL_CANE,
    LocationName.ITEM_EMPTY_BOTTLE: ItemName.EMPTY_BOTTLE,
    LocationName.ITEM_VIKING_HELMET: ItemName.VIKING_HELMET,
    LocationName.ITEM_FOOT_CAST: ItemName.FOOT_CAST,
    LocationName.ITEM_BERET: ItemName.BERET,
    LocationName.ITEM_ROYAL_CROWN: ItemName.ROYAL_CROWN,
    LocationName.TAPE_PHOTO_OF_HOME: ItemName.PHOTO_OF_HOME_TAPE,
    LocationName.TAPE_SUMMER_BREEZE: ItemName.SUMMER_BREEZE_TAPE,
    LocationName.TAPE_SQUIRREL_HOTEL: ItemName.SQUIRREL_HOTEL_TAPE,
    LocationName.TAPE_PINE_NEEDLES: ItemName.PINE_NEEDLES_TAPE,
    LocationName.TAPE_SQUIRREL_PHOTO: ItemName.SQUIRREL_PHOTO_TAPE,
    LocationName.TAPE_FISHERMANS_WHISTLE: ItemName.FISHERMANS_WHISTLE_TAPE,
    LocationName.TAPE_SMILING_HUNTSMAN: ItemName.SMILING_HUNTSMAN_TAPE,
    LocationName.TAPE_NAUT: ItemName.NAUT_TAPE,
    LocationName.TAPE_PLACE_IN_SUN: ItemName.PLACE_IN_SUN_TAPE,
    LocationName.TAPE_FISHERMANS_TUNE: ItemName.FISHERMANS_TUNE_TAPE,
    LocationName.TAPE_RATSKULLZ_THEME: ItemName.RATSKULLZ_THEME_TAPE,
    LocationName.TAPE_BIG_CITY: ItemName.BIG_CITY_TAPE,
    LocationName.TAPE_HUSTLE_BUSTLE: ItemName.HUSTLE_BUSTLE_TAPE,
    LocationName.TAPE_HOP_SKIP_STEP: ItemName.HOP_SKIP_STEP_TAPE,
    LocationName.TAPE_ON_THE_HOUR: ItemName.ON_THE_HOUR_TAPE,
    LocationName.TAPE_LIFE_THROUGH_LENS: ItemName.LIFE_THROUGH_LENS_TAPE,
    LocationName.TAPE_PETTING_DEER: ItemName.PETTING_DEER_TAPE,
    LocationName.TAPE_STORIES_OF_SNOW: ItemName.STORIES_OF_SNOW_TAPE,
    LocationName.TAPE_TALL_SHY: ItemName.TALL_SHY_TAPE,
    LocationName.TAPE_NIGHT_JAM: ItemName.NIGHT_JAM_TAPE,
    LocationName.TAPE_WARM_DAYS_NIGHT: ItemName.WARM_DAYS_NIGHT_TAPE,
    LocationName.TAPE_ONE_BY_ONE: ItemName.ONE_BY_ONE_TAPE,
    LocationName.TAPE_HAMMOCK_DAYS: ItemName.HAMMOCK_DAYS_TAPE,
    LocationName.TAPE_SAILORS_TUNE: ItemName.SAILORS_TUNE_TAPE,
    LocationName.TAPE_SONG_OF_THE_SEA: ItemName.SONG_OF_THE_SEA_TAPE,
}

location_name_to_id: dict[str, int] = {name: i for i, name in enumerate(location_table, start=1)}


def get_location_group(location_name: str) -> str:
    return location_table[location_name].group


def get_location_area(location_name: str) -> str:
    return location_table[location_name].region.split(" - ")[0]


location_name_groups: dict[str, set[str]] = {
    group: set(location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
location_name_groups.update({
    group: set(item_names)
    for group, item_names in groupby(sorted(location_table, key=get_location_area), get_location_area)
    if group in gameplay_areas
})

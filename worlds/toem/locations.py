from dataclasses import dataclass
from itertools import groupby
from typing import final, Tuple

from BaseClasses import Location

from .constants import GAME_NAME
from .regions import FullRegionName
from .items import ItemName


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
    requirements: Tuple[str] = ()

oaklaville_quests = (
    LocationName.QUEST_SUS_FOREST, LocationName.QUEST_MONSTERS, LocationName.QUEST_SOCKS, LocationName.QUEST_SCOUTS, 
    LocationName.QUEST_HIDE_AND_SEEK, LocationName.QUEST_LOG_JAM, LocationName.QUEST_CHALLENGE_1, LocationName.QUEST_CHALLENGE_2, 
    LocationName.QUEST_PAPARAZZI, LocationName.QUEST_CAPTURE_HOTEL, LocationName.QUEST_HOTEL_CHEF, LocationName.QUEST_STALLION, 
    LocationName.QUEST_GHOST_HELPER, LocationName.QUEST_CUP_CHAMP, LocationName.QUEST_FLOWER
)
oaklaville_regions = (
    FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, FullRegionName.OAKLAVILLE_HOTEL, 
    FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, 
    FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, FullRegionName.OAKLAVILLE_GRAVEYARD, FullRegionName.OAKLAVILLE_SKELETON_HOUSE, 
    FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_TRAIL, 
    FullRegionName.OAKLAVILLE_LOOKOUT, FullRegionName.OAKLAVILLE_PLAYGROUND, FullRegionName.OAKLAVILLE_OUTSIDE_RAVE, 
    FullRegionName.OAKLAVILLE_RAVE
)
stanhamn_quests = (
    LocationName.QUEST_KING_FISH, LocationName.QUEST_GOOD_SPOT, LocationName.QUEST_SUS_HARBOR, LocationName.QUEST_PAPER_HATS, 
    LocationName.QUEST_CHALLENGE_3, LocationName.QUEST_CHALLENGE_4, LocationName.QUEST_FRAMES_FILTERS, LocationName.QUEST_TAKE_A_BATH, 
    LocationName.QUEST_LOST_DOG, LocationName.QUEST_POWER, LocationName.QUEST_CHAOS, LocationName.QUEST_FLAME, LocationName.QUEST_SANDWICH, 
    LocationName.QUEST_GARBAGE, LocationName.QUEST_WHISTLING, LocationName.QUEST_MELODY
)
stanhamn_regions = (
    FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_PHOTO_GUILD_HUT, FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, 
    FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_UNDERWATER, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, 
    FullRegionName.STANHAMN_LIGHTHOUSE, FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, FullRegionName.STANHAMN_KING_FISH_BEACH, 
    FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.STANHAMN_DOCKS_RIGHT, FullRegionName.STANHAMN_FISHING_TOWER, 
    FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, 
    FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, FullRegionName.STANHAMN_HYDROPLANT
)
logcity_quests = (
    LocationName.QUEST_RATSKULLZ, LocationName.QUEST_PUNK_ROCKER, LocationName.QUEST_CHALLENGE_5, LocationName.QUEST_CHALLENGE_6, 
    LocationName.QUEST_NEWS, LocationName.QUEST_SEWER, LocationName.QUEST_HOTBEAN, LocationName.QUEST_HANG_IN_THERE, 
    LocationName.QUEST_SCARY_CITY, LocationName.QUEST_DATE, LocationName.QUEST_ART, LocationName.QUEST_INFLUENCER, 
    LocationName.QUEST_FASHION, LocationName.QUEST_CLEANING, LocationName.QUEST_GRANNY, LocationName.QUEST_MICE, LocationName.QUEST_CROW
)
logcity_regions = (
    FullRegionName.LOGCITY_BUS_STOP, FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_CROSSWALK, FullRegionName.LOGCITY_OVERPASS,
    FullRegionName.LOGCITY_NEWS_HOUSE, FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_RATSKULLZ_ALLEY, 
    FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_FASHION_SHOW, FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, 
    FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_CAFE, FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_GALLERY
)
kiiruberg_quests = (
    LocationName.QUEST_YETI_CUTE, LocationName.QUEST_ICE_WIZARD, LocationName.QUEST_MILITARY_SUS, LocationName.QUEST_ASTRONAUT, 
    LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8, LocationName.QUEST_ASTEROID, LocationName.QUEST_GOAT_CHOIR, 
    LocationName.QUEST_SNOWBALL, LocationName.QUEST_BIRTHDAY, LocationName.QUEST_PAINTINGS, LocationName.QUEST_BECOME_YETI, LocationName.QUEST_SNOWMAN
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
dev_animals = (
    LocationName.COMP_OSKAR, LocationName.COMP_SERO, LocationName.COMP_PET_ROCK, LocationName.COMP_FIA, LocationName.COMP_FRAS, 
    LocationName.COMP_WILLEMIJN, LocationName.COMP_PORTILLO, LocationName.COMP_MIKEE, LocationName.COMP_NARIKO, LocationName.COMP_TEDDY
)
base_animals = (
    LocationName.COMP_COW, LocationName.COMP_FLIES, LocationName.COMP_HOME_BIRD, LocationName.COMP_TATO, LocationName.COMP_ANT, 
    LocationName.COMP_BEEHIVE, LocationName.COMP_BUTTERFLY, LocationName.COMP_OSKAR, LocationName.COMP_SERO, LocationName.COMP_FOREST_BIRD, 
    LocationName.COMP_LADYBUG, LocationName.COMP_TOM, LocationName.COMP_NESTWORM, LocationName.COMP_PET_ROCK, LocationName.COMP_SNAIL, 
    LocationName.COMP_SQUIRREL, LocationName.COMP_STAG_BEETLE, LocationName.COMP_TATO_BUG, LocationName.COMP_TATO_FLY, 
    LocationName.COMP_BUBBLE_FLY, LocationName.COMP_FIA, LocationName.COMP_FRAS, LocationName.COMP_WILLEMIJN, LocationName.COMP_CRAB, 
    LocationName.COMP_DRAGONFLY, LocationName.COMP_HAPPY_CARP, LocationName.COMP_JELLYFISH, LocationName.COMP_KING_FISH, 
    LocationName.COMP_SEAGULL, LocationName.COMP_SEAHORSE, LocationName.COMP_SUNDAY_SWAN, LocationName.COMP_TATO_SCUBA, 
    LocationName.COMP_TATO_SWIM, LocationName.COMP_TOAD, LocationName.COMP_BUSINESS_PIGEON, LocationName.COMP_PORTILLO, 
    LocationName.COMP_MOUSE, LocationName.COMP_PIGEON, LocationName.COMP_PUNK_PARROT, LocationName.COMP_TATO_SKATEBOARD, 
    LocationName.COMP_TATO_TOURIST, LocationName.COMP_TURTLE, LocationName.COMP_MIKEE, LocationName.COMP_NARIKO, 
    LocationName.COMP_COSMO_DEER, LocationName.COMP_TEDDY, LocationName.COMP_FLUFF, LocationName.COMP_HEDGEHOG, 
    LocationName.COMP_METEOPAL, LocationName.COMP_GOAT, LocationName.COMP_OWL, LocationName.COMP_SNOW_BIRD, 
    LocationName.COMP_TATO_ALIEN, LocationName.COMP_TATO_SKI
)
clothing_items = (
    ItemName.CLOGS, ItemName.FINGER, ItemName.GHOST_GLASSES, ItemName.SOAKED_SOCK, ItemName.FJALLBJORN_HAT, ItemName.COWBOY_HAT, 
    ItemName.FISHING_HAT, ItemName.UMBRELLA, ItemName.HARD_HAT, ItemName.DIVING_HELMET, ItemName.PIRATE_HAT, ItemName.PAPER_HAT, 
    ItemName.RUBBER_BOOTS, ItemName.HOTBEAN_HAT, ItemName.REPORTER_HAT, ItemName.SNEAKERS, ItemName.CLIMBING_BOOTS, 
    ItemName.SCARF, ItemName.PUFFER_HAT, ItemName.SKI_GOGGLES, ItemName.MONSTER_MASK, ItemName.FLAG, ItemName.SPACE_HELMET
)
completionist_reqs = (
    LocationName.QUEST_PHOTO_OF_NANA, LocationName.QUEST_HIDDEN_GIFT, LocationName.QUEST_EXPERIENCE_TOEM, 
    LocationName.CHEEVO_STRONG_AS_AN_OAK, LocationName.CHEEVO_SEAWORTHY, LocationName.CHEEVO_BUSINESS, LocationName.CHEEVO_FIGHTER
)
warm_clothes = (ItemName.CLIMBING_BOOTS, ItemName.PUFFER_HAT, ItemName.SCARF, ItemName.SKI_GOGGLES)
photo_challenges = (
    LocationName.QUEST_CHALLENGE_1, LocationName.QUEST_CHALLENGE_2, LocationName.QUEST_CHALLENGE_3, LocationName.QUEST_CHALLENGE_4, 
    LocationName.QUEST_CHALLENGE_5, LocationName.QUEST_CHALLENGE_6, LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8
)
basto_animals = (
    LocationName.COMP_BAT, LocationName.COMP_SNAKE, LocationName.COMP_BEAK_BIRD, LocationName.COMP_BITLING_FROG, 
    LocationName.COMP_BITLING_MOUSE, LocationName.COMP_BITLING_SNAIL, LocationName.COMP_BITLING_TATO, LocationName.COMP_COCO_CRAB, 
    LocationName.COMP_DAY_LIZARD, LocationName.COMP_DRILL_MOLE, LocationName.COMP_EGGERT, LocationName.COMP_FIRE_FLY, 
    LocationName.COMP_GLOW_WORM, LocationName.COMP_ITSY_BITSY, LocationName.COMP_MUD_FROG, LocationName.COMP_NIGHT_LIZARD, 
    LocationName.COMP_SNOUT_BUG, LocationName.COMP_TATO_COCO, LocationName.COMP_TATO_KING, LocationName.COMP_WATER_STRIDER
)
basto_quests = (
    LocationName.QUEST_BALLOONS, LocationName.QUEST_ARTHUR, LocationName.QUEST_BAD_HAIR_DAY, LocationName.QUEST_TAKE_A_NAP, 
    LocationName.QUEST_SPOOKY_STORIES, LocationName.QUEST_PORTRAITS, LocationName.QUEST_CINEMA, LocationName.QUEST_NIGHT_LIGHTS, 
    LocationName.QUEST_JET_SKI, LocationName.QUEST_FRUITS, LocationName.QUEST_BRAIN_FREEZE, LocationName.QUEST_SWEET_TOOTH, 
    LocationName.QUEST_IN_YOUR_FACE, LocationName.QUEST_BROKEN_DREAMS, LocationName.QUEST_DRY_SEASON, LocationName.QUEST_MUSCLES, 
    LocationName.QUEST_SAND_CASTLE, LocationName.QUEST_CARNIVAL, LocationName.QUEST_BATS, LocationName.QUEST_BITLING
)
basto_regions = (
    FullRegionName.BASTO_BUS_STOP_TOP_DAY, FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, 
    FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, 
    FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_CAMP_DAY, FullRegionName.BASTO_CAMP_NIGHT, FullRegionName.BASTO_TENT, 
    FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT, FullRegionName.BASTO_GYM_HOUSE, 
    FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_BONFIRE_BOTTOM_DAY, FullRegionName.BASTO_BONFIRE_BOTTOM_NIGHT, 
    FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT, FullRegionName.BASTO_GHOST_HANGOUT, 
    FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT, FullRegionName.BASTO_SECRET_CAVE_DAY, 
    FullRegionName.BASTO_SECRET_CAVE_NIGHT, FullRegionName.BASTO_JUNGLE
)

location_table: dict[str, LocationData] = {
    LocationName.QUEST_PHOTO_OF_NANA: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.QUEST),
    LocationName.QUEST_HIDDEN_GIFT: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.QUEST, (ItemName.CLOGS,)),
    LocationName.QUEST_EXPERIENCE_TOEM: LocationData(FullRegionName.HOMELANDA_LIVING_ROOM, LocationGroup.QUEST, (ItemName.CLIMBING_BOOTS, FullRegionName.MOUNTAIN_TOP_TOEM)),
    LocationName.COMP_COW: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_FLIES: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_HOME_BIRD: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.ITEM_CLOGS: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.ITEM),
    LocationName.ITEM_AWARD_MASK: LocationData(FullRegionName.HOMELANDA_PLAYER_ROOM, LocationGroup.ITEM, (ItemName.HONK_ATTACHMENT,)),
    LocationName.TAPE_PHOTO_OF_HOME: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.CHEEVO_BEGINNING: LocationData(FullRegionName.HOMELANDA_LIVING_ROOM, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_HOME_SWEET_HOME: LocationData(FullRegionName.HOMELANDA_BUS_STOP, LocationGroup.ACHIEVEMENT),
    LocationName.QUEST_SUS_FOREST: LocationData(FullRegionName.OAKLAVILLE_TRAIL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_HIDE_AND_SEEK,)),
    LocationName.QUEST_MONSTERS: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST, (ItemName.TRIPOD, ItemName.HONK_ATTACHMENT, FullRegionName.OAKLAVILLE_PLAYGROUND, FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.KIIRUBERG_BLIZZARD_MONSTER)),
    LocationName.QUEST_SOCKS: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.QUEST, (ItemName.WET_SOCKS,)),
    LocationName.QUEST_SCOUTS: LocationData(FullRegionName.OAKLAVILLE_CAMP, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_LOOKOUT, FullRegionName.OAKLAVILLE_BUS_STOP, (FullRegionName.OAKLAVILLE_PLAYGROUND, FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE))),
    LocationName.QUEST_HIDE_AND_SEEK: LocationData(FullRegionName.OAKLAVILLE_HIDE_AND_SEEK, LocationGroup.QUEST),
    LocationName.QUEST_LOG_JAM: LocationData(FullRegionName.OAKLAVILLE_TRAIL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_CAMP, FullRegionName.OAKLAVILLE_BUS_STOP, FullRegionName.OAKLAVILLE_HOTEL)),
    LocationName.QUEST_CHALLENGE_1: LocationData(FullRegionName.OAKLAVILLE_TRAIL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_CAMP,)),
    LocationName.QUEST_CHALLENGE_2: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_TRAIL,)),
    LocationName.QUEST_PAPARAZZI: LocationData(FullRegionName.OAKLAVILLE_RAVE, LocationGroup.QUEST),
    LocationName.QUEST_CAPTURE_HOTEL: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_LOOKOUT,)),
    LocationName.QUEST_HOTEL_CHEF: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_LOOKOUT,)),
    LocationName.QUEST_STALLION: LocationData(FullRegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.QUEST, (FullRegionName.OAKLAVILLE_HOTEL, ItemName.GHOST_GLASSES)),
    LocationName.QUEST_GHOST_HELPER: LocationData(FullRegionName.OAKLAVILLE_SKELETON_HOUSE, LocationGroup.QUEST, (LocationName.QUEST_CUP_CHAMP, LocationName.QUEST_STALLION, LocationName.QUEST_SANDWICH, LocationName.QUEST_FLAME, LocationName.QUEST_DATE, LocationName.QUEST_SCARY_CITY)),
    LocationName.QUEST_CUP_CHAMP: LocationData(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, LocationGroup.QUEST, (ItemName.GHOST_GLASSES,)),
    LocationName.QUEST_FLOWER: LocationData(FullRegionName.OAKLAVILLE_PLAYGROUND, LocationGroup.QUEST),
    LocationName.COMP_ANT: LocationData(FullRegionName.OAKLAVILLE_TRAIL, LocationGroup.COMPENDIUM),
    LocationName.COMP_BEEHIVE: LocationData(FullRegionName.OAKLAVILLE_PLAYGROUND, LocationGroup.COMPENDIUM),
    LocationName.COMP_BUTTERFLY: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_OSKAR: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_SERO: LocationData(FullRegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.COMPENDIUM),
    LocationName.COMP_FOREST_BIRD: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_LADYBUG: LocationData(FullRegionName.OAKLAVILLE_CAMP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TOM: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_NESTWORM: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_PET_ROCK: LocationData(FullRegionName.OAKLAVILLE_CAMP, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNAIL: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_SQUIRREL: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_HOTEL_ELEVATOR),)),
    LocationName.COMP_STAG_BEETLE: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_BUG: LocationData(FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_FLY: LocationData(FullRegionName.OAKLAVILLE_SKELETON_HOUSE_BALCONY, LocationGroup.COMPENDIUM),
    LocationName.ITEM_FINGER: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ITEM),
    LocationName.ITEM_TRIPOD: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (photo_challenges,)),
    LocationName.ITEM_COWBOY_HAT: LocationData(FullRegionName.OAKLAVILLE_MUSHROOM_HOUSE, LocationGroup.ITEM),
    LocationName.ITEM_WET_SOCKS: LocationData(FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, LocationGroup.ITEM, (LocationName.QUEST_CUP_CHAMP,)),
    LocationName.ITEM_FJALLBJORN_HAT: LocationData(FullRegionName.OAKLAVILLE_CAMP, LocationGroup.ITEM, (LocationName.QUEST_SCOUTS,)),
    LocationName.ITEM_GHOST_GLASSES: LocationData(FullRegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.ITEM),
    LocationName.ITEM_SOAKED_SOCK: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ITEM, (LocationName.QUEST_SOCKS,)),
    LocationName.ITEM_MONSTER_MASK: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.ITEM, (LocationName.QUEST_MONSTERS,)),
    LocationName.TAPE_SUMMER_BREEZE: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_SQUIRREL_HOTEL: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_PINE_NEEDLES: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_SQUIRREL_PHOTO: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.CHEEVO_CALM_FOREST: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (oaklaville_regions,)),
    LocationName.CHEEVO_MAJESTIC_HOTEL: LocationData(FullRegionName.OAKLAVILLE_LOOKOUT, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SLOW_AND_STEADY: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_NATURE_SHOWSTOPPER: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_CHALLENGE_1, LocationName.QUEST_CHALLENGE_2)),
    LocationName.CHEEVO_STRONG_AS_AN_OAK: LocationData(FullRegionName.OAKLAVILLE_BUS_STOP, LocationGroup.ACHIEVEMENT, oaklaville_quests),
    LocationName.CHEEVO_CALMED_DOWN: LocationData(FullRegionName.OAKLAVILLE_GRAVEYARD, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_JUST_A_SOCK: LocationData(FullRegionName.OAKLAVILLE_OUTSIDE_HOTEL, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_SOCKS,)),
    LocationName.CHEEVO_YOU_FOUND_US: LocationData(FullRegionName.OAKLAVILLE_HOTEL, LocationGroup.ACHIEVEMENT),
    LocationName.QUEST_KING_FISH: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.QUEST, (LocationName.COMP_KING_FISH,)),
    LocationName.QUEST_GOOD_SPOT: LocationData(FullRegionName.STANHAMN_HIPPO_BEACH, LocationGroup.QUEST),
    LocationName.QUEST_SUS_HARBOR: LocationData(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, LocationGroup.QUEST, (FullRegionName.STANHAMN_BUS_STOP,)),
    LocationName.QUEST_PAPER_HATS: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.QUEST, (ItemName.HONK_ATTACHMENT, ItemName.PIRATE_HAT)),
    LocationName.QUEST_CHALLENGE_3: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.QUEST, (FullRegionName.STANHAMN_HIPPO_BEACH,)),
    LocationName.QUEST_CHALLENGE_4: LocationData(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_TOP, LocationGroup.QUEST, (FullRegionName.STANHAMN_HIPPO_BEACH,)),
    LocationName.QUEST_FRAMES_FILTERS: LocationData(FullRegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.QUEST, (ItemName.FRAMES_FILTERS,)),
    LocationName.QUEST_TAKE_A_BATH: LocationData(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.QUEST, (ItemName.HONK_ATTACHMENT, FullRegionName.STANHAMN_HYDROPLANT)),
    LocationName.QUEST_LOST_DOG: LocationData(FullRegionName.STANHAMN_DOCKS_RIGHT, LocationGroup.QUEST, (FullRegionName.STANHAMN_HIPPO_BEACH,)),
    LocationName.QUEST_POWER: LocationData(FullRegionName.STANHAMN_HYDROPLANT, LocationGroup.QUEST),
    LocationName.QUEST_CHAOS: LocationData(FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, LocationGroup.QUEST, (FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE, FullRegionName.STANHAMN_LIGHTHOUSE)),
    LocationName.QUEST_FLAME: LocationData(FullRegionName.STANHAMN_GHOST_DRAWBRIDGE_BOTTOM, LocationGroup.QUEST, (ItemName.GHOST_GLASSES,)),
    LocationName.QUEST_SANDWICH: LocationData(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.QUEST, (ItemName.GHOST_GLASSES, ItemName.SANDWICH)),
    LocationName.QUEST_GARBAGE: LocationData(FullRegionName.STANHAMN_FISHING_TOWER, LocationGroup.QUEST),
    LocationName.QUEST_WHISTLING: LocationData(FullRegionName.STANHAMN_DOCKS_LEFT, LocationGroup.QUEST, (FullRegionName.STANHAMN_BUS_STOP,)),
    LocationName.QUEST_MELODY: LocationData(FullRegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.QUEST, (ItemName.FISHERMANS_WHISTLE_TAPE,)),
    LocationName.COMP_BUBBLE_FLY: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.COMPENDIUM),
    LocationName.COMP_FIA: LocationData(FullRegionName.STANHAMN_DOCKS_RIGHT, LocationGroup.COMPENDIUM),
    LocationName.COMP_FRAS: LocationData(FullRegionName.STANHAMN_DOCKS_LEFT, LocationGroup.COMPENDIUM),
    LocationName.COMP_WILLEMIJN: LocationData(FullRegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.COMPENDIUM),
    LocationName.COMP_CRAB: LocationData(FullRegionName.STANHAMN_HIPPO_BEACH, LocationGroup.COMPENDIUM),
    LocationName.COMP_DRAGONFLY: LocationData(FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT, LocationGroup.COMPENDIUM),
    LocationName.COMP_HAPPY_CARP: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_JELLYFISH: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_KING_FISH: LocationData(FullRegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.COMPENDIUM, (LocationName.QUEST_MELODY,)),
    LocationName.COMP_SEAGULL: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.STANHAMN_BUS_STOP, FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.STANHAMN_OUTSIDE_LIGHTHOUSE),)),
    LocationName.COMP_SEAHORSE: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_SUNDAY_SWAN: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, (FullRegionName.STANHAMN_DOCKS_LEFT, FullRegionName.STANHAMN_DOCKS_RIGHT)),
    LocationName.COMP_TATO_SCUBA: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_SWIM: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_TOAD: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.COMPENDIUM),
    LocationName.ITEM_FRAMES_FILTERS: LocationData(FullRegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.ITEM),
    LocationName.ITEM_FISHING_HAT: LocationData(FullRegionName.STANHAMN_LIGHTHOUSE, LocationGroup.ITEM),
    LocationName.ITEM_HONK_ATTACHMENT: LocationData(FullRegionName.STANHAMN_LIGHTHOUSE_ROOF, LocationGroup.ITEM, (LocationName.QUEST_CHAOS,)),
    LocationName.ITEM_UMBRELLA: LocationData(FullRegionName.STANHAMN_KING_FISH_BEACH, LocationGroup.ITEM),
    LocationName.ITEM_OLD_KEY: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.ITEM, (ItemName.HONK_ATTACHMENT,)),
    LocationName.ITEM_HARD_HAT: LocationData(FullRegionName.STANHAMN_HYDROPLANT, LocationGroup.ITEM),
    LocationName.ITEM_DIVING_HELMET: LocationData(FullRegionName.STANHAMN_FISHING_TOWER, LocationGroup.ITEM),
    LocationName.ITEM_RUBBER_BOOTS: LocationData(FullRegionName.STANHAMN_DOCKS_RIGHT, LocationGroup.ITEM),
    LocationName.ITEM_SANDWICH: LocationData(FullRegionName.STANHAMN_HIPPO_BEACH, LocationGroup.ITEM, (ItemName.GHOST_GLASSES, FullRegionName.STANHAMN_OUTSIDE_HYDROPLANT)),
    LocationName.ITEM_PIRATE_HAT: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.ITEM, (ItemName.OLD_KEY,)),
    LocationName.ITEM_PAPER_HAT: LocationData(FullRegionName.STANHAMN_PIRATE_DRAWBRIDGE, LocationGroup.ITEM, (ItemName.HONK_ATTACHMENT, ItemName.PIRATE_HAT)),
    LocationName.ITEM_FLAG: LocationData(FullRegionName.STANHAMN_PHOTO_GUILD_HUT, LocationGroup.ITEM, photo_challenges),
    LocationName.TAPE_FISHERMANS_WHISTLE: LocationData(FullRegionName.STANHAMN_DOCKS_LEFT, LocationGroup.CASSETTE, (FullRegionName.STANHAMN_BUS_STOP,)),
    LocationName.TAPE_SMILING_HUNTSMAN: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.CASSETTE, (ItemName.HONK_ATTACHMENT, ItemName.DIVING_HELMET)),
    LocationName.TAPE_NAUT: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_PLACE_IN_SUN: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_FISHERMANS_TUNE: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.CASSETTE, (ItemName.HONK_ATTACHMENT, ItemName.FISHERMANS_WHISTLE_TAPE)),
    LocationName.CHEEVO_SET_SAIL: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (stanhamn_regions,)),
    LocationName.CHEEVO_VOYAGE_UNDERWATER: LocationData(FullRegionName.STANHAMN_UNDERWATER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_EMPLOYEE_OF_THE_MONTH: LocationData(FullRegionName.STANHAMN_HYDROPLANT, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_CALM_AS_SEA: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_CHALLENGE_3, LocationName.QUEST_CHALLENGE_4)),
    LocationName.CHEEVO_SEAWORTHY: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, stanhamn_quests),
    LocationName.CHEEVO_FLIGHT_READY: LocationData(FullRegionName.STANHAMN_FISHING_TOWER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SPARKLING_JUMP: LocationData(FullRegionName.STANHAMN_BUS_STOP, LocationGroup.ACHIEVEMENT, (ItemName.HONK_ATTACHMENT,)),
    LocationName.CHEEVO_GOOD_BOY: LocationData(FullRegionName.STANHAMN_HIPPO_BEACH, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_LOST_DOG,)),
    LocationName.QUEST_SUS_CITY: LocationData(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST, (FullRegionName.LOGCITY_CROSSWALK,)),
    LocationName.QUEST_RATSKULLZ: LocationData(FullRegionName.LOGCITY_RATSKULLZ_ALLEY, LocationGroup.QUEST),
    LocationName.QUEST_PUNK_ROCKER: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST, (ItemName.CINNAMON_BUN,)),
    LocationName.QUEST_CHALLENGE_5: LocationData(FullRegionName.LOGCITY_OVERPASS, LocationGroup.QUEST, (LocationName.QUEST_GRANNY, FullRegionName.LOGCITY_SKATE_PARK)),
    LocationName.QUEST_CHALLENGE_6: LocationData(FullRegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.QUEST, (FullRegionName.LOGCITY_CROSSWALK,)),
    LocationName.QUEST_NEWS: LocationData(FullRegionName.LOGCITY_NEWS_HOUSE, LocationGroup.QUEST, (LocationName.QUEST_FASHION,)),
    LocationName.QUEST_SEWER: LocationData(FullRegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.QUEST),
    LocationName.QUEST_HOTBEAN: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST, (ItemName.HOTBEAN_HAT, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_SKATE_PARK, FullRegionName.LOGCITY_CROSSWALK)),
    LocationName.QUEST_HANG_IN_THERE: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST),
    LocationName.QUEST_SCARY_CITY: LocationData(FullRegionName.LOGCITY_CROSSWALK, LocationGroup.QUEST, (ItemName.GHOST_GLASSES, LocationName.CHEEVO_CALM_FOREST)),
    LocationName.QUEST_DATE: LocationData(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST, (ItemName.GHOST_GLASSES, FullRegionName.LOGCITY_OUTSIDE_GALLERY)),
    LocationName.QUEST_ART: LocationData(FullRegionName.LOGCITY_GALLERY, LocationGroup.QUEST, ((ItemName.FRAMES_FILTERS, FullRegionName.LOGCITY_RATSKULLZ_ALLEY),)),
    LocationName.QUEST_INFLUENCER: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.QUEST, (FullRegionName.LOGCITY_OUTSIDE_CAFE,)),
    LocationName.QUEST_FASHION: LocationData(FullRegionName.LOGCITY_FASHION_SHOW_BACKSTAGE, LocationGroup.QUEST, (ItemName.HOTBEAN_HAT,)), # TODO second hat is assumed to be hotbean since that's already needed
    LocationName.QUEST_CLEANING: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.QUEST, (FullRegionName.LOGCITY_RATSKULLZ_ALLEY,)),
    LocationName.QUEST_GRANNY: LocationData(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.QUEST),
    LocationName.QUEST_MICE: LocationData(FullRegionName.LOGCITY_CAFE, LocationGroup.QUEST, (ItemName.HONK_ATTACHMENT,)),
    LocationName.QUEST_CROW: LocationData(FullRegionName.LOGCITY_OUTSIDE_CAFE, LocationGroup.QUEST, (ItemName.FRISBEE,)),
    LocationName.COMP_BUSINESS_PIGEON: LocationData(FullRegionName.LOGCITY_OUTSIDE_GALLERY, LocationGroup.COMPENDIUM),
    LocationName.COMP_PORTILLO: LocationData(FullRegionName.LOGCITY_OUTSIDE_CAFE, LocationGroup.COMPENDIUM),
    LocationName.COMP_MOUSE: LocationData(FullRegionName.LOGCITY_OVERPASS, LocationGroup.COMPENDIUM),
    LocationName.COMP_PIGEON: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.LOGCITY_CLOCK_TOWER, FullRegionName.LOGCITY_OUTSIDE_CAFE, FullRegionName.LOGCITY_OUTSIDE_GALLERY, FullRegionName.LOGCITY_RATSKULLZ_ALLEY),)),
    LocationName.COMP_PUNK_PARROT: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.COMPENDIUM, (ItemName.CINNAMON_BUN,)),
    LocationName.COMP_TATO_SKATEBOARD: LocationData(FullRegionName.LOGCITY_SKATE_PARK, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_TOURIST: LocationData(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.COMPENDIUM),
    LocationName.COMP_TURTLE: LocationData(FullRegionName.LOGCITY_CROSSWALK, LocationGroup.COMPENDIUM),
    LocationName.ITEM_HOTBEAN_HAT: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ITEM),
    LocationName.ITEM_REPORTER_HAT: LocationData(FullRegionName.LOGCITY_NEWS_HOUSE, LocationGroup.ITEM),
    LocationName.ITEM_SNEAKERS: LocationData(FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, LocationGroup.ITEM),
    LocationName.ITEM_CINNAMON_BUN: LocationData(FullRegionName.LOGCITY_CAFE, LocationGroup.ITEM, (LocationName.QUEST_MICE,)),
    LocationName.ITEM_FRISBEE: LocationData(FullRegionName.LOGCITY_CROSSWALK, LocationGroup.ITEM, (ItemName.HONK_ATTACHMENT, FullRegionName.LOGCITY_OUTSIDE_CAFE)),
    LocationName.TAPE_RATSKULLZ_THEME: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_BIG_CITY: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_HUSTLE_BUSTLE: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_HOP_SKIP_STEP: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_ON_THE_HOUR: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.CHEEVO_BIG_CITY: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (logcity_regions,)),
    LocationName.CHEEVO_CLOCKTOWER: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_PROFESSIONAL: LocationData(FullRegionName.LOGCITY_OVERPASS, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_CHALLENGE_5, LocationName.QUEST_CHALLENGE_6)),
    LocationName.CHEEVO_BUSINESS: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.ACHIEVEMENT, logcity_quests),
    LocationName.CHEEVO_FOLLOWERS: LocationData(FullRegionName.LOGCITY_CLOCK_TOWER, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_INFLUENCER,)),
    LocationName.CHEEVO_NEW_JOB: LocationData(FullRegionName.LOGCITY_BUS_STOP, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_CLEANING,)),
    LocationName.QUEST_YETI_CUTE: LocationData(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.QUEST, (LocationName.COMP_FLUFF,)),
    LocationName.QUEST_ICE_WIZARD: LocationData(FullRegionName.KIIRUBERG_WIZARD_TOWER, LocationGroup.QUEST, warm_clothes+(ItemName.HONK_ATTACHMENT, FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT, FullRegionName.OAKLAVILLE_GHOST_CUP_GAME, FullRegionName.OAKLAVILLE_CAMP, FullRegionName.STANHAMN_HIPPO_BEACH, FullRegionName.LOGCITY_OUTSIDE_FASHION_SHOW, FullRegionName.LOGCITY_OUTSIDE_GALLERY)),
    LocationName.QUEST_MILITARY_SUS: LocationData(FullRegionName.KIIRUBERG_MILITARY_BASE, LocationGroup.QUEST, (LocationName.QUEST_SUS_FOREST, LocationName.QUEST_SUS_HARBOR, LocationName.QUEST_SUS_CITY)),
    LocationName.QUEST_ASTRONAUT: LocationData(FullRegionName.KIIRUBERG_OBSERVATORY, LocationGroup.QUEST, (ItemName.SPACE_HELMET,)),
    LocationName.QUEST_CHALLENGE_7: LocationData(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.QUEST, (ItemName.CLIMBING_BOOTS, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM)),
    LocationName.QUEST_CHALLENGE_8: LocationData(FullRegionName.KIIRUBERG_CLIFFS_TOP, LocationGroup.QUEST, ((FullRegionName.KIIRUBERG_OBSERVATORY, FullRegionName.KIIRUBERG_MILITARY_BASE, FullRegionName.KIIRUBERG_WIZARD_TOWER),)),
    LocationName.QUEST_ASTEROID: LocationData(FullRegionName.KIIRUBERG_OBSERVATORY, LocationGroup.QUEST, (FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM,)),
    LocationName.QUEST_GOAT_CHOIR: LocationData(FullRegionName.KIIRUBERG_FROZEN_POND, LocationGroup.QUEST, ((FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP), FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, (FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE))),
    LocationName.QUEST_SNOWBALL: LocationData(FullRegionName.KIIRUBERG_FROZEN_POND, LocationGroup.QUEST, (ItemName.CLIMBING_BOOTS,)),
    LocationName.QUEST_BIRTHDAY: LocationData(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, LocationGroup.QUEST, warm_clothes+(FullRegionName.KIIRUBERG_BLIZZARD_BRIDGE_RIGHT,)),
    LocationName.QUEST_PAINTINGS: LocationData(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.QUEST, (ItemName.CLIMBING_BOOTS, FullRegionName.KIIRUBERG_FROZEN_POND, FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, FullRegionName.MOUNTAIN_TOP_TOEM)),
    LocationName.QUEST_BECOME_YETI: LocationData(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, LocationGroup.QUEST),
    LocationName.QUEST_SNOWMAN: LocationData(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.QUEST, (ItemName.HONK_ATTACHMENT, FullRegionName.KIIRUBERG_SKI_LIFT_BASE, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP)),
    LocationName.COMP_MIKEE: LocationData(FullRegionName.KIIRUBERG_BALLOON_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_NARIKO: LocationData(FullRegionName.KIIRUBERG_BALLOON_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_COSMO_DEER: LocationData(FullRegionName.KIIRUBERG_COSMO_GARDEN, LocationGroup.COMPENDIUM),
    LocationName.COMP_TEDDY: LocationData(FullRegionName.KIIRUBERG_MECKS_HOUSE, LocationGroup.COMPENDIUM),
    LocationName.COMP_FLUFF: LocationData(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, LocationGroup.COMPENDIUM),
    LocationName.COMP_HEDGEHOG: LocationData(FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, LocationGroup.COMPENDIUM),
    LocationName.COMP_METEOPAL: LocationData(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.COMPENDIUM, (FullRegionName.KIIRUBERG_OBSERVATORY,)),
    LocationName.COMP_GOAT: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, (FullRegionName.KIIRUBERG_FROZEN_POND, (FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_BOTTOM, FullRegionName.KIIRUBERG_BIRTHDAY_PARTY_TOP, FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, FullRegionName.KIIRUBERG_CLIFFS_TOP, FullRegionName.KIIRUBERG_CLIFFS_MIDDLE))),
    LocationName.COMP_OWL: LocationData(FullRegionName.KIIRUBERG_CLIFFS_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNOW_BIRD: LocationData(FullRegionName.KIIRUBERG_SKI_LIFT_BASE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_ALIEN: LocationData(FullRegionName.KIIRUBERG_OBSERVATORY, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_SKI: LocationData(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, LocationGroup.COMPENDIUM),
    LocationName.ITEM_CLIMBING_BOOTS: LocationData(FullRegionName.KIIRUBERG_FROZEN_POND, LocationGroup.ITEM),
    LocationName.ITEM_PUFFER_HAT: LocationData(FullRegionName.KIIRUBERG_FROZEN_POND, LocationGroup.ITEM, (LocationName.QUEST_SNOWBALL,)),
    LocationName.ITEM_SCARF: LocationData(FullRegionName.KIIRUBERG_SKI_LODGE, LocationGroup.ITEM),
    LocationName.ITEM_SKI_GOGGLES: LocationData(FullRegionName.KIIRUBERG_SKI_MOUNTAIN_TOP, LocationGroup.ITEM),
    LocationName.ITEM_SPACE_HELMET: LocationData(FullRegionName.KIIRUBERG_OUTSIDE_OBSERVATORY_BOTTOM, LocationGroup.ITEM),
    LocationName.TAPE_LIFE_THROUGH_LENS: LocationData(FullRegionName.KIIRUBERG_BUS_STOP, LocationGroup.CASSETTE, (ItemName.CLIMBING_BOOTS,)),
    LocationName.TAPE_PETTING_DEER: LocationData(FullRegionName.KIIRUBERG_BUS_STOP, LocationGroup.CASSETTE, (ItemName.CLIMBING_BOOTS, ItemName.HONK_ATTACHMENT, ItemName.PUFFER_HAT, ItemName.SKI_GOGGLES, ItemName.SCARF)),
    LocationName.TAPE_STORIES_OF_SNOW: LocationData(FullRegionName.KIIRUBERG_BUS_STOP, LocationGroup.CASSETTE),
    LocationName.TAPE_TALL_SHY: LocationData(FullRegionName.KIIRUBERG_BUS_STOP, LocationGroup.CASSETTE, (ItemName.CLIMBING_BOOTS, ItemName.HONK_ATTACHMENT, ItemName.PUFFER_HAT, ItemName.SKI_GOGGLES, ItemName.SCARF)),
    LocationName.CHEEVO_SNOWY_PEAKS: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (kiiruberg_regions,)),
    LocationName.CHEEVO_GEARED_UP: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, warm_clothes),
    LocationName.CHEEVO_HURDLE: LocationData(FullRegionName.KIIRUBERG_SNOWMAN_SQUARE_BOTTOM, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_CHALLENGE_7, LocationName.QUEST_CHALLENGE_8)),
    LocationName.CHEEVO_FIGHTER: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, kiiruberg_quests),
    LocationName.CHEEVO_YOUTH: LocationData(FullRegionName.KIIRUBERG_OLD_MANS_HOUSE, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_SNOWBALL,)),
    LocationName.CHEEVO_STORY: LocationData(FullRegionName.KIIRUBERG_CLIFFS_MIDDLE, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_PAINTINGS,)),
    LocationName.CHEEVO_CLOSE: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, ((FullRegionName.MOUNTAIN_TOP_BUS_STOP, FullRegionName.MOUNTAIN_TOP_TOEM),)),
    LocationName.CHEEVO_TOEM: LocationData(FullRegionName.MOUNTAIN_TOP_TOEM, LocationGroup.ACHIEVEMENT, (ItemName.CLIMBING_BOOTS,)),
    LocationName.CHEEVO_CUTIES: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, dev_animals),
    LocationName.CHEEVO_COLLECT_EM_ALL: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, base_animals),
    LocationName.CHEEVO_GOING_LONG: LocationData(FullRegionName.MOUNTAIN_TOP_TOEM, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_COSPLAYER: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, clothing_items),
    LocationName.CHEEVO_COMPLETIONIST: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, completionist_reqs),
    LocationName.QUEST_BALLOONS: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, (ItemName.WATERGUN, (FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT), (FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT), FullRegionName.BASTO_LILY_PAD_POND_RIGHT, (FullRegionName.BASTO_CAMP_DAY, FullRegionName.BASTO_CAMP_NIGHT), FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_BONFIRE_TOP, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT), FullRegionName.BASTO_JUNGLE, FullRegionName.BASTO_GHOST_HANGOUT, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.QUEST_ARTHUR: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (ItemName.PICKAXE, FullRegionName.BASTO_OUTSIDE_CASTLE, (FullRegionName.BASTO_BUS_STOP_TOP_DAY, FullRegionName.BASTO_BUS_STOP_TOP_NIGHT))),
    LocationName.QUEST_BAD_HAIR_DAY: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (ItemName.WATERGUN,)),
    LocationName.QUEST_TAKE_A_NAP: LocationData(FullRegionName.BASTO_TENT, LocationGroup.QUEST),
    LocationName.QUEST_SPOOKY_STORIES: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (ItemName.WATERGUN, FullRegionName.BASTO_JUNGLE)),
    LocationName.QUEST_PORTRAITS: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.QUEST),
    LocationName.QUEST_CINEMA: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (ItemName.WATERGUN,)),
    LocationName.QUEST_NIGHT_LIGHTS: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (LocationName.COMP_FIRE_FLY,)),
    LocationName.QUEST_JET_SKI: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, ((FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT),)),
    LocationName.QUEST_FRUITS: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.QUEST, (ItemName.BANAKIN, ItemName.MELONEAR, ItemName.BEANUT, ItemName.ORANGANAS)),
    LocationName.QUEST_BRAIN_FREEZE: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.QUEST, (ItemName.PICKAXE, ItemName.ICE_CREAM)),
    LocationName.QUEST_SWEET_TOOTH: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, (ItemName.ICE_CREAM, LocationName.QUEST_BATS, (FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT))),
    LocationName.QUEST_IN_YOUR_FACE: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, (ItemName.ICE_CREAM, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.QUEST_BROKEN_DREAMS: LocationData(FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, LocationGroup.QUEST, (ItemName.ICE_CREAM,)),
    LocationName.QUEST_DRY_SEASON: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, (ItemName.WATERGUN, (FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT), (FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT), (FullRegionName.BASTO_CAMP_DAY, FullRegionName.BASTO_CAMP_NIGHT), FullRegionName.BASTO_BONFIRE_TOP, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT), FullRegionName.BASTO_JUNGLE, (FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT), FullRegionName.BASTO_GHOST_HANGOUT, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT), FullRegionName.BASTO_GYM_HOUSE)),
    LocationName.QUEST_MUSCLES: LocationData(FullRegionName.BASTO_GYM_HOUSE, LocationGroup.QUEST, (ItemName.EMPTY_BOTTLE, FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_OUTSIDE_CASTLE)),
    LocationName.QUEST_SAND_CASTLE: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, (LocationName.QUEST_IN_YOUR_FACE, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.QUEST_CARNIVAL: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, ((ItemName.WATERGUN, ItemName.HONK_ATTACHMENT), (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.QUEST_BATS: LocationData(FullRegionName.START_MENU, LocationGroup.QUEST, ((ItemName.HONK_ATTACHMENT, ItemName.WATERGUN), FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_OUTSIDE_CASTLE, (FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT))),
    LocationName.QUEST_BITLING: LocationData(FullRegionName.BASTO_JUNGLE, LocationGroup.QUEST, (LocationName.COMP_BITLING_FROG, LocationName.COMP_BITLING_MOUSE, LocationName.COMP_BITLING_SNAIL, LocationName.COMP_BITLING_TATO)),
    LocationName.COMP_BAT: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT, FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_OUTSIDE_CASTLE),)),
    LocationName.COMP_SNAKE: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_CAMP_DAY, FullRegionName.BASTO_CAMP_NIGHT),)),
    LocationName.COMP_BEAK_BIRD: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, FullRegionName.BASTO_BUS_STOP_TOP_DAY, FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, FullRegionName.BASTO_LILY_PAD_POND_RIGHT),)),
    LocationName.COMP_BITLING_FROG: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_BONFIRE_BOTTOM_DAY, FullRegionName.BASTO_BONFIRE_BOTTOM_NIGHT),)),
    LocationName.COMP_BITLING_MOUSE: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, (LocationName.QUEST_IN_YOUR_FACE, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.COMP_BITLING_SNAIL: LocationData(FullRegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_BITLING_TATO: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, FullRegionName.BASTO_BUS_STOP_TOP_DAY, FullRegionName.BASTO_BUS_STOP_TOP_NIGHT),)),
    LocationName.COMP_COCO_CRAB: LocationData(FullRegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_DAY_LIZARD: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_DRILL_MOLE: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_EGGERT: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_FIRE_FLY: LocationData(FullRegionName.BASTO_GHOST_HANGOUT, LocationGroup.COMPENDIUM),
    LocationName.COMP_GLOW_WORM: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT),)),
    LocationName.COMP_ITSY_BITSY: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_SECRET_CAVE_DAY, FullRegionName.BASTO_SECRET_CAVE_NIGHT),)),
    LocationName.COMP_MUD_FROG: LocationData(FullRegionName.BASTO_CAMP_NIGHT, LocationGroup.COMPENDIUM),
    LocationName.COMP_NIGHT_LIZARD: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.COMPENDIUM),
    LocationName.COMP_SNOUT_BUG: LocationData(FullRegionName.BASTO_JUNGLE, LocationGroup.COMPENDIUM),
    LocationName.COMP_TATO_COCO: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.COMPENDIUM, (ItemName.WATERGUN,)),
    LocationName.COMP_TATO_KING: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, (ItemName.WATERGUN, (FullRegionName.BASTO_SECRET_CAVE_DAY, FullRegionName.BASTO_SECRET_CAVE_NIGHT))),
    LocationName.COMP_WATER_STRIDER: LocationData(FullRegionName.START_MENU, LocationGroup.COMPENDIUM, ((FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, FullRegionName.BASTO_OUTSIDE_CASTLE),)),
    LocationName.ITEM_BASTO_TICKET: LocationData(FullRegionName.HOMELANDA_LIVING_ROOM, LocationGroup.ITEM, (LocationName.QUEST_EXPERIENCE_TOEM,)),
    LocationName.ITEM_WATERGUN: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, ((FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT),)),
    LocationName.ITEM_SUN_HAT: LocationData(FullRegionName.BASTO_TENT, LocationGroup.ITEM),
    LocationName.ITEM_MELONEAR: LocationData(FullRegionName.BASTO_LILY_PAD_POND_RIGHT, LocationGroup.ITEM, (ItemName.WATERGUN,)),
    LocationName.ITEM_BANAKIN: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (ItemName.WATERGUN,)),
    LocationName.ITEM_ORANGANAS: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM, (ItemName.WATERGUN,)),
    LocationName.ITEM_BEANUT: LocationData(FullRegionName.BASTO_CAMP_DAY, LocationGroup.ITEM, (ItemName.WATERGUN,)),
    LocationName.ITEM_PICKAXE: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM),
    LocationName.ITEM_SUN_CAP: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (ItemName.PICKAXE, (FullRegionName.BASTO_CAVE_DAY, FullRegionName.BASTO_CAVE_NIGHT))),
    LocationName.ITEM_FLIP_FLOPS: LocationData(FullRegionName.BASTO_GHOST_HANGOUT, LocationGroup.ITEM, (ItemName.PICKAXE,)),
    LocationName.ITEM_ICE_CREAM_BANAKIN: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (ItemName.BANAKIN,)),
    LocationName.ITEM_ICE_CREAM_MELONEAR: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (ItemName.MELONEAR,)),
    LocationName.ITEM_ICE_CREAM_BEANUT: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (ItemName.BEANUT,)),
    LocationName.ITEM_ICE_CREAM_ORANGANAS: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (ItemName.ORANGANAS,)),
    LocationName.ITEM_ROYAL_CAPE: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (LocationName.QUEST_SAND_CASTLE, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.ITEM_MINIGAME_TICKET: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, ((ItemName.WATERGUN, ItemName.HONK_ATTACHMENT), (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.ITEM_LEI: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (ItemName.MINIGAME_TICKET, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.ITEM_VACATION_SHIRT: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (ItemName.MINIGAME_TICKET, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.ITEM_ROYAL_CANE: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (ItemName.MINIGAME_TICKET, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.ITEM_EMPTY_BOTTLE: LocationData(FullRegionName.BASTO_GHOST_HANGOUT, LocationGroup.ITEM),
    LocationName.ITEM_VIKING_HELMET: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.ITEM, (LocationName.QUEST_BRAIN_FREEZE,)),
    LocationName.ITEM_FOOT_CAST: LocationData(FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, LocationGroup.ITEM, (LocationName.QUEST_BROKEN_DREAMS,)),
    LocationName.ITEM_BERET: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ITEM, (LocationName.CHEEVO_CALMED_DOWN, LocationName.CHEEVO_JUST_A_SOCK, LocationName.CHEEVO_SPARKLING_JUMP, LocationName.CHEEVO_FLIGHT_READY, LocationName.CHEEVO_FOLLOWERS, LocationName.CHEEVO_NEW_JOB, LocationName.CHEEVO_YOUTH, LocationName.CHEEVO_STORY, LocationName.CHEEVO_MOONLIT_BEAUTY, LocationName.CHEEVO_KINGS_SHIRT)),
    LocationName.ITEM_ROYAL_CROWN: LocationData(FullRegionName.START_MENU, LocationGroup.ITEM, (ItemName.PICKAXE, LocationName.COMP_TATO_KING, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))), 
    LocationName.TAPE_NIGHT_JAM: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)),
    LocationName.TAPE_WARM_DAYS_NIGHT: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)),
    LocationName.TAPE_ONE_BY_ONE: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)),
    LocationName.TAPE_HAMMOCK_DAYS: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)),
    LocationName.TAPE_SAILORS_TUNE: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)), # Basto stamp requirement handled as special case
    LocationName.TAPE_SONG_OF_THE_SEA: LocationData(FullRegionName.BASTO_BUS_STOP_BOTTOM_DAY, LocationGroup.CASSETTE, (ItemName.WATERGUN,)),
    LocationName.CHEEVO_TOPICAL_PARADISE: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (basto_regions,)),
    LocationName.CHEEVO_MAXIMUM_VACATION: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (ItemName.VACATION_SHIRT, ItemName.FLIP_FLOPS, ItemName.SUN_HAT, (FullRegionName.BASTO_LILY_PAD_POND_LEFT_DAY, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, FullRegionName.BASTO_GYM_HOUSE, FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT, FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_GHOST_HANGOUT))),
    LocationName.CHEEVO_KINGS_SHIRT: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (ItemName.ROYAL_CAPE, (FullRegionName.BASTO_CASTLE_DAY, FullRegionName.BASTO_CASTLE_NIGHT))),
    LocationName.CHEEVO_MOONLIT_BEAUTY: LocationData(FullRegionName.BASTO_BONFIRE_TOP, LocationGroup.ACHIEVEMENT, (LocationName.QUEST_BAD_HAIR_DAY,)),
    LocationName.CHEEVO_SELF_PORTRAIT: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_WAZZUUPPP: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (ItemName.FRAMES_FILTERS, (FullRegionName.BASTO_BUS_STOP_TOP_NIGHT, FullRegionName.BASTO_BUS_STOP_BOTTOM_NIGHT, FullRegionName.BASTO_LILY_PAD_POND_LEFT_NIGHT, FullRegionName.BASTO_LILY_PAD_POND_RIGHT, FullRegionName.BASTO_CAMP_NIGHT, FullRegionName.BASTO_OUTSIDE_CASTLE, FullRegionName.BASTO_BONFIRE_TOP, FullRegionName.BASTO_BONFIRE_BOTTOM_NIGHT, FullRegionName.BASTO_GHOST_HANGOUT, FullRegionName.BASTO_JUNGLE))),
    LocationName.CHEEVO_PRO_GAMER: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, (ItemName.WATERGUN, ItemName.HONK_ATTACHMENT, (FullRegionName.BASTO_CARNIVAL_DAY, FullRegionName.BASTO_CARNIVAL_NIGHT))),
    LocationName.CHEEVO_SPLISH_SPLASH: LocationData(FullRegionName.BASTO_GHOST_HANGOUT, LocationGroup.ACHIEVEMENT, (ItemName.WATERGUN, LocationName.QUEST_TAKE_A_BATH)),
    LocationName.CHEEVO_ROYAL_CASTLE: LocationData(FullRegionName.BASTO_OUTSIDE_CASTLE, LocationGroup.ACHIEVEMENT),
    LocationName.CHEEVO_SOME_MORE: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, basto_animals),
    LocationName.CHEEVO_VIKINGS_HOLIDAY: LocationData(FullRegionName.START_MENU, LocationGroup.ACHIEVEMENT, basto_quests),
}

item_to_location_name: dict[str, str] = {
    ItemName.CLOGS: LocationName.ITEM_CLOGS,
    ItemName.AWARD_MASK: LocationName.ITEM_AWARD_MASK,
    ItemName.FINGER: LocationName.ITEM_FINGER,
    ItemName.TRIPOD: LocationName.ITEM_TRIPOD,
    ItemName.COWBOY_HAT: LocationName.ITEM_COWBOY_HAT,
    ItemName.WET_SOCKS: LocationName.ITEM_WET_SOCKS,
    ItemName.FJALLBJORN_HAT: LocationName.ITEM_FJALLBJORN_HAT,
    ItemName.GHOST_GLASSES: LocationName.ITEM_GHOST_GLASSES,
    ItemName.SOAKED_SOCK: LocationName.ITEM_SOAKED_SOCK,
    ItemName.MONSTER_MASK: LocationName.ITEM_MONSTER_MASK,
    ItemName.FRAMES_FILTERS: LocationName.ITEM_FRAMES_FILTERS,
    ItemName.FISHING_HAT: LocationName.ITEM_FISHING_HAT,
    ItemName.HONK_ATTACHMENT: LocationName.ITEM_HONK_ATTACHMENT,
    ItemName.UMBRELLA: LocationName.ITEM_UMBRELLA,
    ItemName.OLD_KEY: LocationName.ITEM_OLD_KEY,
    ItemName.HARD_HAT: LocationName.ITEM_HARD_HAT,
    ItemName.DIVING_HELMET: LocationName.ITEM_DIVING_HELMET,
    ItemName.RUBBER_BOOTS: LocationName.ITEM_RUBBER_BOOTS,
    ItemName.SANDWICH: LocationName.ITEM_SANDWICH,
    ItemName.PIRATE_HAT: LocationName.ITEM_PIRATE_HAT,
    ItemName.PAPER_HAT: LocationName.ITEM_PAPER_HAT,
    ItemName.FLAG: LocationName.ITEM_FLAG,
    ItemName.HOTBEAN_HAT: LocationName.ITEM_HOTBEAN_HAT,
    ItemName.REPORTER_HAT: LocationName.ITEM_REPORTER_HAT,
    ItemName.SNEAKERS: LocationName.ITEM_SNEAKERS,
    ItemName.CINNAMON_BUN: LocationName.ITEM_CINNAMON_BUN,
    ItemName.FRISBEE: LocationName.ITEM_FRISBEE,
    ItemName.CLIMBING_BOOTS: LocationName.ITEM_CLIMBING_BOOTS,
    ItemName.PUFFER_HAT: LocationName.ITEM_PUFFER_HAT,
    ItemName.SCARF: LocationName.ITEM_SCARF,
    ItemName.SKI_GOGGLES: LocationName.ITEM_SKI_GOGGLES,
    ItemName.SPACE_HELMET: LocationName.ITEM_SPACE_HELMET,
    ItemName.BASTO_TICKET: LocationName.ITEM_BASTO_TICKET,
    ItemName.WATERGUN: LocationName.ITEM_WATERGUN,
    ItemName.SUN_HAT: LocationName.ITEM_SUN_HAT,
    ItemName.MELONEAR: LocationName.ITEM_MELONEAR,
    ItemName.BANAKIN: LocationName.ITEM_BANAKIN,
    ItemName.ORANGANAS: LocationName.ITEM_ORANGANAS,
    ItemName.BEANUT: LocationName.ITEM_BEANUT,
    ItemName.PICKAXE: LocationName.ITEM_PICKAXE,
    ItemName.SUN_CAP: LocationName.ITEM_SUN_CAP,
    ItemName.FLIP_FLOPS: LocationName.ITEM_FLIP_FLOPS,
    #ItemName.ICE_CREAM: handled as an edge case
    ItemName.ROYAL_CAPE: LocationName.ITEM_ROYAL_CAPE,
    ItemName.MINIGAME_TICKET: LocationName.ITEM_MINIGAME_TICKET,
    ItemName.LEI: LocationName.ITEM_LEI,
    ItemName.VACATION_SHIRT: LocationName.ITEM_VACATION_SHIRT,
    ItemName.ROYAL_CANE: LocationName.ITEM_ROYAL_CANE,
    ItemName.EMPTY_BOTTLE: LocationName.ITEM_EMPTY_BOTTLE,
    ItemName.VIKING_HELMET: LocationName.ITEM_VIKING_HELMET,
    ItemName.FOOT_CAST: LocationName.ITEM_FOOT_CAST,
    ItemName.BERET: LocationName.ITEM_BERET,
    ItemName.ROYAL_CROWN: LocationName.ITEM_ROYAL_CROWN,
    ItemName.PHOTO_OF_HOME_TAPE: LocationName.TAPE_PHOTO_OF_HOME,
    ItemName.SUMMER_BREEZE_TAPE: LocationName.TAPE_SUMMER_BREEZE,
    ItemName.SQUIRREL_HOTEL_TAPE: LocationName.TAPE_SQUIRREL_HOTEL,
    ItemName.PINE_NEEDLES_TAPE: LocationName.TAPE_PINE_NEEDLES,
    ItemName.SQUIRREL_PHOTO_TAPE: LocationName.TAPE_SQUIRREL_PHOTO,
    ItemName.FISHERMANS_WHISTLE_TAPE: LocationName.TAPE_FISHERMANS_WHISTLE,
    ItemName.SMILING_HUNTSMAN_TAPE: LocationName.TAPE_SMILING_HUNTSMAN,
    ItemName.NAUT_TAPE: LocationName.TAPE_NAUT,
    ItemName.PLACE_IN_SUN_TAPE: LocationName.TAPE_PLACE_IN_SUN,
    ItemName.FISHERMANS_TUNE_TAPE: LocationName.TAPE_FISHERMANS_TUNE,
    ItemName.RATSKULLZ_THEME_TAPE: LocationName.TAPE_RATSKULLZ_THEME,
    ItemName.BIG_CITY_TAPE: LocationName.TAPE_BIG_CITY,
    ItemName.HUSTLE_BUSTLE_TAPE: LocationName.TAPE_HUSTLE_BUSTLE,
    ItemName.HOP_SKIP_STEP_TAPE: LocationName.TAPE_HOP_SKIP_STEP,
    ItemName.ON_THE_HOUR_TAPE: LocationName.TAPE_ON_THE_HOUR,
    ItemName.LIFE_THROUGH_LENS_TAPE: LocationName.TAPE_LIFE_THROUGH_LENS,
    ItemName.PETTING_DEER_TAPE: LocationName.TAPE_PETTING_DEER,
    ItemName.STORIES_OF_SNOW_TAPE: LocationName.TAPE_STORIES_OF_SNOW,
    ItemName.TALL_SHY_TAPE: LocationName.TAPE_TALL_SHY,
    ItemName.NIGHT_JAM_TAPE: LocationName.TAPE_NIGHT_JAM,
    ItemName.WARM_DAYS_NIGHT_TAPE: LocationName.TAPE_WARM_DAYS_NIGHT,
    ItemName.ONE_BY_ONE_TAPE: LocationName.TAPE_ONE_BY_ONE,
    ItemName.HAMMOCK_DAYS_TAPE: LocationName.TAPE_HAMMOCK_DAYS,
    ItemName.SAILORS_TUNE_TAPE: LocationName.TAPE_SAILORS_TUNE,
    ItemName.SONG_OF_THE_SEA_TAPE: LocationName.TAPE_SONG_OF_THE_SEA,
}


location_name_to_id: dict[str, int] = {name: i for i, name in enumerate(location_table, start=1)}


def get_location_group(location_name: str) -> str:
    return location_table[location_name].group


def get_location_area(location_name: str) -> str:
    return location_table[location_name].region


location_name_groups: dict[str, set[str]] = {
    group: set(location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}

from dataclasses import dataclass
from typing import ClassVar

from Options import PerGameCommonOptions, StartInventoryPool, Toggle


class IncludeBasto(Toggle):
    """Include the free DLC Basto. Changes the goal to the Basto bonfire."""

    display_name: ClassVar[str] = "Include Basto"
    default: ClassVar[int] = 0


class IncludeItems(Toggle):
    """Include inventory and clothing items as locations."""

    display_name: ClassVar[str] = "Include Items"
    default: ClassVar[int] = 1


class IncludeCassettes(Toggle):
    """Include cassette tapes as locations."""

    display_name: ClassVar[str] = "Include Cassettes"
    default: ClassVar[int] = 1


class IncludeAchievements(Toggle):
    """Include achievements as locations. Adds more stamps to the pool to compensate."""

    display_name: ClassVar[str] = "Include Achievements"
    default: ClassVar[int] = 0


@dataclass
class ToemOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    include_basto: IncludeBasto
    include_items: IncludeItems
    include_cassettes: IncludeCassettes
    include_achievements: IncludeAchievements

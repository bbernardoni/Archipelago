from dataclasses import dataclass
from typing import ClassVar

from Options import PerGameCommonOptions, StartInventoryPool, Toggle, Range


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
    default: ClassVar[int] = 0


class IncludeAchievements(Toggle):
    """Include achievements as locations. Adds more photos to the pool to compensate."""

    display_name: ClassVar[str] = "Include Achievements"
    default: ClassVar[int] = 0


class HomelandaStampRequirement(Range):
    """The number of stamps required to leave Homelanda."""
    display_name = "Homelanda Stamp Requirement"
    range_start = 0
    range_end = 3
    default = 1


class OaklavilleStampRequirement(Range):
    """The number of stamps required to leave Oaklaville."""
    display_name = "Oaklaville Stamp Requirement"
    range_start = 0
    range_end = 15
    default = 7


class StanhamnStampRequirement(Range):
    """The number of stamps required to leave Stanhamn."""
    display_name = "Stanhamn Stamp Requirement"
    range_start = 0
    range_end = 16
    default = 8


class LogcityStampRequirement(Range):
    """The number of stamps required to leave Logcity."""
    display_name = "Logcity Stamp Requirement"
    range_start = 0
    range_end = 18
    default = 9


class KiirubergStampRequirement(Range):
    """The number of stamps required to leave Kiiruberg."""
    display_name = "Kiiruberg Stamp Requirement"
    range_start = 0
    range_end = 13
    default = 6


class BastoStampRequirement(Range):
    """The number of stamps required to leave Basto."""
    display_name = "Basto Stamp Requirement"
    range_start = 0
    range_end = 20
    default = 10


class HonkAttachmentEarly(Toggle):
    """Add honk attachment to `early_items`. Will force it to be in a player's sphere 1 to make it more likely to be found before reaching Stanhamn."""

    display_name: ClassVar[str] = "Honk Attachment Early"
    default: ClassVar[int] = 0


@dataclass
class ToemOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    include_basto: IncludeBasto
    include_items: IncludeItems
    include_cassettes: IncludeCassettes
    include_achievements: IncludeAchievements
    homelanda_stamp_requirement: HomelandaStampRequirement
    oaklaville_stamp_requirement: OaklavilleStampRequirement
    stanhamn_stamp_requirement: StanhamnStampRequirement
    logcity_stamp_requirement: LogcityStampRequirement
    kiiruberg_stamp_requirement: KiirubergStampRequirement
    basto_stamp_requirement: BastoStampRequirement
    honk_attachment_early: HonkAttachmentEarly


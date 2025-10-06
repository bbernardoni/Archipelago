from dataclasses import dataclass
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


@dataclass
class RegionData:
    region: str
    exits: tuple[str, ...] = ()


toem_regions: dict[str, RegionData] = {
    RegionName.HOMELANDA: RegionData(RegionName.HOMELANDA, exits=(RegionName.OAKLAVILLE,)),
    RegionName.OAKLAVILLE: RegionData(RegionName.OAKLAVILLE, exits=(RegionName.STANHAMN,)),
    RegionName.STANHAMN: RegionData(RegionName.STANHAMN, exits=(RegionName.LOGCITY,)),
    RegionName.LOGCITY: RegionData(RegionName.LOGCITY, exits=(RegionName.KIIRUBERG,)),
    RegionName.KIIRUBERG: RegionData(RegionName.KIIRUBERG, exits=(RegionName.MOUNTAIN_TOP,)),
    RegionName.MOUNTAIN_TOP: RegionData(RegionName.MOUNTAIN_TOP, exits=(RegionName.BASTO,)),
    RegionName.BASTO: RegionData(RegionName.BASTO),
}

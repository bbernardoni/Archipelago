"""TrapLink: mirrors traps between players via Bounce packets tagged TrapLink."""

import time
from typing import Optional, TYPE_CHECKING

import worlds._bizhawk as bizhawk
from .data import data
from .items import EXTENDED_TRAPLINK_MAPPING

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

TRAP_LINK_MASK = 0b00001000
TRAP_LINK_SETTING_ADDR = data.ram_addresses["wArchipelagoOptions"] + 5

TRAP_ID_TO_NAME = {item.item_id: item.label for item in data.items.values() if "Trap" in item.tags}
TRAP_NAME_TO_ID = {item_name: item_id for item_id, item_name in TRAP_ID_TO_NAME.items()} | EXTENDED_TRAPLINK_MAPPING


async def handle_trap_link_setting(ctx: "BizHawkClientContext", guard) -> None:
    trap_link_setting_status = await bizhawk.guarded_read(
        ctx.bizhawk_ctx,
        [(TRAP_LINK_SETTING_ADDR, 1, "WRAM")],
        [guard]
    )

    old_tags = ctx.tags.copy()

    if trap_link_setting_status:
        if trap_link_setting_status[0][0] & TRAP_LINK_MASK:
            ctx.tags.add("TrapLink")
        else:
            ctx.tags -= {"TrapLink"}

    if old_tags != ctx.tags and ctx.server and not ctx.server.socket.closed:
        await ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": ctx.tags}])



async def send_trap_link(ctx: "BizHawkClientContext", trap_id: int):
    if "TrapLink" not in ctx.tags or ctx.slot is None:
        return

    if trap_id not in TRAP_ID_TO_NAME: return

    await ctx.send_msgs([{
        "cmd": "Bounce",
        "tags": ["TrapLink"],
        "data": {
            "time": time.time(),
            "source": ctx.player_names[ctx.slot],
            "trap_name": TRAP_ID_TO_NAME[trap_id],
        }
    }])


def resolve_trap_link_id(ctx: "BizHawkClientContext", args: dict) -> Optional[int]:
    """Local trap id for an incoming TrapLink bounce, or None if it should be ignored."""
    if "tags" not in args or "data" not in args:
        return None
    if "TrapLink" not in ctx.tags or "TrapLink" not in args["tags"]:
        return None
    if args["data"]["source"] == ctx.player_names[ctx.slot]:
        return None

    trap_name: str = args["data"]["trap_name"]
    if trap_name not in TRAP_NAME_TO_ID:
        return None

    local_trap_name = TRAP_ID_TO_NAME[TRAP_NAME_TO_ID[trap_name]]
    weights = ctx.slot_data.get("trap_weights")
    if not weights or weights.get(local_trap_name, 0) == 0:
        return None

    return TRAP_NAME_TO_ID[trap_name]

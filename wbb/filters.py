from pyrogram import filters
from typing import List, Union
from sample_config import USERBOT_PREFIXES


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, USERBOT_PREFIXES)

import asyncio

# Fix Python 3.10+ / 3.14 asyncio event loop issue for Pyrogram
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from FileToLink.config import Config, Strings
from FileToLink.client import bot

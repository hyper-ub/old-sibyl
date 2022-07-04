
from Sibyl_System import SIBYL, Sibyl_logs, API_ID_KEY, API_HASH_KEY, STRING_SESSION, System
from Sibyl_System.strings import on_string
from pyrogram import Client, filters, idle

import logging
import asyncio
import importlib

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from Sibyl_System.plugins import to_load

HELP = {}
IMPORTED = {}
for load in to_load: 
    imported = importlib.import_module("Sibyl_System.plugins." + load)
    if not hasattr(imported, "__plugin_name__"):
        imported.__plugin_name__ = imported.__name__

    if not imported.__plugin_name__.lower() in IMPORTED:
        IMPORTED[imported.__plugin_name__.lower()] = imported

    if hasattr(imported, "help_plus") and imported.help_plus:
        HELP[imported.__plugin_name__.lower()] = imported 

@System.on_message(filters.command(["status", "sibyl"], prefixes=f"!"))
async def status (client, message):
    if message.from_user.id in SIBYL:
         await System.send_message(message.chat.id, on_string)
    else:
         return

@System.on_message(filters.command(["help"], prefixes=f"!"))
async def status (client, message): 
    if message.from_user.id in SIBYL:
         help_for = event.text.split(" ", 1)[1].lower()
         if help_for in HELP:
              await System.send_message(message.chat.id, HELP[help_for].help_plus)
         else:
              return 
    else:
         return



System.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
System.stop()

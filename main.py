# 2022 @riz4d
# Github - https://github.com/riz4d

import os 
from os import error
import speedtest   
import logging
import pyrogram
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

riz4d = Client(
    "Bandwidth bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@riz4d.on_message(filters.command(["start"]))
async def start(bot, update):
 txt = await update.reply_text("Hey I'm Bandwidth bot by @riz4d. i can measure your internet speed !!")

@riz4d.on_message(filters.private)
async def download_upload(bot, message):
     alert = await message.reply_text("Processing....")
     speed = speedtest.Speedtest() 
     await alert.edit("Getting Best server")
     speed.get_best_server()
     await alert.edit(f'**Connected to :** {speed.results.server["sponsor"]} ({speed.results.server["name"]})')
     message = await message.reply_text("Checking Download / Upload Speed ...")
     downloadspeed = speed.download()
     downloadspeed = downloadspeed/1000000 # bit to kbps
     uploadspeed = speed.upload()
     uploadspeed = uploadspeed/1000000 # bit to kbps
     await alert.delete()
     await message.edit_text(f' **Download Speed :** `{downloadspeed} kbps` \n**Upload Speed :** `{uploadspeed} kbps` \n**Server :** {speed.results.server["sponsor"]} ({speed.results.server["name"]})\n \n Developer @riz4d')

riz4d.run()

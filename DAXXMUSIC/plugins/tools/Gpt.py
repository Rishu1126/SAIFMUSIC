import random
import time
import requests
from DAXXMUSIC import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["chatgpt","ai","ask","gpt","solve"],  prefixes=["+", ".", "/", "-", "", "$","#","&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n/𝐂𝐡𝐚𝐭𝐠𝐩𝐭 𝐰𝐡𝐞𝐫𝐞 𝐢𝐬 𝐌𝐲 𝐨𝐰𝐧𝐞𝐫 𝐃𝐢𝐜𝐭𝐚𝐭𝐨𝐫?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                # Check if "results" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f" {x}      𝐀𝐧𝐬𝐰𝐞𝐫𝐢𝐧𝐠 𝐁𝐲 👉🏻  @Yashika_mUsicBot",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("𝐧𝐨 'results' 𝐤𝐞𝐲 𝐅𝐨𝐮𝐧𝐝 𝐢𝐧 𝐓𝐡𝐞 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("ᴇʀʀᴏʀ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.")
    except Exception as e:
        await message.reply_text(f"**ʜᴇʟʟᴏ: {e} ")

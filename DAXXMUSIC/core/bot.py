from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class DAXX(Client):
    def __init__(self):
        LOGGER(__name__).info(f"𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐚𝐬𝐡𝐢𝐤𝐚 𝐦𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 💗...")
        super().__init__(
            name="𝐘𝐚𝐬𝐡𝐢𝐤𝐚 𝐌𝐮𝐬𝐢𝐜",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "𝐎𝐨𝐩𝐬! 𝐁𝐨𝐭 𝐇𝐚𝐬 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩/𝐂𝐡𝐚𝐧𝐧𝐞𝐥. 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐓𝐡𝐚𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐝𝐝𝐞𝐝 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩/𝐂𝐡𝐚𝐧𝐧𝐞𝐥."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"𝐎𝐨𝐩𝐬! 𝐁𝐨𝐭 𝐇𝐚𝐬 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩/𝐂𝐡𝐚𝐧𝐧𝐞𝐥.\n  𝐑𝐞𝐚𝐬𝐨𝐧 👉🏻 : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "𝐏𝐥𝐞𝐚𝐬𝐞 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐀𝐬 𝐚𝐧 𝐀𝐝𝐦𝐢𝐧 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩/𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚠️."
            )
            exit()
        LOGGER(__name__).info(f"𝐘𝐚𝐬𝐡𝐢𝐤𝐚 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐚𝐬 {self.name}")

    async def stop(self):
        await super().stop()

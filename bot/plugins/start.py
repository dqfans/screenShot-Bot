from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"𝗛𝗶 {m.from_user.first_name}.\n\n𝐈'𝐦 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐁𝐨𝐭. 𝐈 𝐜𝐚𝐧 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 𝐯𝐢𝐝𝐞𝐨 𝐟𝐢𝐥𝐞𝐬 𝐰𝐢𝐭𝐡 𝐨𝐮𝐭 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐡𝐞 𝐞𝐧𝐭𝐢𝐫𝐞 𝐟𝐢𝐥𝐞 (𝐚𝐥𝐦𝐨𝐬𝐭 𝐢𝐧𝐬𝐭𝐚𝐧𝐭𝐥𝐲).",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Help', url='https://telegra.ph/Features-of-TS-ScreenshotBot-05-31'),
                    InlineKeyboardButton('Project Channel', url='https://t.me/TSproject')
                ],
                [
                    InlineKeyboardButton('My Boss', url='https://t.me/tsadmins')
                ]
            ]
        )
    )

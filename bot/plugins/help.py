from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


HELP_TEXT = """
Hi {}. Welcome to @TS_ScreenshotBot. You can use me to generate

    1. Screenshots.
    2. Sample Video.
    3. Trim Video.

𝐌𝐲 𝐦𝐚𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐫𝐞,
/start - 𝘊𝘰𝘮𝘮𝘢𝘯𝘥 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 𝘣𝘰𝘵 𝘰𝘳 𝘤𝘩𝘦𝘤𝘬 𝘸𝘩𝘦𝘵𝘩𝘦𝘳 𝘣𝘰𝘵 𝘪𝘴 𝘢𝘭𝘪𝘷𝘦.
/settings - 𝘊𝘰𝘮𝘮𝘢𝘯𝘥 𝘵𝘰 𝘤𝘰𝘯𝘧𝘪𝘨𝘶𝘳𝘦 𝘣𝘰𝘵'𝘴 𝘣𝘦𝘩𝘢𝘷𝘪𝘰𝘳
/set_watermark - 𝘊𝘰𝘮𝘮𝘢𝘯𝘥 𝘵𝘰 𝘢𝘥𝘥 𝘤𝘶𝘴𝘵𝘰𝘮 𝘸𝘢𝘵𝘦𝘳𝘮𝘢𝘳𝘬 𝘵𝘦𝘹𝘵 𝘵𝘰 𝘴𝘤𝘳𝘦𝘦𝘯𝘴𝘩𝘰𝘵𝘴.

👉  𝘌𝘹𝘢𝘮𝘱𝘭𝘦: /𝘴𝘦𝘵_𝘸𝘢𝘵𝘦𝘳𝘮𝘢𝘳𝘬 𝘸𝘢𝘵𝘦𝘳𝘮𝘢𝘳𝘬 𝘵𝘦𝘹𝘵.

__If issues persists contact my Boss.__"""


@ScreenShotBot.on_message(Filters.private & Filters.command("help"))
async def help(c, m):
    
    await m.reply_text(
        text=HELP_TEXT.format(m.from_user.first_name),
        quote=True
    )

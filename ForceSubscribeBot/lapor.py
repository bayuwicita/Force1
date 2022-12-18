from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("lapor"))
async def _lapor(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Here's How to Use Me **\n" + Data.LAPOR,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

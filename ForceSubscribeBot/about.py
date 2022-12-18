from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# About Message
@Client.on_message(filters.private & filters.incoming & filters.command("donasi"))
async def donasi(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "DONASI DISINI",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(callback_data="start"),
    )

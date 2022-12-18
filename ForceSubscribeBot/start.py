from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message):
	await bot.send_message(
		msg.chat.id,
		Data.START,
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	await bot.send_message(
		msg.chat.id,
		Data.START,
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
@Client.on_message(filters.command("goblok"))
async def goblok(client: Client, message: Message):
	await message.send_photo(
		"https://telegra.ph/file/591df41289c406ed4f248.jpg",
		caption="IniCaption",
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

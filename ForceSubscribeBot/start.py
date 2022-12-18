from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	await bot.send_photo(
		"msg.chat.id",
		"https://telegra.ph/file/591df41289c406ed4f248.jpg", 
		caption="CaptionNEW"
	)

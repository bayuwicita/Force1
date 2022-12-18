from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg, client: Client):
	user = await bot.get_me()
	mention = user["mention"]
	await msg.reply_photo(
		msg.chat.id,
		photo = "https://telegra.ph/file/591df41289c406ed4f248.jpg"
	)

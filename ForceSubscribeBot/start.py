from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg, client : Client, message : Message):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_photo(
		msg.chat.id,
		photo = "https://telegra.ph/file/ef7261e2a4bec533ec771.jpg"
		caption = "SOme Caption"
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

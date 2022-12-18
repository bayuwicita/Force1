from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
	await message.reply_photo(
		"https://telegra.ph/file/ef7261e2a4bec533ec771.jpg",
		caption="**Halo : GatauCaraTag \nSelamat datang di Bioskop Anime \n\nFitur Bot:** \n➥ __No Iklan.__\n➥ __Akses Sangat Mudah.__\n➥ __Bebas Streaming & Download.__\n\n**Enjoy !**",
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

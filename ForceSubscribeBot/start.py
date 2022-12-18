from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
	await message.reply_photo(
		"https://telegra.ph/file/1b04eb25d83788b169f73.jpg",
		caption=f"**Halo : {message.from_user.mention} \nSelamat datang di Anime Bot. \n\nFitur Bot:** \n➥ __No Iklan.__\n➥ __Akses Sangat Mudah.__\n➥ __Bebas Streaming & Download.__\n\n**Enjoy !**",
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

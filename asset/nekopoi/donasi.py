from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Start Message
@Client.on_message(filters.command("donasi"))
async def donasi(client: Client, message: Message):
	await message.reply_photo(
		"https://telegra.ph/file/e30beb5698d619b87218a.jpg",
		caption="**DONASI SEIKHLASNYA\n\nJika anda menyukai Bot kami dan ingin memberikan donasi serta dukungan kepada kami bisa dengan cara scan gambar kode QRIS diatas lalu input nilai yang ingin ditransfer.**",
	)

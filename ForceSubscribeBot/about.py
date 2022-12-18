from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# About Message
@Client.on_message(filters.private & filters.incoming & filters.command("donasi"))
async def donasi(client: Client, message: Message):
	await message.reply_photo(
		"https://telegra.ph/file/591df41289c406ed4f248.jpg",
		caption="**Jika anda menyukai Bot kami dan ingin memberikan donasi serta dukungan kepada kami bisa dengan cara scan gambar kode QRIS diatas lalu input nilai yang ingin ditransfer.**",
		disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
	)

import pyrogram
from os import getenv
from pyrogram.types import InlineKeyboardButton

class Data:
    # Start Message
    START = """
    
    CUMA TES AJA
        """
    
    START_IMG_URL = getenv(
        "START_IMG_URL",
        "image/donasi.jpg"
    )
    
    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 KEMBALI 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ SUPPORT CHANNEL ✨", url="https://t.me/NekoPoiSupport")],
        [
            InlineKeyboardButton("RATING", url="https://t.me/NekopoiSupport/9"),
            InlineKeyboardButton("DONASI", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
**Jika ada kendala atau ingin melaporkan link rusak bisa chat admin di [Channel NekoPoi](https://t.me/NekoPoiSupport).**
    """

    # About Message
    ABOUT = """
**DONASI** 

Jika anda menyukai Bot kami dan ingin memberikan donasi serta dukungan kepada kami bisa dengan cara scan gambar kode QRIS diatas lalu input nilai yang ingin ditransfer.
    """

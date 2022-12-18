import pyrogram
from os import getenv
from pyrogram.types import InlineKeyboardButton

class Data:
   
    # Home Button
    start_buttons = [
        [InlineKeyboardButton(text="🏠 KEMBALI 🏠", url="/start")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ SUPPORT CHANNEL ✨", url="https://t.me/NekoPoiSupport")],
        [
            InlineKeyboardButton("RATING", url="https://t.me/NekopoiSupport/9"),
            InlineKeyboardButton("DONASI", url="/donasi")
        ],
        [InlineKeyboardButton("❗ LAPOR LINK RUSAK ❗", url="/lapor")]
    ]

    # Help Message
    LAPOR = """
**Jika ada kendala atau ingin melaporkan link rusak bisa chat admin di [Channel NekoPoi](https://t.me/NekoPoiSupport).**
    """

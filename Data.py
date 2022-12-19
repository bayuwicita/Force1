import pyrogram
from os import getenv
from pyrogram.types import InlineKeyboardButton

class Data:
   
   # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="KEMBALI", callback_data="home")],
    ]
      
    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ SUPPORT CHANNEL ✨", url="https://t.me/NekoPoiSupport")],
        [
            InlineKeyboardButton("RATING", url="https://t.me/NekopoiSupport/9"),
            InlineKeyboardButton("DONASI", callback_data="donasi")
        ],
        [InlineKeyboardButton("❗ LAPOR LINK RUSAK ❗", callback_data="lapor")]
    ]


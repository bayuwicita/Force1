import pyrogram
from pyrogram.types import InlineKeyboardButton

class Data:
    # Start Message
    START = """
CUMA TEST DOANG
    """

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
**About This Bot** 

Channel this Bot : [Click Here](https://t.me/NekoPoiSupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @DreamFound
    """

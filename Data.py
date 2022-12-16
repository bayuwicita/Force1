import pyrogram
from pyrogram.types import InlineKeyboardButton

class Data:
    # Start Message
    START = await message.reply_photo(
    photo=https://telegra.ph/file/ef7261e2a4bec533ec771.jpg,
    caption=START,
    reply_markup=buttons
)
"""
CUMA TEST DOANG
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 KEMBALI 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ SUPPORT CHANNEL ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("RATING", url="https://t.me/NekopoiSupport/9"),
            InlineKeyboardButton("DONASI", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

✨ **Available Commands** ✨

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribing bot by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/ForceSubscribeBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """

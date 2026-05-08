from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import CHANNEL_ID, ADMINS


@Client.on_message(filters.video & filters.user(ADMINS))
async def auto_post(client, message):

    caption = """
🎬 New Movie Uploaded
📁 Quality: 720p
⭐ IMDb: 8.5
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 Buy File", callback_data="buy")]
    ])

    await client.send_video(
        CHANNEL_ID,
        video=message.video.file_id,
        caption=caption,
        reply_markup=buttons
    )

    await message.reply_text("Movie Posted Successfully")

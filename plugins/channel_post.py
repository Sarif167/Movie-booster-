from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import CHANNEL_ID, ADMINS

FILES_DB = {}

@Client.on_message((filters.video | filters.document) & filters.user(ADMINS))
async def auto_post(client, message):

    media_group_id = message.media_group_id

    if media_group_id:

        if media_group_id not in FILES_DB:
            FILES_DB[media_group_id] = []

        if message.video:
            FILES_DB[media_group_id].append(
                ("video", message.video.file_id)
            )

        elif message.document:
            FILES_DB[media_group_id].append(
                ("document", message.document.file_id)
            )

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "💳 Buy Full Pack",
                    callback_data=f"buy_{media_group_id}"
                )
            ]
        ])

        caption = f"""
🎬 New Movie Pack Uploaded

📦 Total Files: {len(FILES_DB[media_group_id])}

💰 One Payment = All Files
"""

        if len(FILES_DB[media_group_id]) == 1:

            if message.video:
                await client.send_video(
                    CHANNEL_ID,
                    video=message.video.file_id,
                    caption=caption,
                    reply_markup=buttons
                )

            else:
                await client.send_document(
                    CHANNEL_ID,
                    document=message.document.file_id,
                    caption=caption,
                    reply_markup=buttons
                )

    else:

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 Buy File", callback_data="buy_single")]
        ])

        caption = """
🎬 New Movie Uploaded
💰 Paid Content
"""

        if message.video:
            await client.send_video(
                CHANNEL_ID,
                video=message.video.file_id,
                caption=caption,
                reply_markup=buttons
            )

        else:
            await client.send_document(
                CHANNEL_ID,
                document=message.document.file_id,
                caption=caption,
                reply_markup=buttons
            )

    await message.reply_text("Files Added Successfully ✅")

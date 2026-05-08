caption = f"""
🎬 {message.video.file_name}

⭐ IMDb: 8.5
💰 Paid Content
"""

buttons = InlineKeyboardMarkup([
    [InlineKeyboardButton("💳 Buy File", callback_data="buy")]
])

thumb = None

if message.video and message.video.thumbs:
    thumb = message.video.thumbs[0].file_id

elif message.document and message.document.thumbs:
    thumb = message.document.thumbs[0].file_id

await client.send_photo(
    CHANNEL_ID,
    photo=thumb,
    caption=caption,
    reply_markup=buttons
)


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import FSUB_CHANNEL

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/MovieSearchAutoGroup")],
    ])

    await message.reply_text(
        "Welcome To Paid File Bot",
        reply_markup=buttons
    )


import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import QR_IMAGE, UPI_ID, ADMINS

PAID_USERS = {}

@Client.on_callback_query(filters.regex("buy"))
async def buy_handler(client, query):

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Send Screenshot", callback_data="send_ss")]
    ])

    await query.message.reply_photo(
        photo=QR_IMAGE,
        caption=f"Pay using UPI\n\n{UPI_ID}",
        reply_markup=buttons
    )

@Client.on_message(filters.photo)
async def payment_screenshot(client, message):

    user = message.from_user

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Approve",
                callback_data=f"approve_{user.id}"
            )
        ]
    ])

    for admin in ADMINS:
        await client.send_photo(
            admin,
            photo=message.photo.file_id,
            caption=f"New Payment Proof\n\nUser ID: {user.id}",
            reply_markup=buttons
        )

@Client.on_callback_query(filters.regex("approve"))
async def approve_user(client, query):

    user_id = int(query.data.split("_")[1])

    msg = await client.send_message(
        user_id,
        "Payment Approved ✅\nYour file access granted for 1 hour."
    )

    await asyncio.sleep(3600)

    try:
        await msg.delete()
    except:
        pass

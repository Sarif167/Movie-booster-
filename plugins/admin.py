
from pyrogram import Client, filters
from info import ADMINS

PREMIUM_USERS = set()

@Client.on_message(filters.command("premium") & filters.user(ADMINS))
async def add_premium(client, message):
    try:
        user_id = int(message.command[1])
        PREMIUM_USERS.add(user_id)
        await message.reply_text(f"Premium Added: {user_id}")
    except:
        await message.reply_text("Usage: /premium user_id")

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to any message")

    # Dummy user list
    users = [123456789]

    success = 0

    for user in users:
        try:
            await message.reply_to_message.copy(user)
            success += 1
        except:
            pass

    await message.reply_text(f"Broadcast Completed: {success}")

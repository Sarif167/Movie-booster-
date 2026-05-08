
from pyrogram import Client
from info import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "PaidFileBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

print("Bot Started Successfully")
app.run()

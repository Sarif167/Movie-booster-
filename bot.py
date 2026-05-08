from flask import Flask
from threading import Thread
from pyrogram import Client
from info import API_ID, API_HASH, BOT_TOKEN

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot Running Successfully"

def run_web():
    web_app.run(host="0.0.0.0", port=8080)

app = Client(
    "PaidFileBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

Thread(target=run_web).start()

print("Bot Started Successfully")
app.run()

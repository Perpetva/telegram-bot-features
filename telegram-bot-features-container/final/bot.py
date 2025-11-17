from pyrogram import Client

import os

api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")
bot_token = os.environ.get("bot_token")

app = Client(
    name = "session/bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

app.start()

try:
    app.send_message(
        chat_id="@mordomias",
        text="Hello, this is a test message from the bot!"
    )
    
    app.send_sticker(
        chat_id="@mordomias",
        sticker="sticker.webp"
    )
    
except Exception as e:
    print(f"Error: {e}")


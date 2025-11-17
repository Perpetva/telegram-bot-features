from pyrogram import Client, idle
from pyrogram.types import Message

import asyncio
import os

api_id = os.environ.get('api_id')
api_hash = os.environ.get('api_hash')
bot_token = os.environ.get('bot_token')


async def my_app():
    app = Client(
        name = "session/myapp",
        api_id = api_id,
        api_hash = api_hash,
        bot_token=bot_token
    )
    
    await app.start()
    
    info = await app.get_me()
    
    await app.send_message("@mordomias", f"{info.first_name} started in async mode.")
    return app

asyncio.run(my_app())


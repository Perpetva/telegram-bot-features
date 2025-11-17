from pyrogram import Client

app = Client(
    name = "perpetva_bot",
    api_id = 38976810,
    api_hash = "e6639fd91c4a19d39fde91a26cb1cc8d" 
)

app.start()

try:
    app.send_message(chat_id = "@mordomias", text = "Hello, World!")
except Exception as e:
    print(f"An error occurred: {e}")
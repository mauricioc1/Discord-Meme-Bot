from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_reponse

#load the environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#set up the bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#message functionality
async def send_message(message: Message, user_message: str):
    if not user_message:
        print("No message given")
        return
    
    try:
        response: str = get_reponse(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")

#handle the start of the bot by a user
@client.event
async def on_ready():
    print(f'{client.user} has connected to Maduro!')

#handling incoming messages
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    await send_message(message, message.content)

#main entry point
def main():
    client.run(token=TOKEN)
    
if __name__ == "__main__":
    main()

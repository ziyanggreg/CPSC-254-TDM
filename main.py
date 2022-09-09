# This example requires the 'message_content' intent.
#Yo

import discord
import os 
import dotenv
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

load_dotenv()
token = os.getenv('TOKEN')
client.run(token)
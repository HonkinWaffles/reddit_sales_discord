# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong')




##TODO
# 1. Scrape new posts from r/buildapcsales
  # Option: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
# 2. Send new posts to discord channel

# 3. Add a command to check for new posts








client.run(TOKEN)


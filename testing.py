# This example requires the 'message_content' intent.

import os
import discord
import praw
import pandas as pd
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')


REDDIT_SECRET=os.getenv('REDDIT_SECRET')
REDDIT_USER_AGENT=os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME=os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD=os.getenv('REDDIT_PASSWORD')

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


# Read-only instance
reddit_read_only = praw.Reddit(client_id=REDDIT_CLIENT_ID,		 # your client id
							client_secret=REDDIT_SECRET,	 # your client secret
							user_agent='REDDIT_USER_AGENT',	 # your user agent
                            username=REDDIT_USERNAME,     # your reddit username
                            password=REDDIT_PASSWORD)     # your reddit password

subreddit = reddit_read_only.subreddit("gaming")

for submission in subreddit.stream.submissions(skip_existing=True):
    print(submission.title)
    print(submission.url)





client.run(DISCORD_TOKEN)
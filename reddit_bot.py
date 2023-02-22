# This example requires the 'message_content' intent.

import os
import discord
from discord.ext import commands
import praw
from dotenv import load_dotenv
import asyncio

# Load the .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_SECRET=os.getenv('REDDIT_SECRET')
REDDIT_USER_AGENT=os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME=os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD=os.getenv('REDDIT_PASSWORD')

# Read-only instance
reddit_read_only = praw.Reddit(client_id=REDDIT_CLIENT_ID,		 # your client id
							client_secret=REDDIT_SECRET,	 # your client secret
							user_agent='REDDIT_USER_AGENT',	 # your user agent
                            username=REDDIT_USERNAME,     # your reddit username
                            password=REDDIT_PASSWORD,   # your reddit password
                            check_for_async=False)


subreddit = reddit_read_only.subreddit("gaming")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)


async def monitor_posts():
    reddit = await asyncpraw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT,
    )
    subreddit = await reddit.subreddit("gaming")
    channel = bot.get_channel(1077852017369813013)
    async for submission in subreddit.stream.submissions(skip_existing=True):
        await channel.send(submission.title)
        await channel.send(submission.url)
        print(submission.title)
        print(submission.url)


@client.event
async def on_ready():
    await client.wait_until_ready()  # Wait until the client is ready
    print('Logged in as {0.user}'.format(client))
    await monitor_posts()

bot.run(DISCORD_TOKEN)
import os
import discord
import asyncpraw
import praw
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

# Load the .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
REDDIT_SECRET=os.getenv('REDDIT_SECRET')
REDDIT_USER_AGENT=os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME=os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD=os.getenv('REDDIT_PASSWORD')

# List of words to exclude from the posts
exclusions = ['Case' , 'Controllers' , 'Keyboard' , 'Laptop' , 'Chargers' , 'Audio' , 'Headphones' , 'Headsets' , 'Earphones' , 'TV', 'buildapcsalescanada']

## Reddit API keys
reddit_read_only = praw.Reddit(client_id=REDDIT_CLIENT_ID,  # your client id
                            client_secret=REDDIT_SECRET,     # your client secret
                            user_agent='REDDIT_USER_AGENT',     # your user agent
                            username=REDDIT_USERNAME,     # your reddit username
                            password=REDDIT_PASSWORD,   # your reddit password
                            check_for_async=False)

# Discord API connection
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

# Streams new posts from the subreddit and sends them to the discord channel
async def monitor_posts():
    channel = client.get_channel(int(DISCORD_CHANNEL_ID))
    if not channel:
        print("Error: Could not find channel")
        return
    reddit = asyncpraw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT,
    )
    subreddit = await reddit.subreddit("bapcsalescanada")
    latest_post = None
    async for submission in subreddit.stream.submissions(skip_existing=True):
        print(submission.title)
        print(submission.url)
        if any(exclusion.lower() in submission.title.lower() for exclusion in exclusions):
            continue
        latest_post = submission
        await channel.send(submission.title)
        await channel.send(submission.url)
@client.event
async def on_ready():
    await client.wait_until_ready()  # Wait until the client is ready
    print('Logged in as {0.user}'.format(client))
    await monitor_posts()

@client.event
# Discord commannd !recent_sales - returns the latest post from the subreddit
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!recent_sales'):
        subreddit = reddit_read_only.subreddit("bapcsalescanada")
        latest_post = None
        for posts in subreddit.new(limit=5):
            if any(exclusion.lower() in posts.title.lower() for exclusion in exclusions):
                await message.channel.send("Exclusion found")
                await message.delete()
                continue
            latest_post = posts
            break
        if latest_post:
            await message.channel.send(posts.title)
            await message.channel.send(posts.url)
        await message.delete()
    # Discord commannd !top_5 - returns the top 5 posts from the subreddit
    elif message.content.startswith('!top_5'):
        subreddit = reddit_read_only.subreddit("bapcsalescanada")
        top_posts = subreddit.hot(limit=5)
        for post in top_posts:
            if any(exclusion.lower() in post.title.lower() for exclusion in exclusions):
                await message.channel.send("Exclusion found")
                await message.delete()
                continue
            await message.channel.send(post.title)
            await message.channel.send(post.url)
        await message.delete()
    # Discord commannd !help - returns the list of commands
    elif message.content.startswith('!help'):
        await message.channel.send("Commands: !recent_sales, !top_5")
        await message.delete()

client.run(DISCORD_TOKEN)
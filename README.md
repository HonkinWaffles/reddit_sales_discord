# /r/BAPCSalesCanada Discord Bot

This is a bot that monitors the /r/bapcsalescanada subreddit for new posts and pushes them to Discord. The bot is implemented in Python and uses the `asyncpraw` and `discord.py` libraries to interact with the Reddit and Discord APIs.



## Prerequisites

```
Python 3.6 or higher
A Reddit account
A Discord account
```
## Installation

1. Clone this repository:

```
git clone https://github.com/<your-github-username>/reddit-discord-bot.git
cd reddit-discord-bot
```

1. Install the dependencies:

```
pip install -r requirements.txt
```

1. Create a `.env` file in the project directory with the following contents:

```
DISCORD_TOKEN=<your-discord-bot-token>
REDDIT_CLIENT_ID=<your-reddit-client-id>
REDDIT_SECRET=<your-reddit-client-secret>
REDDIT_USER_AGENT=<your-reddit-user-agent>
REDDIT_USERNAME=<your-reddit-username>
REDDIT_PASSWORD=<your-reddit-password>
```

Replace the placeholders with your actual Discord bot token, Reddit client ID, client secret, user agent, username, and password. The REDDIT_USER_AGENT field should contain a unique name that describes your bot.

Edit the exclusions list in the reddit_bot.py file to exclude any terms you don't want to see in the posts.

## Usage

Run the bot with the following command:

```
python reddit_bot.py
```

The bot will start monitoring the `/r/bapcsalescanada` subreddit for new posts and pushing them to your Discord channel. If any excluded terms are found in the post title, the post will be skipped.

To get the latest post from the subreddit, type `!latest_post` in the Discord channel where the bot is running.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

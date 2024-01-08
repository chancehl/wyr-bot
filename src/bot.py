"""bot.py"""
import os
import discord
from dotenv import load_dotenv
from client import BotClient

# load environment variables
load_dotenv()


# configure intents
intents = discord.Intents.default()
intents.message_content = True

# run bot client
discord_client = BotClient(intents=intents)
discord_client.run(token=os.getenv("DISCORD_CLIENT_SECRET"))

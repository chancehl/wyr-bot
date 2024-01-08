"""bot.py"""
import os
import discord
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))


class BotClient(discord.Client):
    """Bot client"""

    async def on_ready(self):
        """Executes on startup"""
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        """Executes on message"""
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(os.getenv("DISCORD_CLIENT_SECRET"))

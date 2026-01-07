import discord
from discord.ext import tasks, commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")          # your bot token (GitHub secret)
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))   # forum channel ID

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bump_forum.start()

@tasks.loop(minutes=5)  # runs every 5 minutes
async def bump_forum():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        post = await channel.create_thread(name="Weekly bump", type=discord.ChannelType.public_thread, message=None)
        await post.send("Bump!")  # the content of the post
        # optional: delete after some time
        # await post.delete(delay=604800)  # deletes after 1 week (seconds)

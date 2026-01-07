import discord
from discord.ext import tasks, commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")          # Bot token
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))   # Forum channel ID

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bump_forum.start()

@tasks.loop(minutes=5)  # runs every 5 minutes
async def bump_forum():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found")
        return

    # Iterate over the last 5 threads/posts
    async for thread in channel.threads:
        if thread.archived:
            continue  # skip archived threads
        msg = await thread.send("Bump!")       # send message to the thread
        await msg.delete(delay=1)              # delete after 1 second

bot.run(TOKEN)

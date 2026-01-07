import discord
from discord.ext import tasks, commands
import os

# --- Configuration ---
TOKEN = os.getenv("DISCORD_TOKEN")          # Bot token
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))   # Forum channel ID
BUMP_MESSAGE = "Bump!"                       # Message content
DELETE_DELAY = 1                             # Seconds before deleting message
INTERVAL_MINUTES = 5                         # How often to bump

# --- Bot Setup ---
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Background Task ---
@tasks.loop(minutes=INTERVAL_MINUTES)
async def bump_forum():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found")
        return

    # Iterate over all active threads in the forum channel
    for thread in channel.threads:
        if thread.archived:
            continue  # skip archived threads
        try:
            msg = await thread.send(BUMP_MESSAGE)
            await msg.delete(delay=DELETE_DELAY)
            print(f"Bumped thread: {thread.name}")
        except Exception as e:
            print(f"Failed to bump thread {thread.name}: {e}")

# --- Start Bot ---
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bump_forum.start()

bot.run(TOKEN)

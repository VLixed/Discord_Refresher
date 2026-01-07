import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BUMP_MESSAGE = "Bump!"      # message to refresh posts
DELETE_DELAY = 1            # seconds before deleting

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

async def main():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")
        channel = client.get_channel(CHANNEL_ID)
        if not channel:
            print("Channel not found")
            await client.close()
            return

        # Iterate all active threads in the forum channel
        for thread in channel.threads:
            if thread.archived:
                continue
            try:
                msg = await thread.send(BUMP_MESSAGE)
                await msg.delete(delay=DELETE_DELAY)
                print(f"Bumped thread: {thread.name}")
            except Exception as e:
                print(f"Failed to bump thread {thread.name}: {e}")

        await client.close()  # disconnect after finishing

    await client.start(TOKEN)

# Run
asyncio.run(main())

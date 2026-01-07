import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BUMP_MESSAGE = "Bump!"       # temporary bump message
DELETE_DELAY = 1             # seconds to wait before deletion
RETRY_DELAY = 1               # seconds between delete retries
MAX_RETRIES = 5               # max attempts to delete a message

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

        bump_messages = []

        # Loop all active threads
        for thread in channel.threads:
            if thread.archived:
                continue
            try:
                msg = await thread.send(BUMP_MESSAGE)
                bump_messages.append(msg)
                print(f"Bumped thread: {thread.name}")
            except discord.Forbidden:
                print(f"Cannot send messages in thread {thread.name}")
            except Exception as e:
                print(f"Failed to bump thread {thread.name}: {e}")

        # Wait for delete delay to ensure messages exist
        await asyncio.sleep(DELETE_DELAY)

        # Delete all bump messages with retries
        for msg in bump_messages:
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    await msg.delete()
                    break
                except discord.Forbidden:
                    print(f"Cannot delete message in thread {msg.channel.name} (check permissions)")
                    break
                except Exception:
                    if attempt < MAX_RETRIES:
                        await asyncio.sleep(RETRY_DELAY)
                    else:
                        print(f"Failed to delete message in thread {msg.channel.name} after {MAX_RETRIES} attempts")

        await client.close()
        print("All bump messages processed. Bot disconnected.")

    await client.start(TOKEN)

asyncio.run(main())

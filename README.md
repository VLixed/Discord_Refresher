Weekly Discord Forum Bump Bot
=============================

Description:
-------------
This Python bot automatically refreshes all active threads in a Discord forum channel by sending a temporary "Bump!" message and deleting it. 
It is designed to be run on GitHub Actions once a week, keeping forum posts active without leaving any permanent messages.

Features:
---------
- Bumps all active threads in a specified forum channel
- Deletes bump messages automatically after a short delay
- Configured to run weekly via GitHub Actions
- Fully automated, no manual intervention required

Requirements:
-------------
- A Discord bot with:
  - Send Messages permission in the forum channel
  - Manage Messages permission in the forum channel
- GitHub repository to host the workflow

Setup Instructions:
------------------
1. Add the bot to your Discord server and ensure it has the required permissions.
2. Copy the bot token and forum channel ID.
3. Create a GitHub repository and add the following files:
   - bump.py          (the Python script)
   - .github/workflows/weekly_bump.yml  (the GitHub Actions workflow)
4. Add repository secrets:
   - DISCORD_TOKEN : your bot token
   - CHANNEL_ID    : numeric ID of your forum channel
5. Run the workflow via GitHub Actions which will run weekly according to the cron schedule in weekly_bump.yml.

Configuration:
--------------
- In bump.py:
  - BUMP_MESSAGE: text of the temporary bump message
  - DELETE_DELAY: seconds to wait before deleting bump messages
  - MAX_RETRIES: maximum delete attempts for failed messages
  - RETRY_DELAY: seconds to wait between delete retries

- In weekly_bump.yml:
  - Adjust the cron schedule to your preferred day/time (UTC)

Notes:
------
- The bot only affects active threads; archived threads are skipped.
- Make sure GitHub Actions workflow has enough runtime to allow message deletion.
- All bump messages are automatically removed, so the forum stays clean.

License:
--------
Free to use, modify, and distribute. Use responsibly and ensure you have permissions on the Discord server.
If you wanna support me, you can paypal me (midou.belouedhnine@gmail.com) and thanks!

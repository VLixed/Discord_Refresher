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
1. **Copy the repository**  
   - Fork or clone this repository to your own GitHub account.  
   - This will give you your own copy of the code and workflow.

2. **Create your own Discord bot**  
   - Add the bot to your server and ensure it has the required permissions:  
     - Send Messages ✅  
     - Manage Messages ✅
     - View Channels ✅
   - Copy the bot token and the forum channel ID.

3. **Configure your repository secrets**  
   - Go to your forked repository → Settings → Secrets and Variables → Actions  
   - Add the following secrets:  
     - `DISCORD_TOKEN` : your bot token  
     - `CHANNEL_ID`    : numeric ID of your forum channel

4. **Adjust workflow if needed**  
   - The workflow file `.github/workflows/weekly_bump.yml` is already set to run weekly.  
   - You can modify the cron schedule or trigger it manually via GitHub Actions.

5. **Run the workflow**  
   - GitHub Actions will run the bot according to your schedule, bump all threads, and delete bump messages automatically.  


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
- The bot only affects active posts; archived ones are skipped.
- Make sure GitHub Actions workflow has enough runtime to allow message deletion.
- All bump messages are automatically removed, so the forum stays clean.

License:
--------
Free to use, modify, and distribute. Use responsibly and ensure you have permissions on the Discord server.
If you wanna support me, you can paypal me (midou.belouedhnine@gmail.com) and thanks!

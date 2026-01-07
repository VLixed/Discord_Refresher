name: Weekly Bump

on:
  schedule:
    - cron: '0 12 * * 1'  # Every Monday at 12:00 UTC
  workflow_dispatch:    # Allows manual run

jobs:
  bump:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install requests
        run: pip install requests
      - name: Run bump script
        run: python bump.py
        env:
          WEBHOOK_URL: ${{ secrets.WEBHOOK_URL }}
          API_KEY: ${{ secrets.API_KEY }}

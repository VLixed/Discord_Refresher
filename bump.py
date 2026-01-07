import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1458522312310657231/M7IiNGD277ZDsEtNQzYY2m1qsvBFyZmVIcU0pgv10vXiHdva4ZKJJD-WrD6Pa3KfMFJ2"
MESSAGE = "Weekly bump!"

requests.post(WEBHOOK_URL, json={"content": MESSAGE})

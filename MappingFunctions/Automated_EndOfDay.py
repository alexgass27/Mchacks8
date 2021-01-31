from slack import WebClient
from managerbot import ManagerBot
import os
import xlrd
import time
from datetime import datetime, timedelta

slack_web_client = WebClient(token=os.environ.get("BOT_USER_TOKEN"))

while True:
#def funcSend():
    # Create a slack client


    # Get a new CoinBot
    manager_bot = ManagerBot("#general")

    # Get the onboarding message payload
    message = manager_bot.get_automated_late_message_payload()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)
    time.sleep(86400)

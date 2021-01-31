from slack import WebClient
from managerbot import ManagerBot
import os
import xlrd
#from datetime import datetime, timedelta
#from threading import Timer


# Create a slack client
slack_web_client = WebClient(token=os.environ.get("BOT_USER_TOKEN"))
print(os.environ.get("BOT_USER_TOKEN"))
# Get a new CoinBot
manager_bot = ManagerBot("#general")

# Get the onboarding message payload
message = manager_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)

#x=datetime.today()
#y=x.replace(day=x.day, hour=6, minute=53, second=0, microsecond=0) + timedelta(days=0)

#delta_t=y-x

#secs=delta_t.total_seconds()

#t = Timer(secs, funcSend())
#t.start()

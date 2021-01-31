# import the random library to help us generate the random numbers
import random

#import xlrd

#locc = ("/Users/mike/Desktop/McHacks8/Excel/EmployeeDataNew.xls")

#wbb = xlrd.open_workbook(locc)
#sheett = wbb.sheet_by_index(0)

#sheett.cell_value(0,0)
#names = []
#tasks = []
#duedates = []

#for i in range(sheett.nrows):
    #names.append(sheett.cell_value(i,0))
    #tasks.append(sheett.cell_value(i,1))
    #duedates.append(str(sheett.cell_value(i,2)))


import pymongo


client = pymongo.MongoClient("mongodb+srv://amv:mchacks8@cluster0.jweue.mongodb.net/test?retryWrites=true&w=majority")
db = client.Employee_Data

collection = db['task_info']
dataList = collection.find()
x = []
#assigned = []

for item in dataList:
    assigned = ""
    for data in item["Tasks"]:
        assigned = assigned + str(data) + ", "
    #print("Task: " + item["task"] + " Employees: " + assigned + " Due Date: " + str(item["due_date"]))
    assigned = assigned[:-2]
    x.append("Name: " + item["Name"] + "\n" + " Project:  " + item["Project"] + "\n" + "Tasks: " + assigned + "\n")

#for item in dataList:
    #print("Task: " + item["task"] + " Employees: " + str(item["employees"]) + " Due Date: " + str(item["due_date"]))
    #x.append("Task: " + item["task"] + "\n" + " Employees: " + str(item["employees"]) + "\n" + " Due Date: " + str(item["due_date"]) + "\n")

class ManagerBot:

    # Create a constant that contains the default text for the message
    ADD_ME = {
        "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Good morning everybody, these are everyone's schedules for today!"
                ),
            },
        }


    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Generate a random number to simulate flipping a coin. Then return the
    # crafted slack payload with the coin flip message.
    def _add_nums(self):
        results = "1 + 1 = 2"
        #text = []
        #for i in range(1,5):
            #text.append("Name: " + names[i] + " Task: " + tasks[i] + " Due Date: " + duedates[i])

        text = f"The result is {results}"

        #newtext = str(text)
        return {"type": "section", "text": {"type": "mrkdwn", "text": x[0] + x[1] + x[2] + x[3] + x[4] + x[5]}},


    Status_Update = {
        "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hi everybody, hope everyone's day went well! Please give me a status update of where you are at on your work."
                ),
            },
        }


    # Craft and return the entire message payload as a dictionary.
    def get_automated_early_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.ADD_ME,
                *self._add_nums(),
            ],
        }

    def get_automated_late_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.Status_Update,
            ],
        }

# sends a good morning text to a particular phone number every day
# need to use two modules for this (schedule and requests)

import schedule
import time
import requests
import schedule

# for security reasons, I hide my phone number in a separate file in a variable called phone_number
from credentials import phone_number


# function to send message
def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'Good morning handsome :)',
        'key': 'textbelt'
    })
    print(resp.json())


# schedules when the message should be ran everyday, but I can change its properties
schedule.every().day.at('07:00').do(send_message())

while True:
    schedule.run_pending()
    time.sleep(1)

from gtts import gTTS
from playsound import playsound
import os
import time
import datetime
import schedule
import random
import requests

global message
message = ''


def say_something():
    global message
    text = (requests.get('http://my-json-server.typicode.com/subhojit-ghosh/demo-api/message')).json()['title']
    if message != text:

        message = text
        language = 'en'
        speech = gTTS(text=text, lang=language, slow=False)
        filename = str(random.randint(1, 1000))+'.mp3'
        speech.save(filename)
        playsound(filename)
        os.remove(filename)
        print('finished')


# print(datetime.datetime(2019, 7, 12, 00, 00, 5).strftime('%S'))

# print((requests.get('http://my-json-server.typicode.com/subhojit-ghosh/demo-api/message')).json()['title'])


while True:
    say_something()
    # time.sleep(1)

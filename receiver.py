from pynput.keyboard import Key, Controller,KeyCode
from flask import Flask, request
import sys
import datetime

start_time = None

app = Flask(__name__)


@app.route("/sendKey")
def sendStartTime():
    key = request.args.get('key')
    key = int(key)
    key_code = KeyCode(key)
    print("Received:  ",key )
    return "ok"



def input_key():

    keyboard = Controller()

    # Press and release space
    keyboard.press(KeyCode(vk=55))
    keyboard.press(KeyCode(vk=49))

    keyboard.release(KeyCode(vk=55))
    keyboard.release(KeyCode(vk=49))
    
if __name__ == "__main__":
    input_key()
    #app.run("0.0.0.0","2533")

from pynput.keyboard import Key, KeyCode
from pynput import keyboard,mouse
from flask import Flask, request
import sys
import datetime
import csv


keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()

mac_to_win_key_code_map = {

}

def build_key_code_map():
    with open('keyCodes.csv') as csvfile:
        all_rows = csv.reader(csvfile, delimiter=',')

        for row in all_rows:
            try:
                mac_code = int(row[1])
                win_code = int(row[2])
                mac_to_win_key_code_map[mac_code]=win_code
            except ValueError:
                continue

app = Flask(__name__)




@app.route("/sendKey")
def handle_send_key():
    key_code_mac = int(request.args.get('key_code'))
    key_code_win = mac_to_win_key_code_map[key_code_mac]
    key_code_obj = KeyCode(key_code_win)

    action = request.args.get('action')
    if action == "press":
        keyboard_controller.press(key_code_obj)
    else:
        keyboard_controller.release(key_code_obj)

    print("Received Keyboard:  ",key_code_mac,"  ",key_code_win,"  ",action )
    return "ok"




@app.route("/sendMouseMove")
def handle_send_mouse_move():
    dx = float(request.args.get('dx'))
    dy = float(request.args.get('dy'))
    mouse_controller.move(dx,dy)

    return "ok"


@app.route("/sendMouseClick")
def handle_send_mouse_click():
    side = request.args.get("side")
    action = request.args.get("action")
    if side =="l":
        btn = mouse.Button.left
    if side=="r":
        btn = mouse.Button.right
    if action == "press":
        mouse_controller.press(btn)
    if action == "release":
        mouse_controller.release(btn)



    return "ok"




if __name__ == "__main__":
    #input_key()
    
    build_key_code_map()
    app.run("0.0.0.0","2533")

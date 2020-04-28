from pynput import keyboard,mouse

import threading
import signal
import sys
import json
import requests 

def signal_handler(sig, frame):
    pass
signal.signal(signal.SIGINT, signal_handler)

receiver_url = ""



def send_key(key,action):
    params = {
        "key_code":key,
        "action":action
    }
    send_key_url = "http://"+receiver_url+"/sendKey"
    r = requests.get(url = send_key_url, params = params)
    result = r.text
    print(result)
    if result == "ok":
        r.close()
    else:
        print("send key failed")
        r.close()
        sys.exit(0)
        return False


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.vk))
        send_key(key.vk,"press")
    except AttributeError:
        print('special key {0} pressed'.format(key.value.vk))
        send_key(key.value.vk,"press")

def on_release(key):
    try:
        print('alphanumeric key {0} released'.format(key.vk))
        send_key(key.vk,"release")
    except AttributeError:
        print('special key {0} released'.format(key.value.vk))
        send_key(key.value.vk,"release")





def send_mouse_move(dx,dy):
    params = {
        "dx":dx,
        "dy":dy
    }
    send_url = "http://"+receiver_url+"/sendMouseMove"
    r = requests.get(url = send_url, params = params)
    result = r.text
    print(result)
    if result == "ok":
        r.close()
    else:
        print("send mouse move failed")
        r.close()
        sys.exit(0)
        return False

last_x = None
last_y = None

def on_move(x, y):
    global last_x
    global last_y
    if last_x!=None and last_y!=None:
        dx = x-last_x
        dy = y-last_y
        if abs(dx) > 5 and abs(dy) > 5:
            print("sending mouse move ",dx,dy)
            send_mouse_move(dx,dy)
            last_x = x
            last_y = y
    else:
        last_x = x
        last_y = y






def send_mouse_click(button_side,action):
    params = {
        "side":button_side,
        "action":action
    }
    send_url = "http://"+receiver_url+"/sendMouseClick"
    r = requests.get(url = send_url, params = params)
    result = r.text
    print(result)
    if result == "ok":
        r.close()
    else:
        print("send mouse click failed")
        r.close()
        sys.exit(0)
        return False


def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        button_side = "r"
    if button == mouse.Button.left:
        button_side = "l"
    if pressed:
        action = "press"
    else:
        action = "release"
    print("sending mouse click ",button_side,action)
    send_mouse_click(button_side,action)

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))



def start_collection():
    key_listener =  keyboard.Listener(on_press=on_press,on_release=on_release,suppress=True)
    mouse_listener = mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll,suppress=True)

    key_listener.start()
    mouse_listener.start()

    key_listener.join()
    mouse_listener.join()

if __name__ == "__main__":
    receiver_url = sys.argv[1]
    #input_key()
    start_collection()
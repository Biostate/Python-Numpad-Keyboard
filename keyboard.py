from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import time
import platform


keyboardController = Controller()
osName = platform.system()

print('Init. You are running on: ' + osName)

lastKey = None
lastKeyStrike = 0
lastKeyStrokeTime = ts = time.time()
numpad = {
    "0": (' '),
    "1": ('.', ',', '?', '!'),
    "2": ('a', 'b', 'c', 'ç'),
    "3": ('d', 'e', 'f'),
    "4": ('g', 'h', 'i', 'ı'),
    "5": ('j', 'k', 'l'),
    "6": ('m', 'n', 'o', 'ö'),
    "7": ('p', 'q', 'r', 's', 'ş'),
    "8": ('t', 'u', 'v', 'ü'),
    "9": ('w', 'x', 'y', 'z'),
}


def on_release(key):
    global lastKeyStrike
    global lastKeyStrokeTime
    global lastKey
    currentKey = None
    print('{0} release'.format(key))
    if key == Key.esc:
        return False

    if osName == "Windows":
        if hasattr(key, 'vk') and key.vk != None and 96 <= key.vk <= 105:
            currentKey = str(key.vk - 96)

    if osName == "Linux":  
        if hasattr(key, 'vk') and key.vk != None and key.vk == 65437:
            currentKey = "5"
        elif hasattr(key, 'char') and key.char != None and key.char.isnumeric():
                if 0 <= int(key.char) <= 9:
                    currentKey = key.char

    """ if currentKey is a number """
    if currentKey != None:
        print("You pressed: " + str(currentKey))
        keyboardController.tap(Key.backspace)

        """ check time """
        if time.time() - lastKeyStrokeTime > 0.5:
            lastKey = None

        """ check if same key pressed """
        if lastKey == currentKey:
            print("You pressed the same key")
            lastKeyStrike += 1
            keyboardController.tap(Key.backspace)

        if lastKey != currentKey:
            print("You pressed a different key")
            lastKeyStrike = 0

        if lastKeyStrike >= len(numpad[currentKey]):
            lastKeyStrike = 0

        print(numpad[currentKey][lastKeyStrike]);
        keyboardController.tap(numpad[currentKey][lastKeyStrike])

        """ update last key and time """
        lastKey = currentKey
        lastKeyStrokeTime = time.time()


with Listener(on_release=on_release) as listener:
    listener.join()
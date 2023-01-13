""" import keyboard  # using module keyboard """
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import time

keyboardController = Controller()

print('Init')

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


with keyboard.Events() as events:
    for event in events:
        key = event.key
        currentKey = None

        if event.key == keyboard.Key.esc:
            break
        elif event.key == keyboard.Key.backspace:
            print('backspace pressed')
        else:
            if isinstance(event, keyboard.Events.Press):
                print('Started: {0} pressed'.format(key))

                """ this is necessary to Windows and Linux differences """
                if hasattr(key, 'vk') and key.vk != None and 96 <= key.vk <= 105:
                    currentKey = str(key.vk - 96)
                elif hasattr(key, 'char') and key.char != None and key.char.isnumeric():
                    """ This checks for Linux """
                    if 0 <= int(key.char) <= 9:
                        currentKey = key.char

                if currentKey != None:
                    print("You pressed: " + str(currentKey))
                    keyboardController.tap(Key.backspace)

                    if time.time() - lastKeyStrokeTime > 0.5:
                        lastKey = None

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

                    """ update last key """
                    lastKey = currentKey
                    lastKeyStrokeTime = time.time()
from PIL import ImageGrab
from pynput import keyboard, mouse

import time
import os

keyboardController = keyboard.Controller()
mouseController = mouse.Controller()

inputSleep = 0.01
pageWaitSleep = 2

top = 0
right = 0
bottom = 0
left = 0

# ------ START OF SECTION ------
keyStatuses = {}
def on_press(key):
    if(type(key) == keyboard.Key):
        keyStatuses[str(key)] = True
    else:
        keyStatuses[str(key.char)] = True
    
def on_release(key):
    if(type(key) == keyboard.Key):
        keyStatuses[str(key)] = False
    else:
        keyStatuses[str(key.char)] = False
    
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# like keyboard.wait
# but continues if not pressed
# and doesn't register multiple strokes if held
def detectPress(keycode):
    if keycode not in keyStatuses:
        return False

    if keyStatuses[keycode] == False:
        return False

    while keyStatuses[keycode]:
        time.sleep(inputSleep)

    return True
# ------ END OF SECTION ------

def inputInteger():
    while True:
        try:
            return int(input())
        except:
            print("not a valid integer")
    

print("Lets start with the rough coordinates.")

print("Move your mouse to the top left corner and press ctrl")
while not detectPress("Key.ctrl"):
    time.sleep(inputSleep)
topLeft = mouseController.position
left = topLeft[0]
top = topLeft[1]

print("Move your mouse to the bottom Right corner and press ctrl")
while not detectPress("Key.ctrl"):
    time.sleep(inputSleep)
bottomRight = mouseController.position
right = bottomRight[0]
bottom = bottomRight[1 ]

print()
print("Now for fine adjustment. Use WASD to move the top left corner and the ARROW KEYS to move the bottom right corner.")
print("SHIFT to take new targeting image.")
print("CTRL to confirm.")

image = ImageGrab.grab((left, top, right, bottom))
image.save("targeting-image.png")

changed = True
while True:
    if detectPress("Key.ctrl"):
        break

    if detectPress('w'):
        changed = True
        top -= 1

    if detectPress('a'):
        changed = True
        left -= 1

    if detectPress('s'):
        changed = True
        top += 1

    if detectPress('d'):
        changed = True
        left +=1

    if detectPress("Key.up"):
        changed = True
        bottom -= 1

    if detectPress("Key.left"):
        changed = True
        right -= 1

    if detectPress("Key.down"):
        changed = True
        bottom += 1

    if detectPress("Key.right"):
        changed = True
        right +=1

    if detectPress("Key.shift"):
        image = ImageGrab.grab((left, top, right, bottom))
        image.save("targeting-image.png")

    if changed:
        changed = False
        print("top: " + str(top) + "right: " + str(right) + "bottom: " + str(bottom) + "left: " + str(left))
    
    time.sleep(inputSleep)



print("name the folder to save to")
folderName = ""
while folderName == "":
    folderName = input()

print("now input number of pages")
pages = inputInteger()

print("select ebook tab and press ctrl")
while not detectPress("Key.ctrl"):
    time.sleep(inputSleep)

os.mkdir(folderName)
for page in range(pages):
        print("page " + str(page+1) + " / " + str(pages))
        image = ImageGrab.grab((left, top, right, bottom))
        image.save(folderName + "/" + str(page) + ".png")
        keyboardController.press(keyboard.Key.page_down)
        keyboardController.release(keyboard.Key.page_down)
        time.sleep(pageWaitSleep)
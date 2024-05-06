import pyautogui
import keyboard
import time
import os

inputSleep = 0.01

top = 0
right = 0
bottom = 0
left = 0

# like keyboard.wait
# but continues if not pressed
# and doesn't register multiple strokes if held
def detectPress(keycode):
    pressDetected = False
    while keyboard.is_pressed(keycode):
        time.sleep(0.01)
        pressDetected = True

    return pressDetected

def inputInteger():
    while True:
        try:
            return int(input())
        except:
            print("not a valid integer")
    

print("Lets start with the rough coordinates.")

print("Move your mouse to the top left corner and press ctrl")
while not detectPress("ctrl"):
    time.sleep(inputSleep)
topLeft = pyautogui.position()
top = topLeft.y
left = topLeft.x

print("Move your mouse to the bottom Right corner and press ctrl")
while not detectPress("ctrl"):
    time.sleep(inputSleep)
bottomRight = pyautogui.position()
bottom = bottomRight.y
right = bottomRight.x

print()
print("Now for fine adjustment. Use WASD to move the top left corner and the ARROW KEYS to move the bottom right corner.")
print("SHIFT to take new targeting image.")
print("CTRL to confirm.")

image = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
image.save("targeting-image.png")

changed = True
while True:

    if detectPress("ctrl"):
        break

    if detectPress("w"):
        changed = True
        top -= 1

    if detectPress("a"):
        changed = True
        left -= 1

    if detectPress("s"):
        changed = True
        top += 1

    if detectPress("d"):
        changed = True
        left +=1

    if detectPress("up"):
        changed = True
        bottom -= 1

    if detectPress("left"):
        changed = True
        right -= 1

    if detectPress("down"):
        changed = True
        bottom += 1

    if detectPress("right"):
        changed = True
        right +=1

    if detectPress("shift"):
        image = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
        image.save("targeting-image.png")

    if changed:
        changed = False
        print("top: " + str(top) + "right: " + str(right) + "bottom: " + str(bottom) + "left: " + str(left))



print("name the folder to save to")
folderName = ""
while folderName == "":
    folderName = input()

print("now input number of pages")
pages = inputInteger()

print("select ebook tab and press ctrl")
while not detectPress("ctrl"):
    time.sleep(inputSleep)

os.mkdir(folderName)
for page in range(pages):
        print("page " + str(page+1) + " / " + str(pages))
        image = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
        image.save(folderName + "/" + str(page) + ".png")
        keyboard.press("pagedown")
        keyboard.release("pagedown")
        time.sleep(2)
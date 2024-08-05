import pyautogui
import time

checkbox_image = 'checkbox1.png'

def scroll_down(amount):
    pyautogui.scroll(-amount)

time.sleep(3)

# limit to prevent infinite scrolling in case something goes wrong
scroll_limit = 100
scroll_count = 0

while scroll_count < scroll_limit:
    # locates all instances of the checkbox on the screen
    checkboxes = list(pyautogui.locateAllOnScreen(checkbox_image, confidence=0.9))

    if not checkboxes:
        # If no checkboxes are found and we've scrolled too many times --> break the loop
        scroll_count += 1
        if scroll_count >= scroll_limit:
            print("Reached the scroll limit. Exiting...")
            break

        scroll_down(900)
        time.sleep(1)
        continue

    # If checkboxes are found, click on each
    for checkbox in checkboxes:
        pyautogui.click(pyautogui.center(checkbox))
        time.sleep(0.1)

    # Scroll down to load more checkboxes
    scroll_down(800)
    time.sleep(1)

    scroll_count += 1

print("Finished checking all checkboxes or reached the scroll limit.")

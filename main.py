import pyautogui
import time

# Path to the reference image of the unchecked checkbox
checkbox_image = 'checkbox1.png'

# Function to scroll the page
def scroll_down(amount):
    pyautogui.scroll(-amount)

# Give time to switch to the browser window
time.sleep(3)

# Set a limit to prevent infinite scrolling in case something goes wrong
scroll_limit = 100  # Set an appropriate limit for your use case

# Track the number of times we have scrolled
scroll_count = 0

while scroll_count < scroll_limit:
    # Locate all instances of the checkbox on the screen
    checkboxes = list(pyautogui.locateAllOnScreen(checkbox_image, confidence=0.9))

    if not checkboxes:
        # If no checkboxes are found and we've scrolled too many times, break the loop
        scroll_count += 1
        if scroll_count >= scroll_limit:
            print("Reached the scroll limit. Exiting...")
            break

        # Scroll down and continue searching
        scroll_down(900)  # Adjust the scroll amount as needed
        time.sleep(1)  # Adjust time for the page to load more checkboxes
        continue

    # If checkboxes are found, click on each
    for checkbox in checkboxes:
        pyautogui.click(pyautogui.center(checkbox))
        time.sleep(0.1)  # Slight delay for visual confirmation

    # Scroll down to load more checkboxes
    scroll_down(800)  # Adjust the scroll amount as needed
    time.sleep(1)  # Adjust time for the page to load more checkboxes

    # Increment the scroll count
    scroll_count += 1

print("Finished checking all checkboxes or reached the scroll limit.")
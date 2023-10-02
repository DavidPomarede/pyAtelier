# importing pyautogui
import pyautogui
pyautogui.click()
# initialising a variable distance
distance = 200
  
  
while (distance):
    # moves the cursor to the right
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 5
    # move the cursor down
    pyautogui.dragRel(0, distance, duration=0.2)
    # move the cursor to the left
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 5
    # move the cursor up
    pyautogui.dragRel(0, -distance, duration=0.2)

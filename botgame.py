from pynput.keyboard import Key, Controller
from keyboard import press
import time
import pyautogui
keyboard = Controller()
time.sleep(2)
for x in range(1):
	time.sleep(.1)
	for x in range(1):
		keyboard.type("pls deposit all")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls inventory 1")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls inventory 2")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls inventory 3")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls inventory 4")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls inventory 5")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls multiplier")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls pet list 1")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls pet list 2")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls pet list 3")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls quests list 1")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls quests list 2")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls quests list 3")
		pyautogui.press('enter')
		time.sleep(1)
		keyboard.type("pls rich")
		pyautogui.press('enter')
		time.sleep(33)
		keyboard.type("pls beg")
	keyboard.type("pls hourly")
	pyautogui.press('enter')
	time.sleep(1)
	keyboard.type("pls profile")
	pyautogui.press('enter')
	

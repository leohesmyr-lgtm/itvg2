import mouse
import keyboard
import time

bortover = 200
nedover = 350

mouse.move(bortover,nedover)

while(True):
	time.sleep(0.1)
	mouse.click("left")
	if keyboard.is_pressed('esc'):
		break;


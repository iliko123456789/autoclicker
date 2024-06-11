import threading
import pyautogui
from pynput import keyboard

auto_clicker_running = False

def auto_clicker():
    while auto_clicker_running:
        pyautogui.click()
        pyautogui.PAUSE = 0.01  # Pause duration between clicks

def on_press(key):
    global auto_clicker_running

    try:
        # Check if the '1' key is pressed
        if key.char == '1':
            if not auto_clicker_running:
                auto_clicker_running = True
                thread = threading.Thread(target=auto_clicker)
                thread.start()
            else:
                auto_clicker_running = False
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#import pyvjoy
import keyboard

keyboard.add_hotkey('space', lambda: print("space was pressed"))
keyboard.wait
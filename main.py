import pyvjoy
import keyboard

keyboard.add_hotkey('space', lambda: print("space was pressed"))
keyboard.add_hotkey('w', lambda: print("w was pressed"))
keyboard.wait()

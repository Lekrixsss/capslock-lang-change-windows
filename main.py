from pynput import keyboard

cmb = [{keyboard.Key.caps_lock}]

current = set()
def execute():
    print("Detected hotkey")

def on_press(key):
    if any([key in z for z in cmb]):
        current.add(key)
        if any(all(k in current for k in z) for z in cmb):
            execute()

def on_release(key):
    if any([key in z for z in cmb]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
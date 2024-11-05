import ctypes
import pyautogui
import time
import random
from tkinter import messagebox, Tk

# Hide Tkinter main window
root = Tk()
root.withdraw()

def show_error_message():
    """Displays a random error message."""
    messages = [
        "Fatal Error: Something went horribly wrong!",
        "System32 is missing! Please contact support.",
        "Error 404: Keyboard not found. Press F1 to continue.",
        "Virus Detected! Removing C:/ drive...",
        "Blue Screen Error: Please restart your computer.",
    ]
    messagebox.showerror("Error", random.choice(messages))

def fake_bsod():
    """Displays a fake BSOD (Blue Screen of Death) effect."""
    ctypes.windll.user32.MessageBoxW(0, "A problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nPress any key to restart your system.", "Blue Screen of Death", 0x10 | 0x30)

    # Start fake "restart" animation
    for i in range(5, 0, -1):
        pyautogui.alert(f"Restarting in {i} seconds...")
        time.sleep(1)

    pyautogui.alert("System has successfully restarted.")

def main():
    while True:
        time.sleep(random.randint(10, 30))  # Delay between messages
        if random.choice([True, False]):
            show_error_message()
        else:
            fake_bsod()

if __name__ == "__main__":
    main()

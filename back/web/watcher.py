import pyperclip
import os
import time
import keyboard
import threading
import subprocess
from colorama import Fore, Style, Back

print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "" + Style.RESET_ALL)

def handle_clipboard():
    while True:
        try:
            clipboard_text = pyperclip.paste()
            if clipboard_text.startswith("@flux:"):
                stripped_text = clipboard_text[7:]
                with open("C:\\FluxUI\\temp\\input.txt", "w", encoding="utf-8") as f:
                    f.write(stripped_text)
                    pyperclip.copy("FluxUI is a cool tool!")

                with open("C:\\FluxUI\\back\\web\\prompt_input.py", "r", encoding="utf-8") as file:
                    exec(file.read())
        except Exception as e:
            print(Fore.RED + f"Error in handle_clipboard: {e}" + Style.RESET_ALL)
        time.sleep(1)

def handle_prompt():
    while True:
        try:
            clipboard_text = pyperclip.paste()
            if clipboard_text.startswith("#flux:"):
                stripped_text = clipboard_text[7:]
                with open("C:\\FluxUI\\ai_prompt.txt", "w", encoding="utf-8") as f:
                    f.write(stripped_text)
                    pyperclip.copy("FluxUI is a cool tool!")
                print("Prompt Updated.")
        except Exception as e:
            print(Fore.RED + f"Error in handle_prompt: {e}" + Style.RESET_ALL)
        time.sleep(1)

def handle_model():
    while True:
        try:
            clipboard_text = pyperclip.paste()
            if clipboard_text.startswith(":flux:"):
                stripped_text = clipboard_text[7:]
                with open("C:\\FluxUI\\back\\model.txt", "w", encoding="utf-8") as f:
                    f.write(stripped_text)
                    pyperclip.copy("FluxUI is a cool tool!")
                with open("C:\\FluxUI\\back\\model.py", "r", encoding="utf-8") as file:
                    exec(file.read())

        except Exception as e:
            print(Fore.RED + f"Error in handle_model: {e}" + Style.RESET_ALL)
        time.sleep(1)

def handle_command():
    while True:
        try:
            clipboard_text = pyperclip.paste()
            if clipboard_text.startswith("~flux:"):
                stripped_text = clipboard_text[7:]
                with open("C:\\FluxUI\\back\\web\\command.txt", "w", encoding="utf-8") as f:
                    f.write(stripped_text)
                    pyperclip.copy("FluxUI is a cool tool!")
                subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/web/command.py'])
                #with open("C:\\FluxUI\\back\\web\\command.py", "r", encoding="utf-8") as file:
                    #exec(file.read())

        except Exception as e:
            print(Fore.RED + f"Error in handle_model: {e}" + Style.RESET_ALL)
        time.sleep(1)

def handle_enter():
    """Triggers the runner.py script when Enter is pressed."""
    keyboard.add_hotkey('alt + X', lambda: os.system("python C:/FluxUI/back/request_input.py"))

if __name__ == "__main__":
    print("Ready and waiting for input...")
    print(Fore.YELLOW + Back.BLACK + Style.DIM + "Press Alt + X to input text via the terminal." + Style.RESET_ALL)
    
    # Starting threads
    threading.Thread(target=handle_clipboard, daemon=True).start()
    threading.Thread(target=handle_prompt, daemon=True).start()
    threading.Thread(target=handle_model, daemon=True).start()
    threading.Thread(target=handle_command, daemon=True).start()

    # Running handle_enter to keep the script running
    handle_enter()
    
    # Keeping the main thread alive
    while True:
        time.sleep(2)

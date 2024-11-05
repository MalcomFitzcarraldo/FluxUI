import pyperclip
import os
import time
import keyboard
import subprocess
from colorama import Fore, Style, Back

print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "" + Style.RESET_ALL)

def handle_clipboard():
    while True:
        clipboard_text = pyperclip.paste()
        if clipboard_text.startswith("@flux:"):
            stripped_text = clipboard_text[7:] 
            with open("C:\\FluxUI\\temp\\input.txt", "w", encoding="utf-8") as f:
                f.write(stripped_text)
                pyperclip.copy("FluxUI is a cool tool!")

            with open("C:\\FluxUI\\back\\prompt_input.py", "r") as file:
                exec(file.read())
        
        time.sleep(1)
def handle_enter():
  """Triggers the runner.py script when Enter is pressed."""
  keyboard.add_hotkey('alt + X', lambda: os.system("C:/FluxUI/back/request_input.py"))

if __name__ == "__main__":
  print("Ready and waiting for input...")
  print(Fore.YELLOW + Back.BLACK + Style.DIM + "Press Alt + X to input text via the terminal." + Style.RESET_ALL)
  handle_enter()
  handle_clipboard()
  

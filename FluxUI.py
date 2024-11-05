from colorama import Fore, Style, Back
import subprocess
import os

print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
subprocess.run([r'C:/FluxUI/back/clear_temp.bat'])
os.system('cls')
#subprocess.run(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/request_input.py'])
subprocess.run(["python", "C:/FluxUI/back/web/watcher.py"])

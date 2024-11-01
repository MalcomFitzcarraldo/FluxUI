from colorama import Fore, Style
import subprocess
print(Fore.GREEN + "FluxUI" + Style.RESET_ALL)
subprocess.run([r'C:/FluxUI/back/clear_temp.bat'])
subprocess.run(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/request_input.py'])




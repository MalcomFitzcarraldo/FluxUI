from colorama import Fore, Style, Back
import subprocess
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Fore.GREEN + "Response Complete." + Style.RESET_ALL)
print(Fore.WHITE + "Press ENTER for new query." + Style.RESET_ALL)
input()
subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/FluxUI.py'])

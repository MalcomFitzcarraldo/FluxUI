from colorama import Fore, Style, Back
import subprocess
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Fore.GREEN + "Response Complete." + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Press ENTER to CLEAR" + Style.RESET_ALL)
print(Fore.YELLOW + Back.RED + Style.BRIGHT + "Press ENTER to CLEAR response and start a new query." + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Press ENTER to CLEAR" + Style.RESET_ALL)
input()
subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/FluxUI.py'])

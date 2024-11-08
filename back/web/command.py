import subprocess
from colorama import Fore, Style, Back

print(Fore.BLACK + Style.DIM + Back.CYAN + "FluxUI Commander" + Style.RESET_ALL)
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "" + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "You can close this window upon success" + Style.RESET_ALL)

# File path to the command
command_file = r"C:\FluxUI\back\web\command.txt"

# Read the command from the file
with open(command_file, "r", encoding="utf-8") as f:
    command = f.read().strip()

# Prepare the command to be run in cmd
cmd_command = f"cmd /c {command}"

# Run the command in cmd
try:
    # Using subprocess.run to execute the command in the shell
    result = subprocess.run(cmd_command, shell=True, text=True)
    result.check_returncode()  # Check if the command was successful

except subprocess.CalledProcessError as e:
    print(Fore.RED + f"Error running command: {e}" + Style.RESET_ALL)

print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Press ENTER to Close window" + Style.RESET_ALL)

input()

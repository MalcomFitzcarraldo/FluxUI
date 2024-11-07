import subprocess
from colorama import Fore, Style, Back

print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "" + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Working. This may take a while..." + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Watch the Network Performance tab on task manager to know when a model has downloaded." + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "You can close this window once the network speed drops or when the model is listed in all models" + Style.RESET_ALL)
# File path to the PowerShell command
command_file = r"C:\FluxUI\back\web\command.txt"

# Read the command from the file
with open(command_file, "r", encoding="utf-8") as f:
    command = f.read().strip()

# Run the PowerShell command
try:
    process = subprocess.Popen(
        ["powershell.exe", "-Command", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )

    # Print the output in real time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    
    # Get the return code and print the error if any
    rc = process.poll()
    if rc != 0:
        error_output = process.stderr.read()
        print(Fore.RED + f"Error running PowerShell command: {error_output}" + Style.RESET_ALL)

except Exception as e:
    print(Fore.RED + f"Exception: {e}" + Style.RESET_ALL)

print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Press ENTER to Close window" + Style.RESET_ALL)

input()

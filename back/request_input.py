from colorama import Fore, Style, Back
import subprocess

print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Style.BRIGHT)
def save_text():
  """
  Asks the user for text input and saves it to a file.
  """
  print(Fore.WHITE + "Send a message:" + Style.RESET_ALL)
  user_input = input()
  try:
    with open("C:\\FluxUI\\temp\\input.txt", "w") as file:
      file.write(user_input)
    print(Fore.GREEN + "Text sent! Launching response..." + Style.RESET_ALL)
    subprocess.run(["python", "C:/FluxUI/back/prompt_input.py"])
  except Exception as e:
    print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
  save_text() 


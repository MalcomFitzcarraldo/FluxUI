from colorama import Fore, Style, Back
import subprocess
import time
file1_path = r'C:\FluxUI\ai_prompt.txt'
file2_path = r'C:\FluxUI\temp\input.txt'
output_file_path = r'C:\FluxUI\temp\prompt_input.txt'
with open(file1_path, 'r') as file1:
    file1_content = file1.read()
with open(file2_path, 'r') as file2:
    file2_content = file2.read()
with open(output_file_path, 'w') as output_file:
    output_file.write(file1_content + "\n" + file2_content)
print(Fore.WHITE + "Ollama Activated. - Opening in Browser.")
print(Style.RESET_ALL)

# Start the scheduler
subprocess.run([r'C:/FluxUI/back/signal_reset.bat'])
time.sleep(1)
subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/update_timer.py'])
time.sleep(1)

subprocess.run(["python", "C:/FluxUI/back/API_ollama.py"])

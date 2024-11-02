from colorama import Fore, Style
import subprocess
import time
from ollama import Client
print(Fore.GREEN + "Signal Clear! " + Style.RESET_ALL)
print(Fore.GREEN + "" + Style.RESET_ALL)
print(Style.DIM)
print(Fore.WHITE)

file_path = r'C:\FluxUI\temp\prompt_input.txt'
output_file_path = r'C:\FluxUI\temp\output.txt'
signal_file_path = r'C:\FluxUI\temp\done.txt'

# Read the input file
with open(file_path, 'r') as file:
    file_content = file.read().strip()

client = Client(host='http://localhost:11434')
response_stream = client.chat(model='gemma2:9b', messages=[{
    'role': 'user',
    'content': f'{file_content}',
}], stream=True)

# Open the output
with open(output_file_path, 'w') as output_file:
    # Start the scheduler
    subprocess.run([r'C:/FluxUI/back/signal_reset.bat'])
    subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/update_timer.py'])
    
    for chunk in response_stream:
        # Print the chunk to the console
        # print(chunk['message']['content'], end='')
        # Write the chunk to the output file
        output_file.write(chunk['message']['content'])
        # Ensure content is written to the file immediately
        output_file.flush()

# Create a signal file to indicate the script has finished 
with open(signal_file_path, 'w') as signal_file: signal_file.write('done')
time.sleep(2)
subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/getrich_final.py'])
subprocess.Popen(['cmd', '/c', 'start', 'python', 'C:/FluxUI/back/finished.py'])
print(Fore.GREEN + "\nResponse cached to temp/output.txt")
time.sleep(1)


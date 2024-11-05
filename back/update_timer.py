import time
import subprocess
import os

signal_file_path = r'C:\FluxUI\temp\done.txt'

def run_merger():
    while True:
        if os.path.exists(signal_file_path):
            print("Main script finished. Exiting scheduler.")
            break
        subprocess.run(['python', 'C:/FluxUI/back/getrich.py'])
        time.sleep(1.5)

if __name__ == "__main__":
    run_merger()


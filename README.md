# FluxUI: Use ollama in your web browser without a web server.
### FluxUI is a Windows application designed to seamlessly bridge the gap between your text prompts and powerful AI models, delivering responses directly to your web browser without relying on external web servers.

![fluxui](https://github.com/user-attachments/assets/d8d789b6-1780-41a9-ba0a-2490488c9140)

## Key Features:

* Direct Model Integration: Submit text to various AI models (installed on Ollama) directly from your web browser.
* Real-time Streaming: Experience immediate feedback as the AI generates its response, displayed in real time within your browser window.
* Rich Text Output: Enjoy clean and well-formatted text responses with proper paragraph breaks and line spacing for easy readability.
* Code Block Formatting: FluxUI automatically recognizes and formats code snippets into dedicated code blocks, enhancing clarity and readability.
* **Zero Web Server Dependency**: Eliminate the need to set up or maintain a web server – FluxUI handles all the communication directly between your system and the AI models.
## Benefits:

* Simplified Workflow: Streamline your interaction with AI models by eliminating the complexities of web server setup and management.
* Enhanced User Experience: Enjoy a responsive and interactive experience with real-time feedback and clear, formatted output.
* Increased Efficiency: Focus on your tasks without the overhead of managing separate web interfaces or servers.


![fluxmini](https://github.com/user-attachments/assets/3a4d2b2e-051c-47d2-9b4e-8dff9e526c1e)



## Installation

### Ollama Setup:
1. Download and install Ollama (WINDOWS). - https://ollama.com/download
   
2. Install Python (with PIP) - https://www.python.org/downloads/
   - Once installed, confirm that you have installed by typing `pip --version` in the Command Prompt.

3. Run the commands below to install all the necessary Python modules:
```
pip install BeautifulSoup4
```
```
pip install colorama
```
```
pip install markdown
```
```
pip install ollama
```

4. Download and extract FluxUI, then create the FluxUI directory.

  * right-click in the **extracted folder** containing the 6 files and click "Open in Terminal".
   
  * Run the following commands to create the directory and install FluxUI.

* Create directory - C:\FluxUI.
   ```cmd
   mkdir "C:\FluxUI"
   ```
* Copy the FluxUI files to C:\FluxUI.
   ```cmd
   xcopy . "C:\FluxUI\" /E /H /C /I
   ```
   
> [!IMPORTANT]
> Without modification, this must to be installed/run from "C:\FluxUI".

 
5. Create desktop shortcut (optional)
  Run the following code in cmd **(as admin)** to create a desktop shortcut: 
- Windows (Standard)
```cmd
cmd /k mklink "C:\Users\%USERNAME%\Desktop\Snap2It.lnk" "C:\FluxUI\FluxUI.py"
```
- Windows (OneDrive)
```cmd
cmd /k mklink "C:\Users\%USERNAME%\OneDrive\Desktop\Snap2It.lnk" "C:\FluxUI\FluxUI.py"
```
or Navigate to **C:\FluxUI** and open **FluxUI.py**

6. Install a model and you're all set!

## Advanced Setup

### Running Ollama from another PC
Open ``C:\FluxUI\back\API_ollama`` line 18: Replace ``localhost`` with the IP of the PC running Ollama

## Screenshots:

![image](https://github.com/user-attachments/assets/71b49752-39aa-4364-ac59-0028b98bbbbf)

![image](https://github.com/user-attachments/assets/27fd32bd-1875-4009-be2f-11c7e0162fc7)

![image](https://github.com/user-attachments/assets/5c8613d4-ed54-482a-864c-70f7ded8a69e)

![image](https://github.com/user-attachments/assets/8c12a084-59f5-434e-9d7f-af10b636a016)



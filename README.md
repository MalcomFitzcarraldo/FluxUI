# FluxUI: Stream AI Responses Directly to Your Browser
### FluxUI is a Windows application designed to seamlessly bridge the gap between your text prompts and powerful AI models, delivering responses directly to your web browser without relying on external web servers.

## Key Features:

* Direct Model Integration: Submit text to various AI models (installed on Ollama) directly from your desktop.
* Real-time Streaming: Experience immediate feedback as the AI generates its response, displayed in real time within your browser window.
* Rich Text Output: Enjoy clean and well-formatted text responses with proper paragraph breaks and line spacing for easy readability.
* Code Block Formatting: FluxUI automatically recognizes and formats code snippets into dedicated code blocks, enhancing clarity and readability.
* Zero Web Server Dependency: Eliminate the need to set up or maintain a web server – FluxUI handles all the communication directly between your system and the AI models.
## Benefits:

* Simplified Workflow: Streamline your interaction with AI models by eliminating the complexities of web server setup and management.
* Enhanced User Experience: Enjoy a responsive and interactive experience with real-time feedback and clear, formatted output.
* Increased Efficiency: Focus on your tasks without the overhead of managing separate web interfaces or servers.

![fluxui](https://github.com/user-attachments/assets/4218babb-688e-4804-b0d1-a5ec70f5e303)


## Installation


1. Download and extract FluxUI, and Create the FluxUI directory.
> [!IMPORTANT]
> Without modification, this must to be installed/run from "C:\FluxUI".
3. right-click in the **extracted folder** containing the 6 files and click "Open in Terminal".
4. Run the following commands to create the directory and install FluxUI.
* Create directory - C:\FluxUI.
   ```cmd
   mkdir "C:\FluxUI"
   ```
* Copy the FluxUI files to C:\FluxUI.
   ```cmd
   xcopy . "C:\FluxUI\" /E /H /C /I
   ```
   
4. Install Python (with PIP) - https://www.python.org/downloads/
   - Once installed, confirm that you have installed by typing `pip --version` in the Command Prompt.

5. Run the commands below to install all the necessary Python modules:
```
pip install BeautifulSoup4
```
```
pip install colorama
```
```
pip install markdown
```


### Ollama Setup:
6. Download and install Ollama (WINDOWS). - https://ollama.com/download
7. Install ollama for Python.
```
pip install ollama
```
8. Install a model on Ollama. - https://ollama.com/library
   *The codes below will install Google Gemma 2b (lightweight)
```
ollama run gemma2:2b
```
9. Open C:\FluxUI\back\API_ollama.py in notepad
10. **Line 19** contains "model='`gemma2:9b`'" **Replace "gemma2:9b"* with the model you have loaded to ollama

* You can edit C:\FluxUI\ai_prompt.txt to change the text in front of the input text
   - Default prompt is: Find the question in the text below and give a simple answer:
   - Default ollama server address: localhost:11434
 
11. Run `C:\FluxUI\FluxUI.py` and the FluxUI will start

![fluxmini](https://github.com/user-attachments/assets/3a4d2b2e-051c-47d2-9b4e-8dff9e526c1e)

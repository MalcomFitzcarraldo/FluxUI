# ✨FluxUI: Unleash the Power of AI in Your Browser✨
### Tired of clunky web interfaces and server dependencies when working with AI? FluxUI bridges the gap between powerful AI models and your web browser seamlessly. 🤯 All you need is Ollama, Python, and FluxUI to experience AI like never before! 💻

## Here's what makes FluxUI special:

* Model Freedom: Use any AI model you desire – the choice is yours! 🚀
* Effortless Installation: Get up and running in minutes with our simple installation process. 💨
* Visually Stunning Output: Experience AI responses with optimized prompts that utilize a variety of fonts, text sizes, emojis, and colors for ultimate readability. 🤩

 ## FluxUI features:

* Code Block Formatting: Code snippets are formatted into dedicated blocks, enhancing clarity and readability. 💻
* Real-time Streaming: Witness the magic unfold as AI generates responses instantly in your browser window. 👀
* Zero Web Server Dependency: Say goodbye to server headaches! FluxUI handles it all. 🔒
* Join the FluxUI revolution and take control of your AI experience today! 🚀
  
![fluxui](https://github.com/user-attachments/assets/d8d789b6-1780-41a9-ba0a-2490488c9140)

![fluxmini](https://github.com/user-attachments/assets/3a4d2b2e-051c-47d2-9b4e-8dff9e526c1e)



## Installation
Install Video
https://youtu.be/7WgEFHB1bvY
### Ollama Setup:
1. Download and install Ollama (WINDOWS). - https://ollama.com/download
   
2. Install Python (with PIP) - Microsoft Store
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
```
pip install pyperclip
```
```
pip install keyboard
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

Code Formatting:
![image](https://github.com/user-attachments/assets/7df50256-1c92-48f5-876d-7834aeeff1bf)

![image](https://github.com/user-attachments/assets/71b49752-39aa-4364-ac59-0028b98bbbbf)

![image](https://github.com/user-attachments/assets/27fd32bd-1875-4009-be2f-11c7e0162fc7)

![image](https://github.com/user-attachments/assets/5c8613d4-ed54-482a-864c-70f7ded8a69e)

![image](https://github.com/user-attachments/assets/8c12a084-59f5-434e-9d7f-af10b636a016)

When I modify the prompt to show HTML
![image](https://github.com/user-attachments/assets/07ed80bd-83ee-413d-abaf-cdc93cb1dc63)



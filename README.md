# ✨FluxUI: Unleash the Power of Ollama in Your Browser✨
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
 * <sup>Confirm that you have pip by typing `pip --version` in the Command Prompt. </sup>

3. Run the command below to install all the necessary Python modules:
```
pip install BeautifulSoup4 colorama markdown ollama pyperclip keyboard
```


4. Download and extract the FluxUI files.
> [!IMPORTANT]
> Without modification, this must to be installed/run from "C:\FluxUI".

5. right-click in the **extracted folder** containing the 6 FluxUI files and click "Open in Terminal".
   
* Create directory - C:\FluxUI.
```cmd
mkdir "C:\FluxUI"
```
* Copy the FluxUI files to C:\FluxUI.
```cmd
xcopy . "C:\FluxUI\" /E /H /C /I
```
* Open FluxUI.py
```cmd
start C:\FluxUI\FluxUI.py
```

6. Go to Manage Models and install the model of your choice.

7. Go to Change Model and update it to the installed model.

### You're all set! 🚀
Tips:
* Create a desktop shortcut for FluxUI.py
* Use the back button in your browser to edit/review submitted queries



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



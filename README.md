# ✨FluxUI: Unleash the Power of Ollama in Your Browser✨
### Tired of clunky web interfaces and server dependencies when working with AI? FluxUI bridges the gap between powerful AI models and your web browser seamlessly. 🤯 All you need is Ollama, Python, and FluxUI to experience AI like never before! 💻

## Here's what makes FluxUI special:

* Model Freedom: Use any AI model you desire – the choice is yours! 🚀
* Total Privacy: Once a response is generated the cache is cleared. 🔒
* Effortless Installation: Get up and running fast with the simple installation process. 💨
* Visually Stunning Output: Experience AI responses with optimized prompts that utilize a variety of fonts, text sizes, emojis, and colors for ultimate readability. 🤩
* Code Block Formatting: Code snippets are formatted into dedicated blocks, enhancing clarity and readability. 💻
* Real-time Streaming: Witness the magic unfold as AI generates responses instantly in your browser window. 👀
* Zero Web Server Dependency: Say goodbye to server headaches! FluxUI handles it all. 🧮

* Join the FluxUI revolution and take control of your AI experience today! 🚀
  
![fluxui](https://github.com/user-attachments/assets/d8d789b6-1780-41a9-ba0a-2490488c9140)


## Installation
Install Video
https://youtu.be/7WgEFHB1bvY
### Ollama Setup:
1. Download and install Ollama. - https://ollama.com/download
   
2. Install Python (with PIP) - https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare
 * <sup>Confirm that you have pip by typing `pip --version` in the Command Prompt. </sup>

3. Run the command below to install all the necessary Python modules:
```
pip install BeautifulSoup4 colorama markdown ollama pyperclip keyboard
```

4. Download and extract the files from the latest release of FluxUI.

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

7. Go to Set Model and update it to the **installed** model.

### You're all set! 🚀
Tips:
* Create a desktop shortcut for FluxUI.py
* Use the back button in your browser to edit/review submitted queries
* Edit or modify the prompt for a more custom experience.



## Advanced Setup

### Running Ollama from another PC
Open ``C:\FluxUI\back\API_ollama`` line 18: Replace ``localhost`` with the IP of the PC running Ollama

## Screenshots:

### Type or paste text, then hit enter and watch the reply.
![image](https://github.com/user-attachments/assets/cf3d5df6-0481-435a-89c4-4a0d655b2422)
### The results stream live, the result is complete once you see a green border.
![image](https://github.com/user-attachments/assets/c08c07c8-14c8-4a70-8c2b-6f8c09b73d03)
### Easily Add/Remove models
![image](https://github.com/user-attachments/assets/5e6c25b7-f5d3-4d9e-b9dc-1893d1b75e46)
### Switch between installed models quickly
![image](https://github.com/user-attachments/assets/ad6f2ca8-1c07-4892-a287-5cbca71b692f)
### Edit the global prompt
![image](https://github.com/user-attachments/assets/87e4dd16-fcff-498f-88ff-bc600145442b)



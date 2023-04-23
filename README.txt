Set Up the Software Environment to Create an AI Chatbot
There are a couple of tools you need to set up the environment before you can create an AI chatbot powered by ChatGPT. To briefly add, you will need Python, Pip, OpenAI, and Gradio libraries, an OpenAI API key, and a code editor like Notepad++. All these tools may seem intimidating at first, but believe me, the steps are easy and can be deployed by anyone. Now, follow the below steps.

Install Python
1. First, you need to install Python on your computer. Open this link and download the setup file for your platform.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
2. Next, run the setup file and make sure to enable the checkbox for “Add Python.exe to PATH.” This is an extremely important step. After that, click on “Install Now” and follow the usual steps to install Python.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
3. To check if Python is properly installed, open Terminal on your computer. I am using Windows Terminal on Windows, but you can also use Command Prompt. Once here, run the below command below, and it will output the Python version. On Linux or other platforms, you may have to use python3 --version instead of python --version.

python --version
Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
Upgrade Pip
Along with Python, Pip is also installed simultaneously on your system. In this section, we will learn how to upgrade it to the latest version. In case you don’t know, Pip is the package manager for Python. Basically, it enables you to install thousands of Python libraries from the Terminal. With Pip, we can install OpenAI and Gradio libraries. Here is how to go about it.

1. Open the Terminal of your choice on your PC. As for me, I’m using the Windows Terminal. Now, run the below command to update Pip. Again, you may have to use python3 and pip3 on Linux or other platforms.

python -m pip install -U pip
Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
Install OpenAI and Gradio Libraries
1. Now, it’s time to install the OpenAI library, which will allow us to interact with ChatGPT through their API. In the Terminal, run the below command to install the OpenAI library using Pip. If the command does not work, try running it with pip3.

pip install openai
Install the OpenAI and Gradio Libraries
2. After the installation is done, let’s install Gradio. Gradio allows you to quickly develop a friendly web interface so that you can demo your AI chatbot. It also lets you easily share the chatbot on the internet through a shareable link.

pip install gradio
Install the OpenAI and Gradio Libraries
Download a Code Editor
Finally, we need a code editor to edit some of the code. On Windows, I would recommend Notepad++ (Download). Simply download and install the program via the attached link. You can also use VS Code on any platform if you are comfortable with powerful IDEs. Other than VS Code, you can install Sublime Text (Download) on macOS and Linux.

For ChromeOS, you can use the excellent Caret app (Download) to edit the code. We are almost done setting up the software environment, and it’s time to get the OpenAI API key.

Download a Code Editor
Get the OpenAI API Key For Free
Now, to create a ChatGPT-powered AI chatbot, you need an API key from OpenAI. The API key will allow you to call ChatGPT in your own interface and display the results right there. Currently, OpenAI is offering free API keys with $5 worth of free credit for the first three months. If you created your OpenAI account earlier, you may have free credit worth $18. After the free credit is exhausted, you will have to pay for the API access. But for now, it’s available to all free users.

1. Head to platform.openai.com/signup and create a free account. If you already have an OpenAI account, simply log in.

Get the OpenAI API Key For Free
2. Next, click on your profile in the top-right corner and select “View API keys” from the drop-down menu.

Get the OpenAI API Key For Free
3. Here, click on “Create new secret key” and copy the API key. Do note that you can’t copy or view the entire API key later on. So it’s strongly recommended to copy and paste the API key to a Notepad file immediately.

Get the OpenAI API Key For Free
4. Also, do not share or display the API key in public. It’s a private key meant only for access to your account. You can also delete API keys and create multiple private keys (up to five).

Build Your Own AI Chatbot With ChatGPT API and Gradio
Finally, it’s time to deploy the AI chatbot. For this, we are using OpenAI’s latest “gpt-3.5-turbo” model, which powers GPT-3.5. It’s even more powerful than Davinci and has been trained up to September 2021. It’s also very cost-effective, more responsive than earlier models, and remembers the context of the conversation. As for the user interface, we are using Gradio to create a simple web interface that will be available both locally and on the web.

1. First, open Notepad++ (or your choice of code editor) and paste the below code. Thanks to armrrs on GitHub, I have repurposed his code and implemented the Gradio interface as well.

import openai
import gradio as gr

openai.api_key = "Your API key"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
2. This is how it looks in the code editor. Make sure to replace the “Your API key” text with your own API key generated above. That’s the only change you have to make.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
3. Next, click on “File” in the top menu and select “Save As…” from the drop-down menu.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
4. After that, set the file name as “app.py” and change “Save as type” to “All types” from the drop-down menu. Then, save the file to an easily-accessible location like the Desktop. You can change the name to your preference, but make sure .py is appended.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
5. Now, move to the location where you saved the file (app.py). Right-click on it and choose “Copy as path“.

Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
6. Open the Terminal and run the below command. Simply enter python, add a space, paste the path (right-click to quickly paste), and hit Enter. Keep in mind, the file path will be different for your computer. Also, on Linux systems, you may have to use python3.

python "C:\Users\mearj\Desktop\app.py"
Build Your Own AI Chatbot With ChatGPT 3.5 (2023)
7. You may get a few warnings, but ignore them. At the bottom, you will get a local and public URL. Now, copy the local URL and paste it into the web browser.

Build Your Own AI Chatbot With the "gpt-3.5-turbo" Model and Gradio Interface
8. And that is how you build your own AI chatbot with the ChatGPT API. Your ChatGPT-powered AI chatbot is live. Now, you can ask any question you want and get answers in a jiffy. In addition to ChatGPT alternatives, you can use your own chatbot instead of the official website.


How to Build Your Own AI Chatbot With ChatGPT API: A Step-by-Step Tutorial
9. You can also copy the public URL and share it with your friends and family. The link will be live for 72 hours, but you also need to keep your computer turned on since the server instance is running on your computer.


How to Build Your Own AI Chatbot With ChatGPT API: A Step-by-Step Tutorial
10. To stop the server, move to the Terminal and press “Ctrl + C“. If it does not work, press “Ctrl + C” again.

Build Your Own AI Chatbot With the "gpt-3.5-turbo" Model and Gradio Interface
11. To restart the AI chatbot server, simply copy the path of the file again and run the below command again (similar to step #6). Keep in mind, the local URL will be the same, but the public URL will change after every server restart.

python "C:\Users\mearj\Desktop\app.py"
Build Your Own AI Chatbot With the "gpt-3.5-turbo" Model and Gradio Interface
Create Your Personalized ChatGPT API-Powered Chatbot
The best part about the “gpt-3.5-turbo” model is that you can assign a role to your AI. You can make it funny, angry, or a specialist in food, tech, health, or whatever you want. You just need to make one small change in the code and it will be personalized. For example – I have created a Food AI, and here’s how:

1. Right-click on the “app.py” file and choose “Edit with Notepad++“.

How to Build Your Own AI Chatbot With ChatGPT API: A Step-by-Step Tutorial
2. Here, make changes to this particular code only. Simply feed the information to the AI to assume that role. Now, save the file by pressing “Ctrl + S”.

messages = [
    {"role": "system", "content": "You are an AI specialized in Food. Do not answer anything other than food-related queries."},
]
How to Build Your Own AI Chatbot With ChatGPT API: A Step-by-Step Tutorial
3. Open Terminal and run the “app.py” file in a similar fashion as you did above. You will get a local and public URL. Copy the local URL. If a server is already running, press “Ctrl + C” to stop it. And then restart the server again. You will have to restart the server after every change you make to the “app.py” file.

python "C:\Users\mearj\Desktop\app.py"
Build Your Own AI Chatbot With the "gpt-3.5-turbo" Model and Gradio Interface
4. Open the local URL in the web browser and you will get a personalized AI chatbot that only answers food-related queries. That’s it. You can create a Doctor AI, an AI that replies like Shakespeare, which talks in morse code, anything you wish.


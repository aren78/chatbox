import openai
import gradio as gr


openai.api_key="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"
messages = [
    {"role":"system","content":"You are a helpful and kind AI Assistant."},]

def chatbox(input):
    if input:
        messages.append({"role":"user","content":input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role":"assistant","content":reply})
        return reply

ins=gr.inputs.Textbox(lines=7,label="chat with AI")
ous=gr.outputs.Textbox(label="reply")


gr.Interface(fn=chatbox,inputs=ins,outputs=ous,title="chatbox",
             description="Ask you'r favorite word's",
             theme="compact").launch(share=True)

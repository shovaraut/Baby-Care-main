# app.py

import gradio as gr
from answer import openai_create

# Placeholder prompt
prompt = "Ask anything about maternal health, pregnancy, childbirth, or childcare..."

# Chat function with memory
def maternal_care_bot(user_input, chat_history):
    chat_history = chat_history or []
    previous_dialogue = list(sum(chat_history, ()))
    previous_dialogue.append(user_input)
    full_prompt = ' '.join(previous_dialogue)
    
    ai_response = openai_create(full_prompt)
    chat_history.append((user_input, ai_response))
    return chat_history, chat_history

# Interface
block = gr.Blocks()

with block:
    gr.Markdown("<h1><center>🤱 Bridging Gaps: Maternal Childcare AI Support</center></h1>")
    gr.Markdown(
        """
        <p><center>
        Welcome to your AI-powered maternal health assistant. This chatbot helps you with expert-backed answers 
        on pregnancy, childbirth, newborn care, breastfeeding, postpartum recovery, mental wellness, and parenting.
        </center></p>
        """
    )
    
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt, label="Your Question")
    state = gr.State()
    send_button = gr.Button("Send")

    send_button.click(
        fn=maternal_care_bot,
        inputs=[message, state],
        outputs=[chatbot, state]
    )

block.launch(share=True, debug=True)

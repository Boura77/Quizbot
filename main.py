import openai
import streamlit as st
import time

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = "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"
MODEL = "gpt-3.5-turbo"
openai.api_key = OPENAI_API_KEY # for open ai
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY # for lang chain


st.title("AGI Quiz Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "You are an expert in making and conducting Single Correct MCQ Questions. You are going to conduct a test of total 10 question, so the correct answer for each question will only be revealed after all the 10 questions have been asked. Ask a question, then once user answers, irrespective if answer is correct or wrong, dont let the user know, just ask next question. Stick to the topic/subject specified by the user. Make the questions progressively tougher. After you have asked all 10 questions, tell the user how many of the 10 questions did they get right."})
    st.session_state.messages.append({"role": "assistant", "content": "Which Topic/Subject will you like to be quizzed on?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Your answer?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=st.session_state.messages,
        temperature = 0.4,
        max_tokens = 600,
        n = 1
    )

    res = response.choices[0].message['content']
    print(res)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        assistant_response = res

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

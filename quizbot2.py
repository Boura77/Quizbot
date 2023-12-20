import openai
import streamlit as st
import time
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = "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"
MODEL = "gpt-3.5-turbo"
openai.api_key = OPENAI_API_KEY # for open ai
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 


st.title("AGI Quiz Application")
prompt_template_name = PromptTemplate(
        input_variables=['topic_name'],
        template="I want to prepare a MCQ quiz on {topic_name}. You are going to conduct a test of total 5 questions on {topic_name}. Ask a question, then once user answers, irrespective if answer is correct or wrong, dont let the user know, just ask next question. Stick to the topic/subject specified by the user. Make the questions progressively tougher. Add one point for each question answered correctly by the user and display total score in the end and reveal the correct answers"
    )

topic = st.sidebar.selectbox("Pick a topic", ("Football", "Cricket", "Pwc", "F1 Racing"))
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    #st.session_state.messages.append({"role": "assistant", "content": "You are an expert in making and conducting Single Correct 4 MCQ Questions. You are going to conduct a test of total 10 questions. Ask a question, then once user answers, irrespective if answer is correct or wrong, dont let the user know, just ask next question. Stick to the topic/subject specified by the user. Make the questions progressively tougher. Add one point for each question answered correctly by the user and display total score in the end"})
    st.session_state.messages.append({"role": "assistant", "content": "Type start to begin :) after selecting topic from sidebar"})

# Display chat messages from history 
for message in st.session_state.messages:
    # if message["role"] != "user":
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Your answer?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    topic_prompt = [{"role": "assistant", "content":prompt_template_name.format(topic_name = topic)}]
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=topic_prompt+st.session_state.messages,
        temperature = 0.4,
        max_tokens = 500,
        n = 1
    )

    assistant_response = response.choices[0].message['content']

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        assistant_response = response.choices[0].message['content']

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

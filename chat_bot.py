import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()
import os

# Initialize the ChatOpenAI model
chat = ChatOpenAI(temperature=0.5)

# Set up Streamlit page configuration
st.set_page_config(page_title="Faizan Chatbot")
st.header("🤖 I am Faizan, the chatbot 💬 Here to assist you. Ask me anything!")

# Initialize session state for message history
if "mymessage" not in st.session_state:
    st.session_state["mymessage"] = [
        SystemMessage(
            content="You are Faizan, a chatbot. Your responsibility is to answer any questions that the human asks."
        )
    ]

if "history" not in st.session_state:
    st.session_state["history"] = []


def chatmodel_response(question):
    # Add the human message to the conversation history
    st.session_state["mymessage"].append(HumanMessage(content=question))

    # Get the AI response
    response = chat(st.session_state["mymessage"])

    # Add the AI response to the conversation history
    st.session_state["mymessage"].append(AIMessage(content=response.content))

    # Update history
    st.session_state["history"].append(
        {"question": question, "answer": response.content}
    )

    return response.content


# Display the conversation history
def display_history():
    if st.session_state["history"]:
        for entry in st.session_state["history"]:
            st.write(f"**You:** {entry['question']}")
            st.write(f"**Faizan:** {entry['answer']}")
            st.write("---")


# User input
input = st.text_input("Input", key="input")

# Submit button
if st.button("Get Answer 🧠🕵️‍♂️"):
    if input:
        response = chatmodel_response(input)
        st.subheader("Here is your response: 🗣️")
        st.write(response)

# Display conversation history
display_history()

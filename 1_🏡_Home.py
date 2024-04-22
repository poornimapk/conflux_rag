import pandas as pd
import streamlit as st
from streamlit_pills import pills

from st_utils import (
    add_sidebar,
)

st.set_page_config(
    page_title="Build a RAG bot, powered by Conflux",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("Build a RAG bot, powered by Conflux: Empowering Productivity, Seamlessly Integrated.")

st.info(
    "Use this page to build your RAG bot over your data! "
    "Once the agent is finished creating, check out the `RAG Config` and "
    "`Generated RAG Agent` pages.\n"
    "To build a new agent, please make sure that 'Create a new agent' is selected.",
    icon="ℹ️",
)

add_sidebar()

# add pills (pills are used to create clickable options on the page)
selected = pills(
    label="Outline your task!",
    options=[
        "I want to analyze this PDF file (data/oracle/March-12(Quarterly)-24.pdf",
        "I want to analyze another PDF file (data/oracle/paul-graham-ideas.pdf)",
    ],
    icons=["📄", "📄"],
    clearable=True,
    index=None
)

# # Choose a file loader if user wants to choose his own PDFs.
# uploaded_file = st.file_uploader(label="Choose a file to analyze",
#                                  type="pdf",
#                                  accept_multiple_files=False,)
#
# if uploaded_file is not None:
#     data_in_bytes = uploaded_file.getvalue()


# Initialize the chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant",
         "content": "What RAG bot do you want to build?"}
    ]


def add_to_message_history(role: str, content: str) -> None:
    message = {"role": role, "content": content}
    st.session_state.messages.append(message)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Your question", )  # Prompt for user input and save to chat history
if prompt is not None:
    if "has_rerun" in st.session_state.keys() and st.session_state.has_rerun:
        st.session_state.has_rerun = False
    else:
        add_to_message_history("user", prompt)
        with st.chat_message("user"):
            st.write(prompt)

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = "Hi, how are you doing?"
                    st.write(response)
                    add_to_message_history("assistant", response)
        else:
            pass

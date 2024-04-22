import streamlit as st


def add_sidebar() -> None:
    with st.sidebar:
        choices = ["Create a new agent"]

        st.radio(
            "Agents",
            choices,
            index=0,
            key="agent_selector",
        )

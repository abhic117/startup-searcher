import streamlit as st
import pandas as pd
import time

from src.database import database_to_dataframe

def stream_data(text):
    for word in text.split():
        for char in list(word):
            yield char
            time.sleep(0.03)
        yield " "

# Set streamlit page config
st.markdown("## " + "Startup Dashboard")
st.set_page_config(layout='wide')

# Configure database and write to screen
df = database_to_dataframe()
df = df.drop(columns=['id'])

# Sidebar that allows dataframe column selection
columns = df.columns.tolist()

with st.sidebar:
    st.markdown("# " + "Columns")
    selection = st.pills(label=None, options=columns, selection_mode="multi", default=columns)

# Display dataframe
with st.container():
    selection = [col for col in columns if col in selection]
    st.dataframe(df[selection], height=250)

# User chat input at bottom of screen
prompt = st.chat_input("Query")

st.markdown("#### " + "Chat Window")

# AI chat window
with st.container(height=250, width=700):
    # Initialise chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Display user inputted prompt and add to message history
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"test: {prompt}"

        with st.chat_message("assistant"):
            st.write_stream(stream_data(response))
        st.session_state.messages.append({"role": "assistant", "content": response})
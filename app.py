import streamlit as st
import pandas as pd
import time
from dotenv import load_dotenv

from src.database import get_startups
from src.rag.retrieve import retrieve
from src.rag.generate import generate_answer

load_dotenv()

def stream_data(text):
    for word in text.split():
        for char in list(word):
            yield char
            time.sleep(0.005)
        yield " "

def find_startup_index(query, dataframe):
    normalized_query = query.casefold()
    matches = [
        (index, str(name))
        for index, name in dataframe["name"].items()
        if pd.notna(name) and str(name).casefold() in normalized_query
    ]
    return max(matches, key=lambda match: len(match[1]))[0] if matches else None

# Set streamlit page config
st.markdown("## " + "Startup Dashboard")
st.set_page_config(layout='wide')

# Configure database and write to screens
startups = get_startups()

df = pd.DataFrame(startups)

# Sidebar that allows dataframe column selection
columns = df.columns.tolist()

with st.sidebar:
    st.markdown("# " + "Columns")
    selected_columns = st.pills(label=None, options=columns, selection_mode="multi", default=columns)

# Display dataframe
with st.container():
    selected_columns = [col for col in columns if col in selected_columns]
    table_event = st.dataframe(
        df[selected_columns],
        height=250,
        on_select="rerun",
        selection_mode="single-row",
        key="startup_table",
    )

    selected_rows = table_event.selection.rows
    if selected_rows:
        st.session_state.selected_startup_index = selected_rows[0]

query = st.chat_input("Query")

if query:
    matched_startup_index = find_startup_index(query, df)
    if matched_startup_index is not None:
        st.session_state.selected_startup_index = matched_startup_index

selected_startup_index = st.session_state.get("selected_startup_index")
selected_startup = (
    df.iloc[selected_startup_index]
    if selected_startup_index is not None and selected_startup_index < len(df)
    else None
)

# AI chat window and selected startup details
chat_column, details_column = st.columns([2, 1], gap="medium")

with chat_column:
    st.markdown("#### " + "Chat Window")
    with st.container(height=250, width="stretch"):
    # Initialise chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Display user inputted prompt and add to message history
        if query:
            st.session_state.messages.append({"role": "user", "content": query})

            with st.chat_message("user"):
                st.markdown(query)

                with st.spinner("Retrieving information..."):
                    context = retrieve(query)

            with st.spinner("Generating response..."):
                response = f"{generate_answer(query, context)}"
                st.session_state.messages.append({"role": "assistant", "content": response})

                with st.chat_message("assistant"):
                    st.write_stream(stream_data(response))

            st.rerun()

with details_column:
    st.markdown("#### " + "Detail View")
    with st.container(height=250, border=True, key="selected-startup-details"):
        if selected_startup is not None:
            st.markdown(f"### {selected_startup['name'] or 'Startup details'}")

            details = {
                "Overview": selected_startup["overview"],
                "Location": selected_startup["location"],
                "Industry": selected_startup["industry"],
                "Stage": selected_startup["stage"],
                "Team": selected_startup["team"],
                "Funding": selected_startup["funding"],
                "Description": selected_startup["description"],
            }
            for label, value in details.items():
                st.markdown(f"**{label}:** {value or 'Not available'}")

            if selected_startup["url"]:
                st.markdown(f"**URL:** [{selected_startup['url']}]({selected_startup['url']})")
            else:
                st.markdown("**URL:** Not available")
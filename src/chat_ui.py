import streamlit as st
from react_agent import run_agent

# Streamlit UI
st.set_page_config(page_title="ChatBMW", page_icon="🤖", layout="centered")

st.title("🤖 ChatBMW - ReAct Agent")
st.caption("Ask about sushi 🍣 or parking 🅿️ near Marienplatz")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
if prompt := st.chat_input("Type your question here..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(prompt)
            st.markdown(response)

    # Save assistant message
    st.session_state["messages"].append({"role": "assistant", "content": response})

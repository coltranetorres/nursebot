import streamlit as st

st.title("Sample Nurse Bot")
st.info('This is a side-by-side chat app.')

st.sidebar.write(st.session_state)

if 'conversations' not in st.session_state:
    st.session_state["conversations"] = []
    
def save_message():
    st.session_state["conversations"].append(
        ("user", st.session_state["chat-message"])
    )

col1, col2 = st.columns(2)

# Chat messages
with col1:
    for sender, message in st.session_state["conversations"]:
        with st.chat_message(sender):
            st.write(message)

# Chat input at the bottom of the page 
st.chat_input(
    placeholder="Type a message",
    key="chat-message",
    on_submit=save_message,
)

# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="llama-2-7b-chat.Q4_K_M.gguf")

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
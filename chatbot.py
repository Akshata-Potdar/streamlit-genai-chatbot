from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the env variable
load_dotenv()
#streamlit page setup
st.set_page_config(
    page_title="🗨 Chatbot",
    page_icon="📥",
    layout="centered", #"wide"
)
st.title("🗨 Generative AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#user_prompt=st.chat_input("Ask a question")

#show chat history:
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]): # with:context manager Everything belongs to that chat bubble.
        st.markdown(message["content"])
#llm initiate
llm=ChatGroq(
    model="llama-3.3-70b-versatile", # we can use different model from groq
    temperature=0.0, #controls randomness
)

#input box:
user_prompt=st.chat_input("Ask a question...")

if user_prompt: #runs only if user entered something
    st.chat_message("user").markdown(user_prompt) #display user message instantaly
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

#invoke:send request to model
    response=llm.invoke(
        input=[{"role":"user","content":"You are a helpful assistant"},*st.session_state.chat_history],
    ) # *:unpacks list items
    assistant_response=response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
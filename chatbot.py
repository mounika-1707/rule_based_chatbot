import streamlit as st
import re

# Title
st.set_page_config(page_title="Rule-Based Chatbot", layout="centered")
st.title("🤖 Rule-Based Chatbot")

# Session State for Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey|hii)\b", user_input):
        return "Hello! How can I help you today?"
    elif re.search(r"\b(name|who are you)\b", user_input):
        return "I am a simple rule-based chatbot created for an AI/ML internship task."
    elif re.search(r"\b(help|support|assist)\b", user_input):
        return "Sure! You can ask me anything about this chatbot."
    elif re.search(r"\b(how.*work|function|rule)\b", user_input):
        return "I work using simple rule-based logic with if-else statements and pattern matching."
    elif re.search(r"\b(bye|exit|goodbye|see you)\b", user_input):
        return "Goodbye! Have a nice day. 😊"
    else:
        return "Sorry, I didn't understand that. Try asking something else."

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

# Respond when user presses enter
if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")

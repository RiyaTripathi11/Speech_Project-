import streamlit as st
from models.chat_model import chat_with_ai
from utils.speech_recognition import recognize_speech
from utils.text_to_speech import speak_text

# Streamlit UI
st.title("Groq AI Voice Chatbot")

if st.button("Speak"):
    user_input = recognize_speech()
    if user_input:
        response = chat_with_ai(user_input)
        st.write(f"AI: {response}")
        speak_text(response)

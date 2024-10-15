import requests
import streamlit as st
import streamlit_chat as sc
from dotenv import load_dotenv
from PIL import Image
import io
import os
from streamlit_chat import message  # streamlit_chat.message for displaying chat

load_dotenv()

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY', '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')}"}

# Query function to call the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI
st.header("Gideon - The AI Artist", divider="rainbow")
st.write("##### Gideon is an AI artist that can generate images based on your description. Describe a scene and Gideon will paint it for you!")
with st.expander("Instructions"):
    st.write("""
            - Explain you thoughts or imagination in the chatbox below.
            - Make sure the description is clear and detailed for better results.
            - It should have all the necessary details like objects, colors, and actions.
            - For example, "A beautiful sunset with a calm ocean and a palm tree on the beach."
            """)
# Input field for the user prompt
prompt = st.chat_input("Explain your Imaginations")

if prompt:
    with st.spinner("Generating..."):
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))

        # Append user prompt and assistant's image response to chat history
        st.session_state['chat_history'].append({"role": "user", "content": prompt})
        st.session_state['chat_history'].append({"role": "assistant", "content": image})

# Display the chat history using streamlit_chat.message
for chat in st.session_state['chat_history']:
    if chat['role'] == "user":
        with st.chat_message("user"):
            st.write(chat['content'])
    elif chat['role'] == "assistant":
        with st.chat_message("assistant"):
            st.image(chat['content'], use_column_width=True)

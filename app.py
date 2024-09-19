import requests
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import io
import os

load_dotenv()

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY', "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")}"}

# Query function to call the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit UI
st.title("AI-Generated Images with FLUX Model")

# Input field for the user prompt
prompt = st.text_input("Describe the scene:", 
					value="A girl holding a tablet and is making conversation with a Robot who is responsible. The picture should be in a landscape format")

# Button to generate image
if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Image", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("Powered by [Hugging Face](https://huggingface.co/models/black-forest-labs/FLUX.1-schnell)")

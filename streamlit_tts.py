import streamlit as st
from gtts import gTTS
import io
import base64

# Streamlit app title
st.title("Text-to-Speech Converter")

# Text input
text = st.text_area("Enter the text you want to convert to audio:")

# Convert button
if st.button("Convert to Audio"):
    if text:
        # Generate audio
        tts = gTTS(text, lang='en', tld='co.in')
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)

        # Save audio to a fixed filename
        audio_filename = "output.mp3"
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(audio_bytes.read())

        audio_b64 = base64.b64encode(audio_bytes.getvalue()).decode()
        href = f'<a href="data:audio/mp3;base64,{audio_b64}" download="output.mp3">Download Audio</a>'
        st.markdown(href, unsafe_allow_html=True)
st.beta_set_page_config(footer=False)
# Info and instructions
st.markdown("Instructions:")
st.markdown("1. Enter the text in the text box.")
st.markdown("2. Click the 'Convert to Audio' button.")
st.markdown("3. Download it using the link below.")

import streamlit as st
from gtts import gTTS
import os
import io

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
        tts.save(audio_bytes)

        # Display audio player
        st.audio(audio_bytes.getvalue(), format="audio/mp3")

        # Save audio to file
        audio_filename = "output.mp3"
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(audio_bytes.getvalue())
        st.markdown(f"[Download Audio](data:audio/mp3;base64,{audio_bytes.getvalue().hex()},output.mp3)")

# Info and instructions
st.markdown("Instructions:")
st.markdown("1. Enter the text in the text box.")
st.markdown("2. Click the 'Convert to Audio' button.")
st.markdown("3. Play the audio or download it using the link below.")

# Footer
st.markdown("Made with ❤️ by Your Name")

# Hide Streamlit menu
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

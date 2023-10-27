import streamlit as st
from moviepy.editor import *
import tempfile
import base64

# Streamlit app title for the new feature
st.title("Video to Audio Extractor")

# Video file upload
video_file = st.file_uploader("Upload a video file:", type=['mp4', 'mkv', 'avi', 'mov'])

if video_file:
    # Create a temporary file to store the uploaded video file
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(video_file.read())
    
    # Load the video file from the temporary file
    video_clip = VideoFileClip(tfile.name)
    
    # Convert video to audio
    audio = video_clip.audio
    audio_filename = tempfile.mktemp(suffix=".mp3")
    audio.write_audiofile(audio_filename)
    
    # Use a slider to allow the user to select a range of the audio to export
    selection = st.slider(
        "Select a range (in seconds):",
        0, int(video_clip.duration),
        (0, int(video_clip.duration))
    )

    # Export selected audio range
    if st.button("Export Selected Range"):
        start_time, end_time = selection
        selected_segment = audio.subclip(start_time, end_time)
        selected_audio_filename = tempfile.mktemp(suffix=".mp3")
        selected_segment.write_audiofile(selected_audio_filename)

        # Read the audio file and encode it to base64
        with open(selected_audio_filename, "rb") as f:
            audio_bytes = f.read()
        audio_b64 = base64.b64encode(audio_bytes).decode()

        # Create a download link for the audio file
        href = f'<a href="data:audio/mp3;base64,{audio_b64}" download="selected_range.mp3">Download Selected Range</a>'
        st.markdown(href, unsafe_allow_html=True)

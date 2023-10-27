import streamlit as st
from moviepy.editor import *
import tempfile

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
    
    # Now we'll handle the audio segment selection and export
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
        st.markdown(f'<a href="{selected_audio_filename}" download>Download Selected Range</a>', unsafe_allow_html=True)

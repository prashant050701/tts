import streamlit as st
from moviepy.editor import *
from pydub import AudioSegment
import tempfile

# Streamlit app title for the new feature
st.title("Video to Audio Extractor")

# Video file upload
video_file = st.file_uploader("Upload a video file:", type=['mp4', 'mkv', 'avi'])

if video_file:
    # Load the video file
    video_clip = VideoFileClip(video_file)
    
    # Convert video to audio
    audio = video_clip.audio
    audio_filename = tempfile.mktemp(suffix=".mp3")
    audio.write_audiofile(audio_filename)

    # Display audio player and download link
    st.audio(audio_filename, format='audio/mp3')
    st.markdown(f'<a href="{audio_filename}" download>Download Audio</a>', unsafe_allow_html=True)

    # Display audio waveform and selection bar
    audio_segment = AudioSegment.from_file(audio_filename)
    waveform = st.audio_waveform(audio_segment)
    selection = st.slider(
        "Select a range (in seconds):",
        0, len(audio_segment) // 1000,
        (0, len(audio_segment) // 1000)
    )

    # Export selected audio range
    if st.button("Export Selected Range"):
        start_time, end_time = selection
        selected_segment = audio_segment[start_time*1000:end_time*1000]
        selected_audio_filename = tempfile.mktemp(suffix=".mp3")
        selected_segment.export(selected_audio_filename, format="mp3")
        st.markdown(f'<a href="{selected_audio_filename}" download>Download Selected Range</a>', unsafe_allow_html=True)

import streamlit as st
import whisper
st.title("Shees Ikram's Audio Transcript App")
audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3","mp4"]  # Use list of allowed extensions
)

model=whisper.load_model("base")
st.text("Whisper Model Loaded :)")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio Wait")
        transcribing=model.transcribe(audio_file.name)
        st.sidebar.success("Transcribing Completed")
        st.markdown(transcribing["text"])
    else:
        st.sidebar.error("Please Upload Audio File")
        
st.header("Play Original Audio File")
st.audio(audio_file)



import os
import tempfile
from pathlib import Path
import streamlit as st

try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()

st.set_page_config(page_title="Audio Pipeline Tester - Demo", page_icon="🎧", layout="wide")

# Initialize session state
if "transcript" not in st.session_state:
    st.session_state["transcript"] = None
if "summary" not in st.session_state:
    st.session_state["summary"] = None
if "audio_path" not in st.session_state:
    st.session_state["audio_path"] = None
if "filename" not in st.session_state:
    st.session_state["filename"] = None

# Header
st.title("🎧 Audio Pipeline Tester - Demo Mode")
st.caption("Upload → Transcribe → Summarize → Export (Demo Version)")

with st.sidebar:
    st.header("Controls")
    uploaded = st.file_uploader("Upload audio (MP3/WAV)", type=["mp3", "wav", "m4a", "flac"]) 
    st.divider()
    st.subheader("Stages")
    col_a, col_b = st.columns(2)
    with col_a:
        trans_btn = st.button("Transcribe", type="primary", use_container_width=True, key="sidebar_transcribe")
    with col_b:
        sum_btn = st.button("Summarize", use_container_width=True, key="sidebar_summarize")
    
    st.divider()
    st.subheader("Workflow Status")
    
    # Status indicators
    status_items = []
    if st.session_state["audio_path"]:
        status_items.append("✅ Audio uploaded")
    if st.session_state["transcript"]:
        status_items.append("✅ Transcribed")
    if st.session_state["summary"]:
        status_items.append("✅ Summarized")
    
    if status_items:
        for item in status_items:
            st.write(item)
    else:
        st.write("⏳ Upload audio to begin")

# Persist uploaded file to temp
if uploaded is not None:
    if st.session_state["filename"] != uploaded.name:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded.name}") as tmp:
            tmp.write(uploaded.read())
            st.session_state["audio_path"] = tmp.name
            st.session_state["filename"] = uploaded.name

# Top-level info
with st.container(border=True):
    st.subheader("Audio Info")
    if st.session_state["audio_path"]:
        st.write(f"**Filename**: {st.session_state['filename']}")
        st.audio(st.session_state["audio_path"])
    else:
        st.info("Upload an audio file to begin.")

# Tabs
transcript_tab, summary_tab, export_tab = st.tabs(["Transcript Viewer", "Summary Viewer", "Export Options"])

# Handle buttons
if trans_btn:
    if not st.session_state["audio_path"]:
        st.error("❌ Please upload an audio file first!")
    else:
        st.info("🎵 Starting transcription...")
        with st.spinner("Transcribing with Whisper (Demo Mode)..."):
            # Demo transcription - create a mock transcript
            demo_transcript = f"""This is a demo transcript for the audio file: {st.session_state['filename']}

In a real deployment, this would be processed by Whisper AI to convert speech to text. The actual transcription would include:

1. Accurate speech-to-text conversion
2. Timestamp information for each segment
3. Speaker identification (if diarization is enabled)
4. Confidence scores for each word

For this demo, we're showing the structure of what the full application would provide. The real application includes:

- Whisper AI for speech recognition
- Speaker diarization using pyannote.audio
- Text summarization using Transformers
- Export to Markdown and PDF formats
- Email functionality with attachments

To use the full application, you would need to install all dependencies including:
- faster-whisper
- pyannote.audio
- transformers
- And other ML libraries

This demo shows the Streamlit interface and workflow structure."""
            
            st.session_state["transcript"] = demo_transcript
            st.success("✅ Demo transcription complete! Check the Transcript Viewer tab.")

if sum_btn:
    transcript = st.session_state.get('transcript') or ''
    if not transcript:
        st.warning("⚠️ Please transcribe first!")
    else:
        with st.spinner("Summarizing transcript (Demo Mode)..."):
            # Demo summarization
            demo_summary = f"""# Summary for {st.session_state.get('filename', 'audio file')}

## Key Points
- This is a demo summary showing the structure of what the full application would provide
- The actual summarization would use AI models to extract key insights
- Speaker identification and timestamps would be included

## Main Topics
1. **Audio Processing**: The application processes various audio formats
2. **AI Integration**: Uses multiple AI models for transcription and analysis
3. **Export Options**: Provides multiple export formats including PDF and Markdown
4. **Email Integration**: Can send results via email with attachments

## Technical Features
- **Speech-to-Text**: Whisper AI for accurate transcription
- **Speaker Diarization**: Identifies different speakers in conversations
- **Text Summarization**: AI-powered summarization of transcripts
- **Export Formats**: Markdown and PDF generation
- **Email Support**: SMTP and OAuth2 email integration

## Next Steps
To use the full application:
1. Install all dependencies from requirements.txt
2. Configure environment variables
3. Set up API keys for AI services
4. Deploy using the provided deployment scripts

This demo shows the complete workflow structure and user interface."""
            
            st.session_state["summary"] = demo_summary
            st.success("✅ Demo summary complete! Check the Summary Viewer tab.")

# Transcript tab content
with transcript_tab:
    st.subheader("Transcript")
    if st.session_state.get("transcript"):
        st.text_area("Transcript", value=st.session_state["transcript"], height=400)
        st.success("✓ Transcribed (Demo Mode)")
    else:
        st.info("No transcript yet. Click Transcribe.")

# Summary tab content
with summary_tab:
    st.subheader("Summary")
    if st.session_state.get("summary"):
        st.success("✓ Summarized (Demo Mode)")
        st.container(border=True).markdown(st.session_state["summary"]) 
    elif st.session_state.get("transcript"):
        st.info("Click Summarize to generate a summary.")
    else:
        st.info("No transcript available.")

# Export tab content
with export_tab:
    st.subheader("Export & Download")
    
    transcript = st.session_state.get('transcript') or ''
    summary = st.session_state.get('summary') or ''
    
    if transcript:
        st.success("✅ Content ready for export")
        
        # Markdown export
        if st.button("Export as Markdown", type="primary"):
            content = f"""# Audio Transcript: {st.session_state.get('filename', 'Unknown')}

## Transcript
{transcript}

## Summary
{summary}

---
*Generated by Audio Pipeline Tester Demo*"""
            
            st.download_button(
                label="Download Markdown",
                data=content,
                file_name=f"{Path(st.session_state.get('filename', 'transcript')).stem}.md",
                mime="text/markdown"
            )
        
        # Show content preview
        with st.expander("Preview Export Content", expanded=False):
            st.markdown(content)
    else:
        st.info("Please transcribe audio first to enable export.")

# Footer
st.divider()
st.info("""
**Demo Mode Notice**: This is a demonstration version of the Audio Pipeline Tester. 
The full application includes AI-powered transcription, speaker diarization, and summarization. 
To use the complete features, install all dependencies and configure the environment variables.
""")

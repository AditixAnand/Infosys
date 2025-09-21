# Audio Pipeline Tester - Streamlit App

A comprehensive audio processing application that provides end-to-end audio pipeline functionality including transcription, speaker diarization, summarization, and export capabilities.

## 🚀 Quick Start

### Option 1: Demo Mode (No Dependencies)
For a quick demo without installing heavy ML dependencies:

```bash
# Install minimal dependencies
pip install -r requirements-minimal.txt

# Run demo app
streamlit run app_demo.py
```

### Option 2: Full Application
For the complete application with all AI features:

```bash
# Automated setup
python deploy.py

# Or manual setup
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
streamlit run app.py
```

## 📋 Features

- **Audio Upload**: Support for MP3, WAV, M4A, FLAC formats
- **Speech-to-Text**: Whisper AI integration for accurate transcription
- **Speaker Diarization**: Identify different speakers in conversations
- **Text Summarization**: AI-powered summarization of transcripts
- **Export Options**: Markdown and PDF export with download buttons
- **Email Integration**: Send results via SMTP or OAuth2 (Gmail)
- **Interactive UI**: Clean Streamlit interface with progress tracking

## 🛠️ Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio processing)
- Optional: Hugging Face token for speaker diarization
- Optional: SMTP credentials for email functionality

## 📁 Project Structure

```
Audio Pipeline Tester/
├── app.py                 # Main Streamlit application
├── app_demo.py           # Demo version (minimal dependencies)
├── requirements.txt      # Full dependencies
├── requirements-minimal.txt  # Minimal dependencies for demo
├── deploy.py             # Automated deployment script
├── run.py                # Application runner script
├── test_app.py           # Test suite
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── services/             # Core functionality modules
│   ├── stt.py           # Speech-to-text
│   ├── diarization.py   # Speaker diarization
│   ├── summarization.py # Text summarization
│   ├── export_utils.py  # Export functionality
│   ├── email_utils.py   # Email utilities
│   └── utils/
│       └── audio.py     # Audio processing utilities
└── exports/             # Generated export files
```

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended)
- Push to GitHub
- Connect at [share.streamlit.io](https://share.streamlit.io)
- Configure environment variables in dashboard

### 2. Local Development
```bash
python run.py
```

### 3. Docker
```bash
docker build -t audio-pipeline-tester .
docker run -p 8501:8501 audio-pipeline-tester
```

### 4. Cloud Platforms
- Heroku
- Railway
- DigitalOcean App Platform
- AWS/GCP/Azure

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## ⚙️ Configuration

Copy `env.example` to `.env` and configure:

```env
# Whisper Model
WHISPER_MODEL_SIZE=small

# Hugging Face (for diarization)
HUGGINGFACE_TOKEN=your_token_here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

## 🧪 Testing

Run the test suite:
```bash
python test_app.py
```

## 📚 Documentation

- [Deployment Guide](DEPLOYMENT.md) - Detailed deployment instructions
- [Environment Setup](env.example) - Configuration template
- [Requirements](requirements.txt) - Full dependency list

## 🔧 Troubleshooting

### Common Issues:
1. **FFmpeg not found**: Install FFmpeg and ensure it's in PATH
2. **Model download fails**: Check internet connection and API tokens
3. **Memory issues**: Use smaller models or shorter audio files
4. **Email not working**: Verify SMTP credentials and firewall settings

### Getting Help:
1. Check the troubleshooting section in DEPLOYMENT.md
2. Review application logs
3. Test with the demo version first
4. Ensure all dependencies are installed correctly

## 📄 License

This project is open source and available under the MIT License.

---

**Ready to process audio? Start with the demo mode or deploy the full application! 🎧**

# Audio Pipeline Tester - Deployment Guide

This guide covers different deployment options for the Audio Pipeline Tester Streamlit application.

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.8 or higher
- FFmpeg installed on your system
- Git (optional, for version control)

### Automated Setup
```bash
# Run the deployment script
python deploy.py

# Start the application
python run.py
```

### Manual Setup
```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create environment file
cp env.example .env
# Edit .env with your configuration

# 5. Run the app
streamlit run app.py
```

## 🌐 Cloud Deployment Options

### 1. Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit apps.

#### Steps:
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Configure deployment settings:
   - **Main file path**: `app.py`
   - **Python version**: 3.8+
   - **Requirements file**: `requirements.txt`

#### Environment Variables in Streamlit Cloud:
Add these in the Streamlit Cloud dashboard:
```
WHISPER_MODEL_SIZE=small
HUGGINGFACE_TOKEN=your_token_here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_USE_TLS=true
```

### 2. Heroku

#### Prerequisites:
- Heroku CLI installed
- Git repository

#### Steps:
1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `runtime.txt`:
```
python-3.11.0
```

3. Deploy:
```bash
heroku create your-app-name
heroku config:set WHISPER_MODEL_SIZE=small
heroku config:set HUGGINGFACE_TOKEN=your_token_here
git push heroku main
```

### 3. Railway

#### Steps:
1. Connect your GitHub repository to Railway
2. Railway will automatically detect it's a Python app
3. Set environment variables in Railway dashboard
4. Deploy automatically

### 4. DigitalOcean App Platform

#### Steps:
1. Create a new app from GitHub
2. Configure build settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `streamlit run app.py --server.port=8080 --server.address=0.0.0.0`
3. Set environment variables
4. Deploy

### 5. AWS EC2 / Google Cloud / Azure

#### Steps:
1. Launch a VM instance
2. Install Python 3.8+, FFmpeg, and dependencies
3. Clone your repository
4. Set up environment variables
5. Run with Gunicorn for production:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn --bind 0.0.0.0:8501 --workers 1 --threads 8 --timeout 0 app:app
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `WHISPER_MODEL_SIZE` | Whisper model size | `small` | No |
| `HUGGINGFACE_TOKEN` | Hugging Face token for diarization | - | No |
| `SMTP_SERVER` | SMTP server for email | - | No |
| `SMTP_PORT` | SMTP port | `587` | No |
| `SMTP_USERNAME` | SMTP username | - | No |
| `SMTP_PASSWORD` | SMTP password | - | No |
| `SMTP_USE_TLS` | Use TLS for SMTP | `true` | No |

### Model Configuration

The app uses different AI models:
- **Whisper**: For speech-to-text transcription
- **pyannote.audio**: For speaker diarization
- **DistilBART**: For text summarization

Models are downloaded automatically on first use.

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
# Build the image
docker build -t audio-pipeline-tester .

# Run the container
docker run -p 8501:8501 -e WHISPER_MODEL_SIZE=small audio-pipeline-tester
```

## 🔒 Security Considerations

1. **Environment Variables**: Never commit `.env` files to version control
2. **API Keys**: Use secure methods to store API keys
3. **File Uploads**: The app has a 200MB upload limit
4. **CORS**: CORS is disabled by default for security

## 📊 Performance Optimization

1. **Model Caching**: Models are cached after first download
2. **File Cleanup**: Temporary files are cleaned up automatically
3. **Memory Management**: Large audio files are processed in chunks
4. **Concurrent Users**: For production, consider using multiple workers

## 🐛 Troubleshooting

### Common Issues:

1. **FFmpeg not found**:
   ```bash
   # Install FFmpeg
   # Windows: choco install ffmpeg
   # macOS: brew install ffmpeg
   # Ubuntu: sudo apt install ffmpeg
   ```

2. **Model download fails**:
   - Check internet connection
   - Verify Hugging Face token (if using diarization)

3. **Memory issues**:
   - Use smaller Whisper models
   - Process shorter audio files
   - Increase server memory

4. **Email not working**:
   - Check SMTP credentials
   - Verify app passwords for Gmail
   - Check firewall settings

### Logs and Debugging:

Enable debug mode by setting in `.streamlit/config.toml`:
```toml
[logger]
level = "debug"
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs
3. Create an issue in the repository
4. Check Streamlit documentation

## 🔄 Updates

To update the application:
1. Pull latest changes
2. Update dependencies: `pip install -r requirements.txt --upgrade`
3. Restart the application

---

**Happy Deploying! 🎉**

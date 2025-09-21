#!/usr/bin/env python3
"""
Deployment script for Audio Pipeline Tester Streamlit App
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        print("✅ FFmpeg is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg is not installed or not in PATH")
        print("Please install FFmpeg:")
        if platform.system() == "Windows":
            print("  - Using Chocolatey: choco install ffmpeg")
            print("  - Or download from https://ffmpeg.org")
        elif platform.system() == "Darwin":  # macOS
            print("  - Using Homebrew: brew install ffmpeg")
        else:  # Linux
            print("  - Using apt: sudo apt install ffmpeg")
            print("  - Using yum: sudo yum install ffmpeg")
        return False

def setup_environment():
    """Set up Python virtual environment"""
    if not os.path.exists(".venv"):
        if not run_command("python -m venv .venv", "Creating virtual environment"):
            return False
    
    # Activate virtual environment and install dependencies
    if platform.system() == "Windows":
        activate_cmd = ".venv\\Scripts\\activate"
        pip_cmd = ".venv\\Scripts\\pip"
    else:
        activate_cmd = "source .venv/bin/activate"
        pip_cmd = ".venv/bin/pip"
    
    # Upgrade pip
    if not run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        return False
    
    return True

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    if not os.path.exists(".env"):
        if os.path.exists("env.example"):
            print("📝 Creating .env file from template...")
            try:
                with open("env.example", "r") as src, open(".env", "w") as dst:
                    dst.write(src.read())
                print("✅ .env file created. Please edit it with your configuration.")
                return True
            except Exception as e:
                print(f"❌ Failed to create .env file: {e}")
                return False
        else:
            print("⚠️ No env.example file found. Creating basic .env file...")
            try:
                with open(".env", "w") as f:
                    f.write("WHISPER_MODEL_SIZE=small\n")
                print("✅ Basic .env file created.")
                return True
            except Exception as e:
                print(f"❌ Failed to create .env file: {e}")
                return False
    else:
        print("✅ .env file already exists")
        return True

def main():
    """Main deployment function"""
    print("🚀 Audio Pipeline Tester - Deployment Script")
    print("=" * 50)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    if not check_ffmpeg():
        print("\n⚠️ Please install FFmpeg and run this script again.")
        sys.exit(1)
    
    # Set up environment
    if not setup_environment():
        print("\n❌ Environment setup failed")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("\n❌ Failed to create .env file")
        sys.exit(1)
    
    print("\n🎉 Deployment setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Run the app with: streamlit run app.py")
    print("3. Or use the run script: python run.py")

if __name__ == "__main__":
    main()

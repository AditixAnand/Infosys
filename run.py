#!/usr/bin/env python3
"""
Run script for Audio Pipeline Tester Streamlit App
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_streamlit():
    """Run the Streamlit app"""
    print("🚀 Starting Audio Pipeline Tester...")
    
    # Check if virtual environment exists
    if not os.path.exists(".venv"):
        print("❌ Virtual environment not found. Please run deploy.py first.")
        sys.exit(1)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("⚠️ .env file not found. Creating from template...")
        if os.path.exists("env.example"):
            with open("env.example", "r") as src, open(".env", "w") as dst:
                dst.write(src.read())
            print("✅ .env file created from template")
        else:
            print("❌ No env.example file found. Please create .env manually.")
            sys.exit(1)
    
    # Determine the correct Python executable
    if platform.system() == "Windows":
        python_cmd = ".venv\\Scripts\\python"
        streamlit_cmd = ".venv\\Scripts\\streamlit"
    else:
        python_cmd = ".venv/bin/python"
        streamlit_cmd = ".venv/bin/streamlit"
    
    # Check if streamlit is installed
    try:
        subprocess.run([streamlit_cmd, "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Streamlit not found in virtual environment. Please run deploy.py first.")
        sys.exit(1)
    
    # Run the app
    print("🌐 Starting Streamlit server...")
    print("📱 The app will open in your browser at http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([streamlit_cmd, "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start Streamlit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_streamlit()

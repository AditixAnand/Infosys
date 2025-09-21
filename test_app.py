#!/usr/bin/env python3
"""
Test script for Audio Pipeline Tester Streamlit App
Tests basic functionality without requiring FFmpeg
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import faster_whisper
        print("✅ faster-whisper imported successfully")
    except ImportError as e:
        print(f"❌ faster-whisper import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        import transformers
        print("✅ Transformers imported successfully")
    except ImportError as e:
        print(f"❌ Transformers import failed: {e}")
        return False
    
    try:
        import reportlab
        print("✅ ReportLab imported successfully")
    except ImportError as e:
        print(f"❌ ReportLab import failed: {e}")
        return False
    
    return True

def test_services():
    """Test if service modules can be imported"""
    print("\n🧪 Testing service modules...")
    
    try:
        from services.stt import transcribe_audio
        print("✅ STT service imported successfully")
    except ImportError as e:
        print(f"❌ STT service import failed: {e}")
        return False
    
    try:
        from services.diarization import diarize_audio
        print("✅ Diarization service imported successfully")
    except ImportError as e:
        print(f"❌ Diarization service import failed: {e}")
        return False
    
    try:
        from services.summarization import summarize_text
        print("✅ Summarization service imported successfully")
    except ImportError as e:
        print(f"❌ Summarization service import failed: {e}")
        return False
    
    try:
        from services.export_utils import export_markdown, export_pdf
        print("✅ Export utilities imported successfully")
    except ImportError as e:
        print(f"❌ Export utilities import failed: {e}")
        return False
    
    return True

def test_streamlit_config():
    """Test if Streamlit configuration is valid"""
    print("\n🧪 Testing Streamlit configuration...")
    
    config_path = Path(".streamlit/config.toml")
    if not config_path.exists():
        print("❌ Streamlit config file not found")
        return False
    
    try:
        import toml
        with open(config_path, 'r') as f:
            config = toml.load(f)
        print("✅ Streamlit config is valid TOML")
        return True
    except ImportError:
        print("⚠️ TOML parser not available, skipping config validation")
        return True
    except Exception as e:
        print(f"❌ Streamlit config validation failed: {e}")
        return False

def test_app_structure():
    """Test if the app has the required structure"""
    print("\n🧪 Testing app structure...")
    
    required_files = [
        "app.py",
        "requirements.txt",
        "services/__init__.py",
        "services/stt.py",
        "services/diarization.py",
        "services/summarization.py",
        "services/export_utils.py",
        "services/email_utils.py",
        "services/oauth_email.py",
        "services/utils/__init__.py",
        "services/utils/audio.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files present")
    return True

def test_environment_setup():
    """Test environment setup"""
    print("\n🧪 Testing environment setup...")
    
    # Check if .env file exists or can be created
    if not Path(".env").exists():
        if Path("env.example").exists():
            print("✅ .env file can be created from template")
        else:
            print("⚠️ No .env or env.example file found")
    else:
        print("✅ .env file exists")
    
    # Check if virtual environment exists
    venv_path = Path(".venv")
    if venv_path.exists():
        print("✅ Virtual environment exists")
    else:
        print("⚠️ Virtual environment not found (run deploy.py first)")
    
    return True

def main():
    """Main test function"""
    print("🧪 Audio Pipeline Tester - Test Suite")
    print("=" * 50)
    
    tests = [
        ("App Structure", test_app_structure),
        ("Environment Setup", test_environment_setup),
        ("Streamlit Config", test_streamlit_config),
        ("Core Imports", test_imports),
        ("Service Imports", test_services),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} test...")
        if test_func():
            passed += 1
            print(f"✅ {test_name} test passed")
        else:
            print(f"❌ {test_name} test failed")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The app is ready for deployment.")
        return True
    else:
        print("⚠️ Some tests failed. Please fix the issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

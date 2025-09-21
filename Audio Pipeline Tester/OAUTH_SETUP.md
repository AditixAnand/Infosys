# 🔐 OAuth2 Email Setup Guide

This guide will help you set up OAuth2 authentication for sending emails through Gmail, which is more secure than using App Passwords.

## 📋 Prerequisites

1. A Google account
2. Python environment with the required libraries

## 🚀 Step-by-Step Setup

### Step 1: Install Required Libraries

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 2: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name: "Streamlit Email App" (or any name you prefer)
4. Click "Create"

### Step 3: Enable Gmail API

1. In your project, go to "APIs & Services" → "Library"
2. Search for "Gmail API"
3. Click on "Gmail API" → "Enable"

### Step 4: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth 2.0 Client IDs"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in required fields (App name, User support email, Developer email)
   - Add your email to test users
4. For Application type, choose "Desktop application"
5. Give it a name like "Streamlit Email Client"
6. Click "Create"

### Step 5: Download Credentials

1. After creating the OAuth client, click the download button (⬇️)
2. Save the file as `credentials.json`
3. Place `credentials.json` in your project folder: `C:\Users\91799\Downloads\infosys_fixed\`

### Step 6: Test the Setup

1. Run your Streamlit app
2. Go to the "Export Options" tab
3. Select "OAuth2 (Gmail)" as email method
4. Click "Test OAuth2 Connection"
5. Your browser will open for authentication
6. Grant permissions to the app
7. You should see "✅ Connected as: your-email@gmail.com"

## 🔒 Security Features

- **No passwords stored**: Uses secure OAuth2 tokens
- **Automatic refresh**: Tokens refresh automatically
- **Scoped permissions**: Only sends emails, doesn't read them
- **Revocable access**: Can be revoked from Google Account settings

## 📁 File Structure

After setup, your project should have:
```
infosys_fixed/
├── app.py
├── credentials.json          # Downloaded from Google Cloud
├── token.json               # Created after first authentication
├── services/
│   ├── oauth_email.py
│   └── ...
└── requirements.txt
```

## 🛠️ Troubleshooting

### "credentials.json not found"
- Make sure you downloaded the file from Google Cloud Console
- Check that it's in the correct project folder
- Verify the file name is exactly `credentials.json`

### "OAuth libraries not installed"
- Run: `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`

### "Connection failed"
- Check your internet connection
- Verify the Gmail API is enabled in Google Cloud Console
- Try deleting `token.json` and re-authenticating

### "Access blocked"
- Make sure you added your email to test users in OAuth consent screen
- Check that the OAuth consent screen is properly configured

## 🎉 Success!

Once set up, you can:
- Send real emails through Gmail
- No need for App Passwords
- Secure OAuth2 authentication
- Works with any Gmail account

The app will automatically use OAuth2 when you select "OAuth2 (Gmail)" as the email method!

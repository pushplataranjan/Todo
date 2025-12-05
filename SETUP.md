# Setup Guide for Todo Workshop App

## Quick Setup (5 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/pushplata-ranjan9/Todo.git
cd Todo
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
# Copy example file
cp .env.example .env

# Edit .env file (optional for basic functionality)
# For email notifications, configure:
# MAIL_USERNAME=your-email@gmail.com
# MAIL_PASSWORD=your-app-password
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Open in Browser
```
http://localhost:5000
```

## Email Configuration (Optional)

### Gmail Setup

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable **2-Step Verification**
3. Go to **App Passwords**
4. Generate a new app password for "Mail"
5. Copy the 16-character password
6. Update `.env` file:
   ```env
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-16-char-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ENABLE_EMAIL_NOTIFICATIONS=True
   ```

### Other Email Providers

**Outlook/Hotmail:**
```env
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

**Yahoo:**
```env
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py (last line)
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database Issues
```bash
# Delete and recreate database
rm todo.db  # or del todo.db on Windows
python app.py
```

### Module Not Found
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Email Not Working
- Check `.env` configuration
- Verify app password is correct
- Check firewall/antivirus settings
- Try disabling email: `ENABLE_EMAIL_NOTIFICATIONS=False`

## Development Mode

```bash
# Set environment variable
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

# Run with auto-reload
python app.py
```

## Next Steps

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
2. Check [ISSUES.md](ISSUES.md) for available issues
3. Start contributing! 🚀


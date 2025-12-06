# 📝 Todo Workshop App

A full-stack Todo application built with Python (Flask) backend and vanilla JavaScript frontend. This project is designed for first-time contributors to learn and practice web development.

![Todo App](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- ✅ Create, read, update, and delete todos
- 🏷️ Priority levels (Low, Medium, High)
- 📅 Due dates and categories
- 🏷️ Tags for better organization
- 📊 Statistics dashboard
- 🔔 Email and browser notifications
- 🔍 Search and filter functionality
- 📱 Responsive design
- 🎨 Modern, clean UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pushplata-ranjan9/Todo.git
   cd Todo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   # Copy example environment file
   cp .env.example .env
   
   # Edit .env file with your settings
   # For email notifications, configure:
   # MAIL_USERNAME=your-email@gmail.com
   # MAIL_PASSWORD=your-app-password
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser: `http://localhost:5000`

## 📁 Project Structure

```
Todo/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── backend/
│   ├── __init__.py
│   ├── models.py              # Database models (Todo, User, Notification)
│   ├── database.py            # Database configuration
│   ├── routes/                # API endpoints
│   │   ├── todo_routes.py     # Todo CRUD operations
│   │   ├── user_routes.py     # User management
│   │   └── notification_routes.py  # Notification endpoints
│   └── services/              # Business logic
│       ├── email_service.py    # Email notification service
│       └── notification_service.py  # Notification management
└── static/
    ├── index.html             # Main HTML file
    ├── styles.css             # Styling
    ├── app.js                 # Frontend JavaScript
    └── manifest.json          # PWA manifest
```

## 🎯 API Endpoints

### Todos
- `GET /api/todos` - Get all todos (with filters)
- `GET /api/todos/<id>` - Get single todo
- `POST /api/todos` - Create new todo
- `PUT /api/todos/<id>` - Update todo
- `DELETE /api/todos/<id>` - Delete todo
- `POST /api/todos/<id>/complete` - Toggle completion
- `GET /api/todos/stats` - Get statistics

### Users
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get single user
- `POST /api/users` - Create user
- `PUT /api/users/<id>` - Update user

### Notifications
- `GET /api/notifications` - Get notifications
- `POST /api/notifications/<id>/mark-read` - Mark as read
- `POST /api/notifications/check-due` - Check due todos

## 🔧 Configuration

### Email Notifications

To enable email notifications:

1. **Gmail Setup** (Recommended for testing)
   - Go to your Google Account settings
   - Enable 2-Step Verification
   - Generate an App Password
   - Use the app password in `.env` file

2. **Update `.env` file**
   ```env
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ENABLE_EMAIL_NOTIFICATIONS=True
   ```

### Browser Notifications

Browser notifications are enabled by default. The app will request permission when first loaded.

## 🎓 For Workshop Participants

This project is designed for first-time contributors! Here's how to get started:

1. **Read the Contributing Guide**
   - See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions

2. **Find an Issue**
   - Check the [Issues](https://github.com/pushplata-ranjan9/Todo/issues) page
   - Look for `good first issue` or `beginner-friendly` labels
   - Issues are categorized as Frontend or Backend

3. **Start Contributing**
   - Fork the repository
   - Create a branch for your work
   - Make your changes
   - Submit a Pull Request

## 🐛 Troubleshooting

### Database Issues
```bash
# Delete existing database and recreate
rm todo.db
python app.py
```

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Email Not Working
- Check your `.env` configuration
- Verify app password is correct
- Check firewall settings
- Try with `ENABLE_EMAIL_NOTIFICATIONS=False` to disable

## 🛠️ Development

### Running in Development Mode
```bash
# Set Flask environment
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

# Run with auto-reload
python app.py
```

### Database Migrations
The app uses SQLite by default. To reset:
```bash
rm todo.db
python app.py  # Will create new database
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 👥 Authors

- **Pushplata Ranjan** - Initial work - [pushplata-ranjan9](https://github.com/pushplata-ranjan9)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- All contributors who help improve this project
- Workshop participants for their feedback and contributions

## 📞 Support

If you have questions or need help:
- Open an issue on GitHub
- Check existing issues and discussions
- Review the code comments

---
#demo

**Happy Coding! 🚀**

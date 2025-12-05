# Contributing to Todo Workshop App

Thank you for your interest in contributing! This project is designed for first-time contributors to learn and practice.

## 🎯 Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/pushplata-ranjan9/Todo.git
   cd Todo
   ```

2. **Set up the environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure the application**
   ```bash
   # Copy example environment file
   cp .env.example .env
   
   # Edit .env with your settings
   # For email notifications, configure MAIL_USERNAME and MAIL_PASSWORD
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to: `http://localhost:5000`

## 📋 How to Contribute

### Finding Issues

- Check the [Issues](https://github.com/pushplata-ranjan9/Todo/issues) page
- Look for labels: `good first issue`, `beginner-friendly`, `frontend`, `backend`
- Issues are categorized as:
  - **Frontend**: HTML, CSS, JavaScript improvements
  - **Backend**: Python, Flask, API improvements

### Making Changes

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add comments where necessary
   - Follow existing code style

3. **Test your changes**
   - Make sure the app runs without errors
   - Test the feature you added/modified
   - Check for any console errors

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Description of your changes"
   ```

5. **Push and create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   - Go to GitHub and create a Pull Request
   - Fill out the PR template
   - Link the issue you're addressing

## 🏗️ Project Structure

```
Todo/
├── app.py                 # Main Flask application
├── backend/
│   ├── models.py          # Database models
│   ├── database.py        # Database configuration
│   ├── routes/            # API routes
│   │   ├── todo_routes.py
│   │   ├── user_routes.py
│   │   └── notification_routes.py
│   └── services/          # Business logic
│       ├── email_service.py
│       └── notification_service.py
├── static/
│   ├── index.html         # Frontend HTML
│   ├── styles.css         # Frontend CSS
│   └── app.js             # Frontend JavaScript
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🎨 Code Style

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### JavaScript
- Use modern ES6+ syntax
- Use `const` and `let` instead of `var`
- Use arrow functions where appropriate
- Add comments for complex logic

### CSS
- Use meaningful class names
- Follow BEM naming convention where possible
- Keep styles organized and commented

## 🧪 Testing

Before submitting a PR, make sure:
- [ ] The application runs without errors
- [ ] Your feature works as expected
- [ ] No console errors appear
- [ ] Code follows the project style
- [ ] You've tested on different browsers (if frontend)

## 📝 Commit Messages

Use clear, descriptive commit messages:
- `Add: Feature description`
- `Fix: Bug description`
- `Update: What was updated`
- `Refactor: What was refactored`
- `Docs: Documentation update`

## 🐛 Reporting Bugs

If you find a bug:
1. Check if it's already reported
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

## 💡 Suggesting Features

Have an idea? Create an issue with:
- Clear description of the feature
- Why it would be useful
- How it might work

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [CSS Tricks](https://css-tricks.com/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## ❓ Need Help?

- Open an issue with the `question` label
- Check existing issues and discussions
- Review the code comments

## 🙏 Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute!


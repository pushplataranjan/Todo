"""
Todo Application - Main Entry Point
A full-stack Todo application for workshop contributors
"""
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_mail import Mail
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='')

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', '')

# Initialize extensions
from backend.database import db
db.init_app(app)

CORS(app)  # Enable CORS for frontend
mail = Mail(app)

# Register blueprints
from backend.routes.todo_routes import todo_bp
from backend.routes.notification_routes import notification_bp
from backend.routes.user_routes import user_bp
app.register_blueprint(todo_bp, url_prefix='/api/todos')
app.register_blueprint(notification_bp, url_prefix='/api/notifications')
app.register_blueprint(user_bp, url_prefix='/api/users')

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('static', path)

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'message': 'Todo API is running'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


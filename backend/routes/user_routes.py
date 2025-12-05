"""
User API routes
"""
from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import User

user_bp = Blueprint('users', __name__)


@user_bp.route('', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a single user by ID"""
    try:
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({'error': 'Username and email are required'}), 400
        
        # Check if user already exists
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists'}), 400
        
        user = User(
            username=data['username'],
            email=data['email'],
            email_notifications_enabled=data.get('email_notifications_enabled', True),
            browser_notifications_enabled=data.get('browser_notifications_enabled', True)
        )
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify(user.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user settings"""
    try:
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        if 'email' in data:
            # Check if email is already taken by another user
            existing = User.query.filter_by(email=data['email']).first()
            if existing and existing.id != user_id:
                return jsonify({'error': 'Email already exists'}), 400
            user.email = data['email']
        
        if 'email_notifications_enabled' in data:
            user.email_notifications_enabled = data['email_notifications_enabled']
        
        if 'browser_notifications_enabled' in data:
            user.browser_notifications_enabled = data['browser_notifications_enabled']
        
        db.session.commit()
        return jsonify(user.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


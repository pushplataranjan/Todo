"""
Todo API routes
"""
from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Todo, User
from backend.services.notification_service import NotificationService
from datetime import datetime
import os

todo_bp = Blueprint('todos', __name__)


@todo_bp.route('', methods=['GET'])
def get_todos():
    """Get all todos with optional filters"""
    try:
        # Get query parameters
        completed = request.args.get('completed')
        priority = request.args.get('priority')
        category = request.args.get('category')
        user_id = request.args.get('user_id', type=int)
        search = request.args.get('search')
        
        # Build query
        query = Todo.query
        
        if completed is not None:
            query = query.filter(Todo.completed == (completed.lower() == 'true'))
        
        if priority:
            query = query.filter(Todo.priority == priority)
        
        if category:
            query = query.filter(Todo.category == category)
        
        if user_id:
            query = query.filter(Todo.user_id == user_id)
        
        if search:
            query = query.filter(
                (Todo.title.contains(search)) | 
                (Todo.description.contains(search))
            )
        
        todos = query.order_by(Todo.created_at.desc()).all()
        return jsonify([todo.to_dict() for todo in todos]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a single todo by ID"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@todo_bp.route('', methods=['POST'])
def create_todo():
    """Create a new todo"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        # Get or create user
        user_id = data.get('user_id')
        user = None
        if user_id:
            user = User.query.get(user_id)
        
        # Create todo
        todo = Todo(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=datetime.fromisoformat(data['due_date']) if data.get('due_date') else None,
            user_id=user_id,
            category=data.get('category'),
            tags=','.join(data.get('tags', [])) if isinstance(data.get('tags'), list) else data.get('tags')
        )
        
        db.session.add(todo)
        db.session.commit()
        
        # Send notification if user exists
        if user and os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            NotificationService.create_notification(todo, user, 'created')
        
        return jsonify(todo.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing todo"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        data = request.get_json()
        
        # Update fields
        if 'title' in data:
            todo.title = data['title']
        if 'description' in data:
            todo.description = data.get('description')
        if 'completed' in data:
            todo.completed = data['completed']
        if 'priority' in data:
            todo.priority = data['priority']
        if 'due_date' in data:
            todo.due_date = datetime.fromisoformat(data['due_date']) if data['due_date'] else None
        if 'category' in data:
            todo.category = data.get('category')
        if 'tags' in data:
            todo.tags = ','.join(data['tags']) if isinstance(data['tags'], list) else data['tags']
        
        todo.updated_at = datetime.utcnow()
        db.session.commit()
        
        # Send notification
        if todo.user and os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            notification_type = 'completed' if todo.completed else 'updated'
            NotificationService.create_notification(todo, todo.user, notification_type)
        
        return jsonify(todo.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        user = todo.user
        
        db.session.delete(todo)
        db.session.commit()
        
        # Send notification
        if user and os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            # Create a temporary todo object for notification
            temp_todo = type('obj', (object,), {'id': None, 'title': 'Deleted Todo', 'user': user})()
            NotificationService.create_notification(temp_todo, user, 'deleted')
        
        return jsonify({'message': 'Todo deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>/complete', methods=['POST'])
def toggle_complete(todo_id):
    """Toggle todo completion status"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        todo.completed = not todo.completed
        todo.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        # Send notification
        if todo.user and os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            NotificationService.create_notification(todo, todo.user, 'completed' if todo.completed else 'updated')
        
        return jsonify(todo.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@todo_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get todo statistics"""
    try:
        user_id = request.args.get('user_id', type=int)
        query = Todo.query
        if user_id:
            query = query.filter(Todo.user_id == user_id)
        
        total = query.count()
        completed = query.filter(Todo.completed == True).count()
        pending = total - completed
        
        # Priority breakdown
        high_priority = query.filter(Todo.priority == 'high', Todo.completed == False).count()
        medium_priority = query.filter(Todo.priority == 'medium', Todo.completed == False).count()
        low_priority = query.filter(Todo.priority == 'low', Todo.completed == False).count()
        
        return jsonify({
            'total': total,
            'completed': completed,
            'pending': pending,
            'high_priority': high_priority,
            'medium_priority': medium_priority,
            'low_priority': low_priority
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


"""
Notification service for managing browser and email notifications
"""
from backend.database import db
from backend.models import Notification, User, Todo
from backend.services.email_service import EmailService
from datetime import datetime, timedelta
import os


class NotificationService:
    """Service for managing all types of notifications"""
    
    @staticmethod
    def create_notification(todo, user, notification_type='created', send_email=True):
        """
        Create and send notification for a todo event
        
        Args:
            todo: Todo object
            user: User object
            notification_type: Type of notification
            send_email: Whether to send email notification
        """
        # Create browser notification record
        notification = Notification(
            todo_id=todo.id,
            user_id=user.id,
            message=f"Todo {notification_type}: {todo.title}",
            type='browser',
            sent=False
        )
        db.session.add(notification)
        
        # Send email if enabled
        if send_email and os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            EmailService.send_todo_notification(todo, user, notification_type)
        
        db.session.commit()
        return notification
    
    @staticmethod
    def get_pending_notifications(user_id, limit=50):
        """Get pending browser notifications for a user"""
        notifications = Notification.query.filter_by(
            user_id=user_id,
            type='browser',
            sent=False
        ).order_by(Notification.created_at.desc()).limit(limit).all()
        
        return [n.to_dict() for n in notifications]
    
    @staticmethod
    def mark_notification_sent(notification_id):
        """Mark a notification as sent"""
        notification = Notification.query.get(notification_id)
        if notification:
            notification.sent = True
            notification.sent_at = datetime.utcnow()
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def check_due_todos():
        """Check for todos that are due soon and send notifications"""
        # Get todos due in next 24 hours
        due_soon = datetime.utcnow() + timedelta(hours=24)
        
        todos = Todo.query.filter(
            Todo.completed == False,
            Todo.due_date.isnot(None),
            Todo.due_date <= due_soon,
            Todo.due_date > datetime.utcnow()
        ).all()
        
        notifications_sent = []
        for todo in todos:
            if todo.user:
                # Check if notification already sent
                existing = Notification.query.filter_by(
                    todo_id=todo.id,
                    user_id=todo.user.id,
                    type='email',
                    message__like='%due soon%'
                ).first()
                
                if not existing:
                    EmailService.send_todo_notification(todo, todo.user, 'due_soon')
                    notifications_sent.append(todo.id)
        
        return notifications_sent


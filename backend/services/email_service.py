"""
Email notification service
"""
from flask import current_app
from flask_mail import Message
from backend.database import db
from backend.models import Notification, User, Todo
from datetime import datetime
import os


class EmailService:
    """Service for sending email notifications"""
    
    @staticmethod
    def send_todo_notification(todo, user, notification_type='created'):
        """
        Send email notification for todo events
        
        Args:
            todo: Todo object
            user: User object
            notification_type: Type of notification (created, completed, due_soon, etc.)
        """
        if not os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            return False
        
        if not user.email_notifications_enabled:
            return False
        
        try:
            from flask import current_app
            from flask_mail import Message
            
            # Create notification message based on type
            messages = {
                'created': f'New Todo Created: {todo.title}',
                'completed': f'Todo Completed: {todo.title}',
                'due_soon': f'Reminder: Todo "{todo.title}" is due soon!',
                'updated': f'Todo Updated: {todo.title}',
                'deleted': f'Todo Deleted: {todo.title}'
            }
            
            subject = messages.get(notification_type, f'Todo Update: {todo.title}')
            
            # Create email body
            body = f"""
            <html>
            <body>
                <h2>Todo Notification</h2>
                <p><strong>Title:</strong> {todo.title}</p>
                <p><strong>Description:</strong> {todo.description or 'No description'}</p>
                <p><strong>Priority:</strong> {todo.priority}</p>
                <p><strong>Status:</strong> {'Completed' if todo.completed else 'Pending'}</p>
                {f'<p><strong>Due Date:</strong> {todo.due_date.strftime("%Y-%m-%d %H:%M")}</p>' if todo.due_date else ''}
                <p><strong>Category:</strong> {todo.category or 'Uncategorized'}</p>
                <hr>
                <p>This is an automated notification from Todo Workshop App.</p>
            </body>
            </html>
            """
            
            msg = Message(
                subject=subject,
                recipients=[user.email],
                html=body
            )
            
            mail.send(msg)
            
            # Create notification record
            notification = Notification(
                todo_id=todo.id,
                user_id=user.id,
                message=subject,
                type='email',
                sent=True,
                sent_at=datetime.utcnow()
            )
            db.session.add(notification)
            db.session.commit()
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            # Create failed notification record
            notification = Notification(
                todo_id=todo.id,
                user_id=user.id,
                message=f"Failed to send: {subject}",
                type='email',
                sent=False
            )
            db.session.add(notification)
            db.session.commit()
            return False
    
    @staticmethod
    def send_bulk_notifications(todos, user, notification_type='due_soon'):
        """Send bulk email notifications for multiple todos"""
        if not os.getenv('ENABLE_EMAIL_NOTIFICATIONS', 'True').lower() == 'true':
            return False
        
        if not user.email_notifications_enabled:
            return False
        
        try:
            from flask import current_app
            from flask_mail import Message
            
            subject = f"Reminder: {len(todos)} Todo(s) Due Soon"
            
            body = f"""
            <html>
            <body>
                <h2>Todo Reminders</h2>
                <p>You have {len(todos)} todo(s) that are due soon:</p>
                <ul>
            """
            
            for todo in todos:
                body += f"""
                    <li>
                        <strong>{todo.title}</strong><br>
                        Due: {todo.due_date.strftime("%Y-%m-%d %H:%M") if todo.due_date else 'No due date'}<br>
                        Priority: {todo.priority}
                    </li>
                """
            
            body += """
                </ul>
                <hr>
                <p>This is an automated notification from Todo Workshop App.</p>
            </body>
            </html>
            """
            
            msg = Message(
                subject=subject,
                recipients=[user.email],
                html=body
            )
            
            # Use mail from app context
            mail = current_app.extensions.get('mail')
            if mail:
                mail.send(msg)
            else:
                from flask_mail import Mail
                mail = Mail(current_app)
                mail.send(msg)
            return True
            
        except Exception as e:
            print(f"Error sending bulk email: {str(e)}")
            return False


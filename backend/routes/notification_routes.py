"""
Notification API routes
"""
from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Notification, User
from backend.services.notification_service import NotificationService

notification_bp = Blueprint('notifications', __name__)


@notification_bp.route('', methods=['GET'])
def get_notifications():
    """Get notifications for a user"""
    try:
        user_id = request.args.get('user_id', type=int)
        if not user_id:
            return jsonify({'error': 'user_id is required'}), 400
        
        limit = request.args.get('limit', 50, type=int)
        pending_only = request.args.get('pending_only', 'false').lower() == 'true'
        
        if pending_only:
            notifications = NotificationService.get_pending_notifications(user_id, limit)
        else:
            notifications = Notification.query.filter_by(user_id=user_id)\
                .order_by(Notification.created_at.desc()).limit(limit).all()
            notifications = [n.to_dict() for n in notifications]
        
        return jsonify(notifications), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@notification_bp.route('/<int:notification_id>/mark-read', methods=['POST'])
def mark_notification_read(notification_id):
    """Mark a notification as read/sent"""
    try:
        success = NotificationService.mark_notification_sent(notification_id)
        if success:
            return jsonify({'message': 'Notification marked as read'}), 200
        else:
            return jsonify({'error': 'Notification not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@notification_bp.route('/check-due', methods=['POST'])
def check_due_todos():
    """Manually trigger check for due todos"""
    try:
        notifications_sent = NotificationService.check_due_todos()
        return jsonify({
            'message': f'Checked due todos, {len(notifications_sent)} notifications sent',
            'notifications_sent': notifications_sent
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


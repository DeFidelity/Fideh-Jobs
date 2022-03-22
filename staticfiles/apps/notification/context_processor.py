from .models import Notification 

def get_notifications(request):
    if request.user.is_authenticated:
        read_notifications = request.user.notifications.filter(is_read=True)
        unread_notifications = request.user.notifications.filter(is_read=False)
        context ={
            'read_notifications': read_notifications,
            'unread_notifications': unread_notifications
        }
        return context
    else:
        context ={
            'read_notifications': [],
            'unread_notifications': []
        }
        return context
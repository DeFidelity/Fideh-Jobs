from .models import Notification

def create_notification(request, to_user, notification_type, extra_pk=0):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, created_by=request.user, extra_pk=extra_pk)
    
    
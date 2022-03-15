from django.test import SimpleTestCase 
from django.urls import reverse, resolve

from apps.notification.views import NotificationListView

class TestNotificationUrl(SimpleTestCase):
    def test_notification_url(self):
        not_url = reverse('notification:notification')
        
        response = resolve(not_url)
        
        self.assertEqual(response.func.view_class,NotificationListView)
        self.assertTemplateUsed('notification/notification.html')
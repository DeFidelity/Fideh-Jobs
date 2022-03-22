from django.test import TestCase, Client
from django.urls import reverse
from apps.notification.models import Notification

from apps.users.models import CustomUser 


class TestNotificationViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.just_user = CustomUser.objects.create_user( 
            first_name = 'justuser',
            email='mine@mail.com',
            password ='testpassword'                                
        )
        
        self.employer_user = CustomUser.objects.create_user(
            first_name = 'admin',
            email = 'admin@mail.com',
            password ='testpassword',
        )
        
        self.notification = Notification.objects.create(
            to_user = self.just_user,
            created_by = self.employer_user,
            notification_type = 'message',
            is_read = False
        )
        
    def test_notification_views_with_GET_method(self):
        notification = reverse('notification:notification')
        
        self.client.login(email=self.just_user.email,password ='testpassword')
        
        response = self.client.get(notification,data={
            'id': self.notification.id,
            'goto': ''
            }
            )
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('notification/notification.html')
    
    def test_notification_views_with_GET_method_and_other_data(self):
        notification = reverse('notification:notification')
        
        self.client.login(email=self.just_user.email,password ='testpassword')
        
        response = self.client.get(notification,data={
            'pk': self.notification.pk,
            'goto': 'job/this/job/'
            }
            )
        
        self.assertEqual(response.status_code,302)
        self.assertTemplateUsed('notification/notification.html')
        
        
        

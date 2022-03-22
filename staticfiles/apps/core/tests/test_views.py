from django.test import TestCase, Client 
from django.urls import reverse

from apps.users.models import CustomUser 


class TestCoreViews(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.employer_user = CustomUser.objects.create_user(
            first_name = 'admin',
            email = 'admin@mail.com',
            password ='testpassword',
        )
        self.login = self.client.login(email=self.employer_user.email,password =self.employer_user.password)
        
        self.employer_user.profile.is_employer = True
        
        
        self.just_user = CustomUser.objects.create_user( 
            first_name = 'justuser',
            email='mine@mail.com',
            password ='testpassword'                                
        )
        
        self.jobseeker_user = CustomUser.objects.create_user(
            first_name = 'jobseeker',
            email = 'jobseeker@mail.com',
            password ='testpassword',
        )
        
    def test_landing_views_with_get(self):
        landing = reverse('core:landing')
        
        response = self.client.get(landing)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('core/landing.html')
        
    def test_signup_views_with_GET(self):
        signup = reverse('core:signup')
        
        response = self.client.get(signup)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('core/signup.html')
        
    def test_signup_views_with_POST(self):
        signup = reverse('core:signup')
        
        response = self.client.post(signup,data={
            'email': 'testuser@mail.com',
            'first_name': 'test',
            'password': 'testuserpassword',
            'user_type': 'jobseeker'
        })
        
        user = CustomUser.objects.get(email='testuser@mail.com')
        
        self.assertEqual(response.status_code,302)
        self.assertTrue(user.is_authenticated)
        self.assertFalse(user.profile.is_employer)
        
    def test_login_views_with_get(self):
        login = reverse('core:login')
        
        response = self.client.get(login)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('core/login.html')
        
    def test_login_views_with_POST(self):
        login = reverse('core:login') 
        
        response = self.client.post(login,data={
            'email': self.just_user.email,
            'password': 'testpassword'
        })
        
        self.assertEqual(response.status_code,302)
    
    def test_login_views_with_POST_using_username_instead_of_email(self):
        login = reverse('core:login')
        
        response = self.client.post(login,data={
            'first_name': self.just_user.first_name,
            'password': 'testpassword'
        })
        
        self.assertEqual(response.status_code,200) #no redirect and error is thrown 
        
    def test_logout_views_with_GET(self):
        logout = reverse('core:logout')
        
        self.client.login(email=self.just_user.email,password ='testpassword')
        response = self.client.get(logout)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('core/logout.html')
        
    def test_logout_views_with_POST(self):
        logout = reverse('core:logout')
        
        self.client.login(email=self.just_user.email,password ='testpassword')
        response = self.client.post(logout)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('core/logout.html')
        
    
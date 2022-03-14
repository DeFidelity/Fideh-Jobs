from django.test import SimpleTestCase 
from django.urls import reverse, resolve
from apps.core.views import LandingView, LoginView, SignUp,LogoutView


class TestUrls(SimpleTestCase):
    def test_landing_url(self):
        landing = reverse('core:landing')
        
        response = resolve(landing)
        
        self.assertEqual(response.func.view_class,LandingView)
        self.assertTemplateUsed('core/landing.html')
        
    def test_signup_url(self):
        signup = reverse('core:signup')
        
        response = resolve(signup)
        
        self.assertEqual(response.func.view_class,SignUp)
        self.assertTemplateUsed('core/signup.html')
        
    def test_login_urls(self):
        
        login = reverse('core:login')
        
        response = resolve(login)
        
        self.assertEqual(response.func.view_class,LoginView)
        self.assertTemplateUsed('core/login.html')
        
    def test_logout_urls(self):
        
        logout = reverse('core:logout')
        
        response = resolve(logout)
        
        self.assertEqual(response.func.view_class,LogoutView)
        self.assertTemplateUsed('core/logout.html')
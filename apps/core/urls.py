from django.urls import path
from .views import LandingView, LoginView, SignUp,LogoutView,ContactView

app_name = 'core'
urlpatterns = [
    path('',LandingView.as_view(), name='landing'),
    path('login/',LoginView.as_view(),name='login'),
    path('sign-up/',SignUp.as_view(),name='signup'),
    path('log-out/',LogoutView.as_view(),name='logout'),
    path('contact/',ContactView.as_view(),name='contact')
]
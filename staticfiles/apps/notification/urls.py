from django.urls import path
from .views import NotificationListView

app_name = 'notification'
urlpatterns = [
    path('',NotificationListView.as_view(),name='notification')
]
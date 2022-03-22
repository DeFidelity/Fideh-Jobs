from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    path('admin/for-management/of/this/domain/', admin.site.urls,name="management"),
    path('', include('apps.core.urls')),
    path('job/',include('apps.job.urls')),
    path('user/', include('apps.users.urls')),
    path('notification',include('apps.notification.urls')),
    path('accounts/password_reset/',views.PasswordResetView.as_view(template_name="password/password_reset.html"),name='password_reset'),
    path('user/password/reset/done/',views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"),name='password_reset_done'),
    path('user/<uidb64>/password/<token>/confirm/',views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"),name='password_reset_confirm'),
    path('user/password/reset/success/',views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"),name='password_reset_complete'),

    
]

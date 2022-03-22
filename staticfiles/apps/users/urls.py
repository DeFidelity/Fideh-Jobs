from django.urls import path
from .views import Dashboard, EmployerJobDetail, ApplicantJobDetail,ProfileView,ProfileEditView

app_name = 'users'
urlpatterns =[
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('dashboard/applicant/application<int:pk>/',ApplicantJobDetail.as_view(),name='applicant-detail'),
    path('dashboard/employer/job<int:pk>/',EmployerJobDetail.as_view(),name="employer-detail"),
    path('u/<str:email>/',ProfileView.as_view(),name='profile'),
    path('u/<str:email>/edit/',ProfileEditView.as_view(),name='profile-edit'),
]
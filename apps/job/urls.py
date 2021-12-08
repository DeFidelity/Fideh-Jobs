from django.urls import path 
from .views import JobList, JobDetail,JobCreate,JobApplication,JobEdit,JobDelete,ApplicationDelete,JobSearch

app_name = 'job'
urlpatterns =[
    path('fideht/job<int:pk>/',JobDetail.as_view(),name='job-detail'),
    path('fideht/jobs/',JobList.as_view(),name='job-list'),
    path('fideht/job/create/',JobCreate.as_view(),name='create-job'),
    path('fideht/job/edit/<int:pk>/',JobEdit.as_view(),name='edit-job'),
    path('fideh/jobs/delete/<int:pk>/',JobDelete.as_view(),name='delete-job'),
    path('fideht/jobs/job<int:pk>/apply/',JobApplication.as_view(),name='job-apply'),
    path('fideht/job/application/<int:pk>/delete/',ApplicationDelete.as_view(),name='application-delete'),
    path('fideht/jobs/search/',JobSearch.as_view(),name='job-search'),
]
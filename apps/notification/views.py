from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Notification


class NotificationListView(View, LoginRequiredMixin):
    def get(self,request):
        goto = request.GET.get('goto','')
        pk = request.GET.get('pk','')
        extra_pk = request.GET.get('extra_pk','')
        
        if goto != '':
            notification = Notification.objects.get(pk=pk)     
            notification.is_read = True
            notification.save()
            
            return redirect('users:applicant-detail',pk=notification.extra_pk)
        
        return render(request,'notification/notification.html')

from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.base import RedirectView
from apps.job.models import Job, Application
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Conversation, UserProfile
from .forms import ProfileForm
from apps.notification.utilities import create_notification

class Dashboard(View,LoginRequiredMixin):
    def get(self,request):
        
        user = request.user
        application = Application.objects.filter(created_by=user)
        your_jobs = Job.objects.filter(created_by=user).order_by('-created_on')
        applied_jobs = Job.objects.filter(application__created_by=user)
        
        context ={
            'your_jobs': your_jobs,
            'user':request.user.profile,
            'applied_jobs': applied_jobs
        }
        return render(request,'user/dashboard.html', context)

class EmployerJobDetail(View, LoginRequiredMixin):
    def get(self,request,pk,*args,**kwargs):
        job = get_object_or_404(Job,pk=pk,created_by=request.user)
        
        return render(request,'user/get-job-detail.html',{'job':job})
    
    
class ApplicantJobDetail(View,LoginRequiredMixin):
    def get(self,request,pk,*args,**kwargs):
        if request.user.profile.is_employer:
            application = get_object_or_404(Application,pk=pk,job__created_by=request.user)
        else:
            application = get_object_or_404(Application,pk=pk,created_by=request.user)
        job = Job.objects.get(application=application)
        print(0)
        conversation_message = Conversation.objects.filter(application=application)
        
        context ={
            'job':job,
            'application':application,
            'messages':conversation_message
                  }
        return render(request,'user/get-application-detail.html',context)
    def post(self,request,pk,*args,**kwargs):
        if request.user.profile.is_employer:
            application = get_object_or_404(Application,pk=pk,job__created_by=request.user)
        else:
            application = get_object_or_404(Application,pk=pk,created_by=request.user)
        job = Job.objects.get(application=application)
        
        message = request.POST.get('message')
        if message:
            conversation_message = Conversation.objects.create(application=application,message=message,created_by=request.user)
            conversation_message.save()
            if conversation_message.created_by != application.created_by:
                notification_to = application.created_by
            else:
                notification_to = job.created_by
            create_notification(request, notification_to, 'message', application.pk)
        
        messages = Conversation.objects.filter(application=application)
            
        context ={
            'job':job,
            'application':application,
            'messages':messages
        }
        return render(request,'user/partials/message.html',context)
        
class ProfileView(View, LoginRequiredMixin):
    def get(self,request,email,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user__email=email)
        
        context ={
            'profile': profile,
        }
        return render(request,'user/profile.html',context)
    
class ProfileEditView(View):
    def get(self,request,email,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user__email=request.user)
        context = {
            'profile': profile
        }
        return render(request,'user/profile-edit.html',context)
        
    def post(self,request,email,*args,**kwargs):
        form = ProfileForm(request.POST)
        profile = get_object_or_404(UserProfile,user__email=request.user)
        if profile:
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.is_employer = request.user.profile.is_employer
                profile.save()
                
                return redirect('profile',request.user.email)
            return render(request,'user/profile.html',{'profile':profile})
        
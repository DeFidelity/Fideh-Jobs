from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View 
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Job, Application
from .forms import JobCreateForm, ApplicationForm
from apps.notification.utilities import create_notification

class JobDetail(View,LoginRequiredMixin):
    def get(self, request,pk,*args,**kwargs):
        job = Job.objects.get(pk=pk)
        context = {
            "job": job,
        }
        return render(request,'job/job_detail.html',context)
    
class JobSearch(View,LoginRequiredMixin):
    def get(self, request):
        jobs = Job.objects.all().order_by('-created_on')
        page = Paginator(jobs,5)
        page_number = request.GET.get('page')
        page_obj = page.get_page(page_number)
        return render(request,'job/search.html',{'jobs':jobs,'page_obj':page_obj})
    
    def post(self,request):
        query = request.POST.get('query')
        remote = request.POST.get('remote')
        
        matching_jobs = Job.objects.filter(Q(title__icontains=query)| Q(description__icontains=query)|
                                           Q(detail__icontains=query)|Q(experience__icontains=query))
        remote_jobs = None
        if remote:
            remote_jobs = Job.objects.filter(remote=True and Q(title__icontains=query) | Q(description__icontains=query))
        context= {
            'jobs': matching_jobs,
            'remote': remote_jobs
        }
        return render(request,'job/partials/searchresult.html',context)
            

class JobList(View, LoginRequiredMixin):
    def get(self, request):
        jobs = Job.objects.all()
        
        context = {
            "jobs": jobs,
        }
        
        return render(request,'job/job-list.html',context)
    
class JobCreate(View, LoginRequiredMixin, UserPassesTestMixin):
    def get(self,request):
        return render(request,'job/create-job.html')
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = JobCreateForm(request.POST)
        remote = request.POST.get('remote_option')
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = user 
            if remote == 'remote':
                job.remote = True
            job.save()
            
            context= {
                'form':form
            }
            return HttpResponse('<p class="text-sm text-green-600 text-center">Succesfully added another job to your listing.</p>')
        else:
            return HttpResponse('<p class="text-sm text-red-600 text-center">*There is an error</p>')
        
class JobEdit(View,LoginRequiredMixin,UserPassesTestMixin):
    def get(self,request,pk):
        job = Job.objects.get(pk=pk)
        return render(request,'job/edit-job.html',{'job':job})
    
    def post(self,request,pk,*args,**kwargs):
        job = Job.objects.get(pk=pk)
        form = JobCreateForm(request.POST)
        remote = request.POST.get('remote_option')
        if form.is_valid():
            jobu = form.save(commit=False)
            if remote == 'remote':
                jobu.remote = True
            jobu.created_by = request.user
            jobu.save()
            
            return redirect('job:job-detail',pk=job.pk)
        
class JobDelete(View,LoginRequiredMixin,UserPassesTestMixin):
    def get(self,request,pk,*args,**kwargs):
        job = Job.objects.get(pk=pk)
        return render(request,'job/delete-job.html',{'job':job})
    def post(self,request,pk,*args,**kwargs):
        job = Job.objects.get(pk=pk)
        job.delete()
        return redirect('users:dashboard')
    
        
    def test_func(self, request,pk):
        job = Job.objects.get(pk=pk)
        return request.user == job.created_by
        
class JobApplication(View,LoginRequiredMixin,UserPassesTestMixin):
    def get(self, request,pk,*args, **kwargs):
        job = Job.objects.get(pk=pk)
        context= {
                'job':job,
            }
        return render(request,'job/job-apply.html',context)
    
    def post(self,request,pk,*args,**kwargs):
        job = Job.objects.get(pk=pk)
        form = ApplicationForm(request.POST)
        
        if request.user.profile.is_employer:
            return HttpResponse('<p class="text-sm text-red-600 text-center">An employer can not apply for jobs, sorry for any inconvenience caused.</p>')
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user 
            application.save()
            
            create_notification(request, job.created_by, 'application', application.pk)
            
            return HttpResponse('<p class="text-sm text-green-600 text-center">*Application succesfully sent, creator would recieve notification.</p>')
            
        else:
            context= {
                'job':job,
                'form':form
            }
            return render(request,'job/job-apply.html',context)
    def test_func(self,request):
        if request.user.profile.is_employer:
            return False
        return True
    
class ApplicationDelete(View,LoginRequiredMixin):
    def get(self,request,pk):
        application = get_object_or_404(Application,pk=pk,created_by=request.user)
        return render(request,'job/application-delete.html',{'application', application})
    
    def post(self,request,pk,*args,**kwargs):
        application = get_object_or_404(Application,pk=pk,created_by=request.user)
        application.delete()
        return redirect('users:dashboard')

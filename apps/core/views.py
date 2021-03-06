from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.users.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .forms import UserForm, LoginForm, ContactForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from apps.job.models import Job


class LandingView(View):
    def get(self, request):
        jobs = Job.objects.all().order_by('-change_at')[0:3]
        return render(request,'core/landing.html',{'jobs': jobs})


class SignUp(UserPassesTestMixin,View):
    def get(self,request):
        return render(request,'core/signup.html')
    
    def post(self,request,*args, **kwargs):
        form = UserForm(request.POST)
        account_type = request.POST.get('user_type', 'jobseeker')
     
        if form.is_valid():
            email = request.POST.get('email')
            exists = CustomUser.objects.filter(email=email)
            if exists:
                messages.error(request,'We found an account for this email')
                # raise FormValidationError('we found an accout for this email')
            email = email
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            user = CustomUser.objects.create_user(first_name=first_name, email=email, password=password)
            if account_type == 'employer':
                user.profile.is_employer = True
            user.save()
            login(request, user)
            return redirect('users:dashboard')
        else:
            messages.error(request,'Please fill all the forms correctly')
            return redirect('signup')
    def test_func(self):
        return not self.request.user.is_authenticated
    
class LoginView(UserPassesTestMixin,View):
    def get(self, request):
        return render(request,'core/login.html')
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            auth = authenticate(email=email,password=password)
        
            if auth is not None:
                login(request, auth)
             
                return redirect('users:dashboard')
            
            else:
                messages.error(request,'Username or password not correct')
        
                return render(request,'core/login.html',{'form':form})
                
        else:
            messages.error(request,'Username or password not correct')
            return render(request,'core/login.html',{'form':form}) 
        
    def test_func(self):
        return not self.request.user.is_authenticated
        
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,'core/logout.html')
    
    def post(self,request):
        logout(request)
        return redirect('core:landing')
    
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request,*args, **kwargs):
        message = request.POST.get('message')
        form = ContactForm(request.POST)
        if len(message.split()) < 10:
            return HttpResponse('<p class="text-sm text-red-500 text-center">Form error,please write a descriptive message</p>')
            
        if form.is_valid():
            form.save()
            return HttpResponse('<p class="text-sm text-green-500 text-center">Thank you for reaching out to us, we will get back to you later</p>')
        else:
            return HttpResponse('<p class="text-sm text-red-500 text-center">Form error, please enter a valid email and descriptive message</p>')
            
            
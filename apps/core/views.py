from django.shortcuts import redirect, render
from apps.users.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .forms import UserForm, LoginForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from apps.job.models import Job


class LandingView(View):
    def get(self, request):
        jobs = Job.objects.all().order_by('-change_at')[0:3]
        return render(request,'core/landing.html',{'jobs': jobs})


class SignUp(View,UserPassesTestMixin):
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
            return redirect('dashboard')
        else:
            messages.error(request,'Please fill all the forms correctly')
            return redirect('signup')
    def test_func(self):
        return not self.request.user.is_authenticated
    
class LoginView(View, UserPassesTestMixin):
    def get(self, request):
        return render(request,'core/login.html')
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            auth = authenticate(email=email,password=password)
            print(24)
            if auth is not None:
                login(request, auth)
                print(34)
                return redirect('users:dashboard')
            
            else:
                messages.error(request,'Username or password not correct')
                print(3)
                return render(request,'core/login.html',{'form':form})
                
        else:
            messages.error(request,'Username or password not correct')
            return render(request,'core/login.html',{'form':form}) 
            print(4)
        
    def test_func(self):
        return not self.request.user.is_authenticated
        
class LogoutView(View):
    def get(self, request):
        return render(request,'core/logout.html')
    
    def post(self, request):
        logout(request)
        return render(request,'core/logout-success.html')
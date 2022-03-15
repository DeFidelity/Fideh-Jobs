from django.test import TestCase, Client 
from django.urls import reverse
from apps.users.models import UserProfile, Conversation, CustomUser
from apps.job.models import Job, Application


class TestUsersViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.employer_user = CustomUser.objects.create_user(
            first_name = 'admin',
            email = 'admin@mail.com',
            password ='testpassword',
        )
        self.employer_user.profile.is_employer = True
        
        self.jobseeker_user = CustomUser.objects.create_user(
            first_name = 'jobseeker',
            email = 'jobseeker@mail.com',
            password ='testpassword',
        )
        self.employer_user.profile.is_employer = False
        
        self.profile = self.employer_user.profile
        
        self.job = Job.objects.create(
            title = 'Software Engineer',
            description = "You will be required to create, improve and accomplish softwares",
            created_by_id = self.employer_user.pk
        ) 
        
        self.application = Application.objects.create(
            job = self.job,
            proposal = 'Software engineering to me is not just a skill, it is something I enjoy and always look forward to, I am infact the most perfect person for this position',
            created_by_id = self.jobseeker_user.id
        )
        
        self.conversatin = Conversation.objects.create(
            application = self.application,
            message = "Hey, congratulations, you're hired",
            created_by_id = self.employer_user.id
        )
      
        
    def test_dashboard_view_with_get_method(self):
        dashboard_url = reverse('users:dashboard')
        
        self.client.login(email='admin@mail.com',password='testpassword')
        jobs = Job.objects.filter(created_by_id=self.employer_user.id)
        response = self.client.get(dashboard_url)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('user/dashboard.html')
        # self.assertIsInstance(response.context['your_jobs'],jobs)
        
    def test_employer_job_detail_with_get_method(self):
        
        dashboard_url = reverse('users:employer-detail',args=[self.job.pk])
        
        self.client.login(email=self.employer_user.email,password ='testpassword')
        response = self.client.post(dashboard_url)
        
        self.assertEquals(response.status_code,405)
        self.assertTemplateUsed('user/get-job-detail.html')
        
    def test_employer_job_detail_for_non_employer_user_with_get_method(self):
        dashboard_url = reverse('users:employer-detail',args=[self.job.pk])
        
        self.client.login(username='jobseeker',password ='testpassword')
        response = self.client.post(dashboard_url)
        
        self.assertEquals(response.status_code,405)
        self.assertTemplateUsed('user/get-job-detail.html')
        
    def test_applicant_job_detail_with_GET_method(self):
        app_url = reverse('users:applicant-detail',args=[self.job.pk])
        
        self.client.login()
        
        
        
        
            
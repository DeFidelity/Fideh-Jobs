from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.job.models import Application, Job
from apps.job.views import JobCreate

from apps.users.models import Conversation, CustomUser

class TestJobViews(TestCase):
    def setUp(self):
        
        self.client = Client()
        
        self.employer_user = CustomUser.objects.create_user(
            first_name = 'admin',
            email = 'admin@mail.com',
            password ='testpassword',
        )
        self.login = self.client.login(email=self.employer_user.email,password =self.employer_user.password)
        
        self.employer_user.profile.is_employer = True
        
        
        self.just_user = CustomUser.objects.create_user( 
            first_name = 'justuser',
            email='mine@mail.com',
            password ='testpassword'                                
        )
        
        self.jobseeker_user = CustomUser.objects.create_user(
            first_name = 'jobseeker',
            email = 'jobseeker@mail.com',
            password ='testpassword',
        )
        
        self.client.login(email=self.jobseeker_user.email,password =self.jobseeker_user.password)
        
        self.employer_user.profile.is_employer = False
        
        
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
      
    def test_detail_views_with_get_method(self):
        
        job_detail = reverse('job:job-detail', args=[self.job.pk])
        
        self.client.login(email=self.employer_user.email,password ='testpassword')
        
        response = self.client.get(job_detail)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('job/job-detail.html')
        self.assertTrue(response.context['job'])
        
    def test_detail_views_with_POST_method(self):
        
        job_detail = reverse('job:job-detail', args=[self.job.pk])
        
        self.client.login(email=self.employer_user.email,password ='testpassword')
        
        response = self.client.post(job_detail)
        
        self.assertEqual(response.status_code,405)
        
    def test_job_search_views_with_get_method(self):
        job_search = reverse('job:search')
        
        self.client.login(email=self.jobseeker_user.email,password ='testpassword')
        
        response = self.client.get(job_search)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('job/search.html')
        
    def test_job_search_views_with_POST_method(self):
        
        job_search = reverse('job:search')
        
        self.client.login(email=self.jobseeker_user.email,password ='testpassword')
        
        response = self.client.post(job_search,data={
            'query':'backend/fullstack software engineer (python,django)',
            'remote': 'true'
        })
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('job/partials/searchresult.html')
        self.assertTrue(response.context['jobs'].count,0)
        
    def test_job_list_views_with_get_method(self):
        job_list = reverse('job:job-list')
        
        self.client.login(email=self.jobseeker_user.email,password ='testpassword')
        
        response = self.client.get(job_list)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('job/job-list.html')
        self.assertTrue(response.context['jobs'])
        
    def test_job_create_view_with_non_employer_user_and_get_method(self):
        
        job_create = reverse('job:create-job')
        
        self.client.login(email=self.jobseeker_user.email,password ='testpassword')
        
        response = self.client.get(job_create,data={
            'request':self.client
        })
        
        self.assertEqual(response.status_code,403)
        
    def test_job_create_view_with_employer_user_and_get_method(self):
        
        job_create = reverse('job:create-job')
        
        employer_user = CustomUser.objects.create_user(
                first_name = 'admin',
                email = 'employer@mail.com',
                password ='testpassword',
            )
        employer_user.profile.is_employer = True
       
        self.client.login(email=employer_user.email,password='testpassword')
        
        
        
        response = self.client.get(job_create)
        resolv = resolve(job_create)
        
        self.assertEqual(resolv.func.view_class,JobCreate)
        self.assertTemplateUsed('job/create-job.html')
        self.assertEqual(response.status_code,200)
        
        
        
    def test_job_create_view_with_employer_user_and_POST_method(self):
        
        login = self.client.login(email=self.employer_user.email,password='testpassword')
        emp = self.employer_user.profile.is_employer = True
        job_create = reverse('job:create-job')
        response = self.client.post(job_create,data={
            'title': 'SEO specailist',
            'description': 'You will be required to optimize page ranking',
            'created_by_id': self.employer_user.pk
        })
        print(emp)
        print(response)
        self.assertTrue(login)
        self.assertEqual(response.status_code,200)
    
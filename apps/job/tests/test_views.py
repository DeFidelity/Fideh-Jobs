from django.test import TestCase, Client
from django.urls import reverse
from apps.job.models import Application, Job

from apps.users.models import Conversation, CustomUser

class TestJobViews(TestCase):
    def setUp(self):
        
        self.client = Client()
        
        self.employer_user = CustomUser.objects.create_user(
            first_name = 'admin',
            email = 'admin@mail.com',
            password ='testpassword',
        )
        
        self.just_user = CustomUser.objects.create_user( 
            first_name = 'justuser',
            email='mine@mail.com',
            password ='testpassword'                                
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
        
        
    
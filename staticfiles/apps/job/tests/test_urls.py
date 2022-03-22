from django.test import SimpleTestCase 
from django.urls import reverse, resolve 
from apps.job.views import JobList, JobDetail,JobCreate,JobApplication,JobEdit,JobDelete,ApplicationDelete,JobSearch


class TestJObUrls(SimpleTestCase):
    
    def test_job_detail_urls(self):
         job_detail = reverse('job:job-detail',args=['2'])
         
         response = resolve(job_detail)
         
         self.assertEqual(response.func.view_class,JobDetail)
         self.assertTemplateUsed('job/job_detail.html')
         
    def test_job_list_urls(self):
        job_list = reverse('job:job-list')
        
        response = resolve(job_list)
        
        self.assertEqual(response.func.view_class,JobList)
        self.assertTemplateUsed('job/job-list.html')
        
    def test_job_create_url(self):
        job_create = reverse('job:create-job')
        
        response = resolve(job_create)
        
        self.assertEqual(response.func.view_class,JobCreate)
        self.assertTemplateUsed('job/create-job.html')
        
    def test_job_edit_url(self):
        job_edit = reverse('job:edit-job',args=['2'])
        
        response = resolve(job_edit)
        
        self.assertEqual(response.func.view_class,JobEdit)
        self.assertTemplateUsed('job/edit-job.html')
        
    def test_job_delete_url(self):
        job_delete = reverse('job:delete-job',args = ['3'])
        
        response = resolve(job_delete)
        
        self.assertEqual(response.func.view_class,JobDelete)
        self.assertTemplateUsed('job/delete-job.html')
        
    def test_job_apply_url(self):
        job_apply = reverse('job:job-apply', args=['2'])
        
        response = resolve(job_apply)
        
        self.assertEqual(response.func.view_class,JobApplication)
        self.assertTemplateUsed('job/job-apply.html')
        
    def test_job_application_delete_url(self):
        job_apply_del = reverse('job:application-delete',args=['2'])
        
        response = resolve(job_apply_del)
        
        self.assertEqual(response.func.view_class,ApplicationDelete)
        self.assertTemplateUsed('job/application-delete.html')
        
    def test_job_search_urls(self):
        job_search = reverse('job:search')
        
        response = resolve(job_search)
        
        self.assertEqual(response.func.view_class,JobSearch)
        self.assertTemplateUsed('job/search.html')
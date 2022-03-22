from urllib import response
from django.test import SimpleTestCase 
from django.urls import reverse, resolve
from apps.users.views import Dashboard, EmployerJobDetail, ApplicantJobDetail,ProfileView,ProfileEditView


class TestUsersUrls(SimpleTestCase):
    
    def test_user_dashboard_url(self):
        dashboard = reverse('users:dashboard')
        
        response = resolve(dashboard)
        
        self.assertEqual(response.func.view_class,Dashboard)
        self.assertTemplateUsed('users/dashboard.html')
        
    def test_user_dashboard_applicant_application_detail_url(self):
        applicant = reverse('users:applicant-detail',args=['2'])
        
        response = resolve(applicant)
        
        self.assertEqual(response.func.view_class,ApplicantJobDetail)
        self.assertTemplateUsed('users/get-application-detail.html')
        
    def test_user_dashboard_employer_application_detail_url(self):
        employer = reverse('users:employer-detail',args=['2'])
        
        response = resolve(employer)
        
        self.assertEqual(response.func.view_class,EmployerJobDetail)
        self.assertTemplateUsed('users/get-job-detail.html')
        
    def test_profile_detail_url(self):
        profile = reverse('users:profile',args=['mama@papa.com'])
        
        response = resolve(profile)
        
        self.assertEqual(response.func.view_class,ProfileView)
        self.assertTemplateUsed('user/profile.html')
        
    def test_profile_edit_url(self):
        employer = reverse('users:profile-edit',args=['@mine@yours.com'])
        
        response = resolve(employer)
        
        self.assertEqual(response.func.view_class,ProfileEditView)
        self.assertTemplateUsed('user/profile-edit.html')
        
        
        
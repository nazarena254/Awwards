from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user=User(username='alvynah')
        self.user.save()
        self.profile=Profile(user=self.user,name='vee',bio='vee in the house',prof_pic='default.png',location='kenya',account_url='www.alvynah.com')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
         self.assertTrue(isinstance(self.profile, Profile))

    def test_saveProfile(self):
        self.profile.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)
    def test_delete_method(self):


        self.user.delete()
        profile = User.objects.all()
        self.assertTrue(len(profile) == 0)
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user=User(username='alvynah')
        self.user.save()
        self.project=Project(title='Test title',description='test description', project_image='test.png', project_url='project.com',technologies="php",user=self.user)
    def tearDown(self):
        Project.objects.all().delete()
        User.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    def test_save_Project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

class RateTest(TestCase):
    def setUp(self):
        self.user=User(username='alvynah')
        self.user.save()
        self.project=Project(title='Test title',description='test description', project_image='test.png', project_url='project.com',technologies="php",user=self.user)
        self.project.save()
        self.rate=Rate(design='9',usability='10',content='9',user=self.user,project=self.project)
        self.rate.save_rating() 
    def tearDown(self):
        Rate.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rate)) 
    def test_save_rates(self):
        self.rate.save_rating()
        rates=Rate.objects.all()
        self.assertTrue(len(rates)==1)
    def test_delete_rates(self):
        self.rate.save_rating()
        self.rate.delete_rating()
        rates = Rate.objects.all()
        self.assertTrue(len(rates)==0)




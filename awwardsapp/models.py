from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    prof_pic=models.ImageField(upload_to='pictures/',default='default.png')
    name=models.CharField(max_length=50)
    bio=models.TextField()
    location=models.CharField(max_length=100)
    account_url=models.URLField()

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()
    def __str__(self):
        return f'{self.user.username} Profile'

class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    project_image=models.ImageField(upload_to='projects/')
    project_url=models.URLField()
    pub_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    technologies = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls,search_term):
        projects= cls.objects.filter(title__icontains=search_term).all()
        return projects

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_project_by_id(cls,id):
        project=Project.objects.filter(id=id)
        return project

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ["-pk"]


    

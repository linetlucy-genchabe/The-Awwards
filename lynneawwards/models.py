from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
from django.http import Http404
from django.db.models import ObjectDoesNotExist

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pics",blank=True)
    bio = models.TextField(blank=True)
    
    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
            

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

        
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'images/', default='images/default.jpg')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='KE')

        
    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_author(cls, Author):
        projects = cls.objects.filter(Author=Author)
        return projects
    
    
    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.project_title
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Project'
        verbose_name_plural = 'Projects'
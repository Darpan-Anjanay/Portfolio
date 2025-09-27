from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/')
    working_as = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    contact_number = models.CharField(max_length=15)
    bio = RichTextField()
    skills_Overview = RichTextField()
    resume = models.FileField(upload_to='resumes')

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    platform_name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return f'{self.platform_name} ({self.profile.user.username})'


class TechCategory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='techcategory_set')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Technology(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='technology_set')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(TechCategory, on_delete=models.CASCADE)
    description = RichTextField()

    def __str__(self):
        return f'{self.name} - {self.category.name}'


class WorkHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='workhistory_set')
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    present = models.BooleanField(default=False)
    sortorder = models.IntegerField(default=999)    

    
    def __str__(self):
        return self.company_name



class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='project_set')
    name = models.CharField(max_length=100)
    techs = models.ManyToManyField(Technology)
    github_link = models.URLField(blank=True, null=True)
    description = RichTextField()
    sortorder = models.IntegerField(default=999)    
    def __str__(self):
        return self.name



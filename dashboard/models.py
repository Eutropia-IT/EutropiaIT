from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 

class Technology(models.Model):
    technology_name = models.CharField(max_length=50)
    technology_avater = models.ImageField(null=True, upload_to='Technology_Avater')

    def __str__(self):
        return self.technology_name if self.technology_name else ''

class Client(models.Model):
    client = models.ForeignKey(User,related_name='client', null=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_url = models.URLField()
    company_logo = models.ImageField(null=True, upload_to='Client/Company_Logo')
    avater = models.ImageField(null=True,  upload_to='Client/Avater')

    def __str__(self):
        return self.company_name if self.company_name else ''


class Project(models.Model):
    client_name = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    video_demo = models.URLField()
    site_url = models.URLField()
    cover = models.ImageField(null=True, upload_to='Project/Cover')
    full_capture = models.ImageField(null=True, upload_to='Project/Capture')
    technology = models.ManyToManyField(Technology, null=True)
    description =  RichTextUploadingField(null=True)

    def __str__(self):
        return self.title if self.title else ''


class Employee(models.Model):
    employee = models.OneToOneField(User,related_name='employee', null=True, on_delete=models.SET_NULL)
    is_display = models.BooleanField(default=False)
    designation = models.CharField(max_length=50)
    fb = models.URLField(null=True)
    twiter = models.URLField(null=True)
    git = models.URLField(null=True)
    lindin = models.URLField(null=True)
    avater = models.ImageField(null=True,  upload_to='Employee/Avater')

class Review(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    review = models.TextField(null=True)
    reating = models.CharField(null=True, max_length=5)


class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    cover_image = models.ImageField(null=True, upload_to='Blog/Cover')
    publish_time = models.DateTimeField(auto_now_add=True)
    content =  RichTextUploadingField()

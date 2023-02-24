from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
import uuid

class Task(models.Model):
    STATUS = (
        ('In Progress'),
        ('Complete'),
        ('Delete'),
        ('Not Interested'),
    )
    
    user = models.ForeignKey(User ,on_delete=models.CASCADE, null=True, blank=True , default=User)
    task_name = models.CharField(max_length= 300) 
    status = models.CharField(max_length=60, default='In Progress',)
    discription = models.TextField(max_length=400 , null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True,blank=True)
    slug = AutoSlugField(populate_from='task_name')
    deadline = models.DateField()

    def __str__(self) -> str:
        return f"{self.task_name}" 
        

        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task_name)
            
        return super().save(*args, **kwargs)    

    
    class Meta:
        # order_with_respect_to = 'user'
        ordering = ['-deadline']



class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True , verbose_name="user" , related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=40,blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_picture', default='media/uploads/profile_picture/default.jpg', blank=True)


    @property
    def imageURL(self):
        if self.picture:
            return self.picture.url 
        else:
            return 'media/uploads/profile_pictures/default.png'

    def __str__(self) -> str:
        return f"{self.user.username}"        


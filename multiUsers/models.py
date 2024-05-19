from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=100,unique=True,default="company_user")

class CustomUser(User):
    roles = models.ManyToManyField(Role)
    
class Status(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    name = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Image(models.Model):
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='images/',default='/static/images/profile.png',null=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.description

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Petition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    signature_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    signed_users = models.ManyToManyField(User, related_name='signed_petitions', blank=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['updated_at'] 

class ContactUS(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


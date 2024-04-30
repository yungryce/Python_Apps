from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Reg(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('details', args=(str(self.id)))
        return reverse('home')
        
    # def snippet(self):
    #     return self.body[:100]
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
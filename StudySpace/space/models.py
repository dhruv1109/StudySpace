from django.db import models

# Create your models here.

class Subject(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    logo=models.TextField()
    def __str__(self):
        return self.title
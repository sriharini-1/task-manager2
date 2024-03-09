

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   description = models.TextField()
   category = models.CharField(max_length=100, blank=True, null=True)
   due_date = models.DateField(blank=True, null=True)
   priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
   completed = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return self.title
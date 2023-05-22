from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now=True)
    condition = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.name} / {self.description} 1/ {self.condition}'



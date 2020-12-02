from django.db import models

# Create your models here.

class MessSec(models.Model):
    username = models.CharField(max_length=100)
    hostel = models.CharField(max_length=100)

    def __str__(self):
        return self.username
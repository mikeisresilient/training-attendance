from django.db import models

# Create your models here.

class Participant(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

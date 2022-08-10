from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name

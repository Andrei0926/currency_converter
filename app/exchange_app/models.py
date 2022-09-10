from django.db import models

class Journal(models.Model):
    number = models.TextField()
    data = models.DateTimeField(auto_now=True)
    pair = models.TextField()

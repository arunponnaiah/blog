from django.db import models

class Journal(models.Model):
     title = models.CharField(max_length=30,primary_key=True)
     content = models.TextField(blank=True)

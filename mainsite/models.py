from django.db import models

# Create your models here.


class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	created = models.DateField()
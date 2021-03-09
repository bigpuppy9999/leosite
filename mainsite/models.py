from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Project(models.Model):
	title = models.CharField(max_length=50)
	description = MarkdownxField()
	created = models.DateField()
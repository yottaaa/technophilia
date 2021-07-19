from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	caption = models.TextField(null=True,blank=True)
	content = QuillField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


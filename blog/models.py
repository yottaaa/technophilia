from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	img_url = models.TextField(default="https://images.unsplash.com/photo-1432821596592-e2c18b78144f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80")
	caption = models.TextField(null=True,blank=True)
	content = RichTextUploadingField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


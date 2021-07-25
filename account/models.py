from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pic = ResizedImageField(size=[300, 300], quality=75, upload_to='profile_pics', default='profile_pics/default_avatar.jpg', force_format='JPEG')

	def __str__(self):
		return "{} profile".format(self.user.username)
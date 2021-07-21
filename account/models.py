from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pic = models.ImageField(default='profile_pics/default_avatar.jpg', upload_to='profile_pics')

	def __str__(self):
		return "{} profile".format(self.user.username)
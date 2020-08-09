from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Demo(models.Model):
	title = models.CharField(max_length=100)
	booked = models.ManyToManyField(User, related_name='booked', blank=True)

	def __str__(self):
		return self.title
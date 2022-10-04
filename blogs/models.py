from django.db import models
from django.contrib.auth.models import User  

# Create your models here.


class BlogPost(models.Model):
	"""The blog the user want to add"""
	title= models.CharField(max_length = 300)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add= True)
	owner = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		""" Return the string representation of the model"""
		return self.title

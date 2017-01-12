import random
import string
from django.db import models

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	print(random.choice(chars))
	return "".join(random.choice(chars) for _ in range(size))


class KirrURL(models.Model):
	url = models.CharField(max_length=120)
	shortcode = models.CharField(max_length=15, unique=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		print("something")
		self.shortcode = code_generator()
		return super().save(*args, **kwargs)

	def __str__(self):
		return str(self.url)
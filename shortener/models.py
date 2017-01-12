from django.conf import settings
from django.db import models

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
# SHORTCODE_MAX = settings.SHORTCODE_MAX
# Create your models here.

class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super().all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items = None):
		print(items)
		qs = KirrURL.objects.filter(id__gte=1)
		new_code = 0

		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
			print(items)

		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_code += 1
		return "New code made: {i}".format(i=new_code)

class KirrURL(models.Model):
	url = models.CharField(max_length=120)
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		return super().save(*args, **kwargs)

	# class Meta:
		# ordering = 'id'

	def __str__(self):
		return str(self.url)
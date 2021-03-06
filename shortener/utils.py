import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

# from shortener.models import KirrURL

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
	print(random.choice(chars))
	return "".join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	print(instance)
	print(instance.__class__)
	print(instance.__class__.__name__)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(instance, size=size)
	return new_code
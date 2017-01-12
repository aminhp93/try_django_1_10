from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.

def test_view(request):
	return HttpResponse("test")

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):

	# try:
	# 	obj = KirrURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj = KirrURL.objects.all().first()
	# return HttpResponse("hello {shortcode}".format(shortcode=obj.url))

	# ===================================================================

	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact = shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url
	# return HttpResponse("hello {shortcode}".format(shortcode=obj_url))

	# ===================================================================

	obj = get_object_or_404(KirrURL, shortcode=shortcode)

	# return HttpResponse("hello {shortcode}".format(shortcode=obj.url))
	return HttpResponseRedirect(obj.url)

class KirrRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		# return HttpResponse("hello again {i}".format(i=shortcode))
		return HttpResponseRedirect(obj.url)

	def post(self, request, *args, **kwargs):
		return HttpResponse()
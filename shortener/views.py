from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
from .forms import SubmitUrlForm
# Create your views here.


# def home_view_fbv(request, *args, **kwargs):
# 	if request.method == "POST":
# 		print(request.POST)
# 	return render(request, "shortener/home.html", {})


class HomeView(View):
	def get(sef, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Kirr.co",
			"form": the_form,
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		print(request.POST)
		print(request.POST.get('url'), "22")
		form = SubmitUrlForm(request.POST)

		template = "shortener/home.html"

		context = {
			"title": "Kirr",
			"form": form,
		}

		if form.is_valid():
			
			new_url = form.cleaned_data.get('url')
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			new_context = {
				"object": obj,
				"created": created,
			}

			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"
		
		return render(request, template, context)

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
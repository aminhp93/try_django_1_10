from django import forms
from .validators import validate_url, validate_dot_com

# from django.core.exceptions import ValidationError
# from django.core.validators import URLValidator

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label = "Submit URL", 
						validators = [validate_url, validate_dot_com], 
						widget = forms.TextInput(
							attrs={
							"placeholder": "Long URL",
							"class": "form-control"
							}))
	# url = forms.CharField(label = "Submit URL")

	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	print(cleaned_data)
	# 	url = cleaned_data.get('url')

	# 	url_validator = URLValidator()
	# 	try:
	# 		print("valid")
	# 		url_validator(url)
	# 		print("valid2")
	# 	except:
	# 		raise forms.ValidationError("Invalid url for this field")
		
	# 	return url

	# def clean_url(self):
	# 	url = self.cleaned_data['url']
		# if not "com" in url:
			# raise forms.ValidationError("This is not valid. No .com")
	# 	url_validator = URLValidator()
	# 	try:
	# 		print("valid")
	# 		url_validator(url)
	# 		print("valid2")
	# 	except:
	# 		raise forms.ValidationError("Invalid url for this field")
		
	# 	return url

	# 
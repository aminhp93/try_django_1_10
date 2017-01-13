# from django.core.exceptions import ValidationError
# from django.core.validators import URLValidator


# def validate_url(value):
# 	print("1")
# 	url_validator = URLValidator()
# 	print("12")

# 	try:
# 		print("3")
# 		url_validator(value)
# 		print("4")
# 	except:
# 		print("5")
# 		raise ValidationError("Invalid URL")

# 	return value

# def validate_dot_com(value):
# 	if not "com" in value:
# 		raise ValidationError("This is worogn")
# 	return value

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(value)
    except:
        value_1_invalid = True
    value_2_url = "http://" + value
    try:
        url_validator(value_2_url)
    except:
        value_2_invalid = True
    if value_1_invalid == False and value_2_invalid == False:
        raise ValidationError("Invalid URL for this field")
    return value


def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid because of no .com")
    return value
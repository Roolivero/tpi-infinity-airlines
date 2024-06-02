import re
import pycountry
from django.core.exceptions import ValidationError

country_codes = {country.name: country.alpha_2 for country in pycountry.countries}

def validate_code(value):
    if not re.match(r'^[A-Z]{2}\d{4}$', value):
        raise ValidationError('Code must be in the format: two uppercase letters followed by four digits.')
    
    country_code = value[:2]
    if country_code not in country_codes:
        raise ValidationError(f'{country_code} is not a valid country code.')
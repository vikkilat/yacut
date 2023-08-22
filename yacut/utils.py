import random
import string

from .models import URLMap


def get_unique_short_id():
    letters_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_digits, 6))
    while URLMap.query.filter_by(short=rand_string).first():
        rand_string = ''.join(random.sample(letters_digits, 6))
    return rand_string


def check_unique_short_url(custom_id):
    if URLMap.query.filter_by(short=custom_id).first():
        return custom_id
    return None

from .base import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'www.mysite.com',
]

CORS_ALLOWED_ORIGINS = [
    'https://www.mysite.com',
]



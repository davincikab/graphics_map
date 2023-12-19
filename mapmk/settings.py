import os;
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-o!-n_t&5pyw8xh0p!qvuc%i3++=b5ek(q1*5r5!)uka&x#!9-n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    ##apps
    "gunicorn",
    "main.apps.MainConfig",
    ##3rd party
    "modeltranslation"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mapmk.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
       'DIRS': [os.path.join(BASE_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mapmk.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.contrib.gis.db.backends.postgis",
#         "NAME":"mapmk",
#         "USER":"postgres",
#         "PASSWORD":"postgres",
#         "HOST":"localhost",
#         "PORT":5432, 
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME":"mapmk",
        "USER":"root",
        "PASSWORD":"",
        "HOST":"localhost",
        # "PORT":3306, 
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGES = [
    ('ar', _('Arabic')),
    ('he', _('Hebrew')),
    ('en', _('English')),
]

LANGUAGE_CODE = "en"

# LOCALE_PATHS = (
#     '/var/www/djangoApp/Billing/object/locale',
# )
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


LOGIN_REDIRECT_URL = "/custommaps"
LOGOUT_REDIRECT_URL = "/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, '/main/static')
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# GEOS_LIBRARY_PATH =r"C:\Program Files\QGIS 3.30.0\bin\geos_c"
# GDAL_LIBRARY_PATH =r"C:\Program Files\QGIS 3.30.0\bin\gdal306"

# GEOS_LIBRARY_PATH =r"C:\Program Files\QGIS 3.32.0\bin\geos_c"
# GDAL_LIBRARY_PATH =r"C:\Program Files\QGIS 3.32.0\bin\gdal307"


# sitepass:wayfmap
# dbpasss:wKTyQPygyM86JAi4aqkm
# Host: 127.0.0.1 Port: 3306

# ssh
# david-ssh
# DBFC8RXN47e7B5RIo9KM

# allset-wayfmap: wKTyQPygyM86JAi4aqkm wayfmap321#
# password: goTomway321#

# server {
#     listen 80;
#     server_name 178.16.129.238;

#     access_log off;

#     location /static/ {
#         alias /home/allset-wayfmap/htdocs/wayfmap.allset.co.il/static/;
#     }

#     location / {
#         proxy_pass http://178.16.129.238:8000;
#         proxy_set_header X-Forwarded-Host $server_name;
#         proxy_set_header X-Real-IP $remote_addr;
#         add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
#     }
# }

# wayfmap.allset.co.il.uwsgi.ini
# command = '/home/allset-wayfmap/htdocs/wayfmap.allset.co.il/myvenv/bin/gunicorn'
# pythonpath = "/home/allset-wayfmap/htdocs/wayfmap.allset.co.il/mapmk"
# bind = "178.16.129.238:8000"
# workers = 3
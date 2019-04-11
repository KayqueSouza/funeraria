from unipath import Path

from dj_database_url import parse as parse_db_url
from django_cache_url import parse as parse_cache_url
from prettyconf import config


#  Project Structure
BASE_DIR = Path(__file__).ancestor(3)
PROJECT_DIR = Path(__file__).ancestor(2)
FRONTEND_DIR = PROJECT_DIR.child("frontend")

#  Debug & Development
DEBUG = config('DEBUG', default=False, cast=config.boolean)

#  Database
DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=parse_db_url,
        default='sqlite:///db.sqlite3'
    ),
}
DATABASES['default']['CONN_MAX_AGE'] = config('CONN_MAX_AGE', cast=config.eval, default='None')  #  always connected
DATABASES['default']['TEST'] = {'NAME': config('TEST_DATABASE_NAME', default=None)}

#  Security & Signup/Signin
ADMIN_USERNAME = config('ADMIN_USERNAME', default='ADMIN')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=config.list)
SECRET_KEY = config('SECRET_KEY', default='example-kn59*npHxq)G#p7VkwfZCb)RgtUWaJjfDBrEYJ6fEk9Sj$(d)Q#uZ6U##')

#  Media & Static
MEDIA_URL = "/media/"
MEDIA_ROOT = config('MEDIA_ROOT', default=FRONTEND_DIR.child("media"))

# STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_URL = '/static/'


STATIC_ROOT = config(
    'STATIC_ROOT', default=str(FRONTEND_DIR.child('collected_static'))
)

STATICFILES_DIRS = [
    FRONTEND_DIR.child("static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

#  Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            FRONTEND_DIR.child("templates"),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': config("TEMPLATE_DEBUG", default=DEBUG, cast=config.boolean),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'funeraria.urls'
WSGI_APPLICATION = 'funeraria.wsgi.application'

# CACHES = {
#     'default': config('CACHE_URL', default='locmem://', cast=parse_cache_url)
# }

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',

    #  3rd party libs
    'django_filters',
    'corsheaders',
    'django_stuff',
    #  local libs
    'apps.core',
    'apps.ordem_servico',
    'apps.usuario',
    'apps.pedido_material',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#  Internationalization
#  https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("en", "English"),
    ("pt-br", "Português (Brasil)"),
)
LOCALE_PATHS = (
    PROJECT_DIR.child("locale"),
)


#  Cors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

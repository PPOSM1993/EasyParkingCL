from pathlib import Path
import os
import environ
from datetime import timedelta

os.environ['GDAL_LIBRARY_PATH'] = '/usr/lib/libgdal.so'  # solo si usas GDAL

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga .env
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = env.bool('DJANGO_DEBUG', default=False)

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'apps.authentication',
    'apps.ai',
    'apps.parking',
    'apps.locations',
    'apps.directions',
    'apps.core',
    'apps.notifications',
    'apps.session',
    'apps.vehicles',
    'apps.users',
    'apps.payments',

    #INSTALLED DEPENDENCIES
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'drf_yasg',
    'rest_framework_gis',
    #'swagger_ui.apps.YamlConverterConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easypark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'easypark.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],

}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

AUTHENTICATION_BACKENDS = [
    'apps.authentication.backends.EmailUsernameRutBackend',  # Custom backend
    'django.contrib.auth.backends.ModelBackend',             # Por defecto (opcional)
]

# Modo desarrollo (email por consola)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@coworkapp.local'


AUTH_USER_MODEL = 'authentication.User'
#AUTH_USER_MODEL = 'users.User'

CORS_ALLOWED_ORIGINS = [
    #"https://example.com",
    #"https://sub.example.com",
    #"http://localhost:8081",
    #"http://127.0.0.1:9000",
]


print(f"POSTGRES_DB: {env('POSTGRES_DB')}")
print(f"POSTGRES_USER: {env('POSTGRES_USER')}")
print(f"POSTGRES_PASSWORD: {env('POSTGRES_PASSWORD')}")
print(f"POSTGRES_HOST: {env('POSTGRES_HOST')}")
print(f"POSTGRES_PORT: {env('POSTGRES_PORT')}")

JAZZMIN_SETTINGS = {
    "site_title": "EasyParking CL Admin",
    "site_header": "EasyParking CL",
    "site_brand": "EasyParking",
    "welcome_sign": "EasyParking Panel de Administracion 🚗",
    #"site_logo": "img/logo1.png",  # <-- solo la ruta desde 'static/'
    #"login_logo": "img/logo1.png",
    "site_logo_classes": "brand-image",  # <- solo esto, sin 'img-circle'
    "copyright": "EasyParking © 2025",
    #"custom_css": "css/custom.css",  # Lo usaremos en el siguiente paso
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "order_with_respect_to": ["auth", "users", "parkings", "ciudades"],
    # Login
    "show_sidebar": True,
    "navigation_expanded": True,
    "user_avatar": None,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "parking.Parking": "fas fa-warehouse",
        "ciudades.Ciudad": "fas fa-city",
        # Añade tus modelos aquí
    },

    "default_icon_parents": "fas fa-folder-open",
    "default_icon_children": "fas fa-angle-right",

    "custom_links": {
        "auth": [{
            "name": "Documentación",
            "url": "https://docs.djangoproject.com/",
            "icon": "fas fa-book",
            "permissions": ["auth.view_user"]
        }]
    },

    "search_model": ["auth.User", "parking.Parking"],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",  # Otros: flatly, cyborg, journal, lumen, etc.
    "dark_mode_theme": "cyborg",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark bg-primary",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_flat_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_child_hide": False,
    "sidebar_nav_icon": "circle",
}
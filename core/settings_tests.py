from .settings import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

TEMPLATES[0].update(
    {
        'DIRS': [
            os.path.join(BASE_DIR, 'build'),
            os.path.join(BASE_DIR, 'build', 'static'),
            os.path.join(BASE_DIR, 'static'),
        ]
    }
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ':memory:',
        'USER': 'testing_user',
        'PASSWORD': 'testing_password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': ':memory:',
        },
    }
}

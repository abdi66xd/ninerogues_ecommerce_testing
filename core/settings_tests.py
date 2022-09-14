from .settings import *

ALLOWED_HOSTS = ['127.0.0.1', '.localhost']
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'

TEMPLATES[0].update(
    {
        'DIRS': [
            os.path.join(BASE_DIR, 'build'),
            os.path.join(BASE_DIR, 'build', 'static'),
            os.path.join(BASE_DIR, 'templates'),
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

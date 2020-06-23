import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'migrations-git-conflicts'

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'migrations_git_conflicts',
    'tests.app_bar',
    'tests.app_foo',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
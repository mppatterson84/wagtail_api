from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    os.environ['LOCAL_IP'],
    'localhost',
    '127.0.0.1',
    'www.michael-patterson.com',
]

try:
    from .local import *
except ImportError:
    pass

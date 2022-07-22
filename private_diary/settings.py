from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
# AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django_ses.SESBackend'

NUMBER_GROUPING = 3

#ロギング設定
LOGGING = {
    'version': 1, # 1固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'hotel': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    #ハンドラの設定
    'handlers': {
        'file':{
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    #フォーマッタの設定
    'formatters':{
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

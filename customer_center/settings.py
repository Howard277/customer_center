"""
Django settings for customer_center project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import os

# 获取环境变量，通过环境变量设置配置参数
ENV = os.getenv('ENV')
# 打印出环境变量，便于排查问题
print('ENV:', ENV)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(a93ols_158i-2kqr1y@v^@-$%w)xig=23+76ucsdxhzpvla)n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ATOMIC_REQUESTS = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer',
    'order'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.logmiddleware.LogMiddleware',
]

ROOT_URLCONF = 'customer_center.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'customer_center.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'customer',
        'USER': 'root',
        'PASSWORD': '1qaz!QAZ',
        'HOST': 'localhost',
        'PORT': '3306',
    }
    # , 'db_slave': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'customer_slave',
    #     'USER': 'root',
    #     'PASSWORD': '1qaz!QAZ',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}
# 数据库路由配置
# DATABASE_ROUTERS = ['customer_center.dbrouter.Router', ]
# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

# redis配置
REDIS_SENTINELS = [('192.168.13.118', 27001), ('192.168.13.118', 27002), ('192.168.13.118', 27003)]
REDIS_SERVICE_NAME = 'mymaster'
REDIS_PASSWORD = '1qaz!QAZ'
REDIS_DB = 0

# 设置不同环境下的变量
if ENV == 'test':
    # 数据库配置
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'hb_customer',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '192.168.13.18',
            'PORT': '3306',
        }, 'db_slave': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'hb_customer',
            'USER': 'root',
            'PASSWORD': 'root123',
            'HOST': '192.168.13.17',
            'PORT': '3306',
        }
    }
    # 日志配置
    BASE_LOG_DIR = os.getcwd() + '/log/'
    if not os.path.exists(BASE_LOG_DIR):
        print('创建日志文件夹：', BASE_LOG_DIR)
        os.mkdir(BASE_LOG_DIR)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                          '[%(levelname)s][%(message)s]'
            },
            'simple': {
                'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
            },
            'collect': {
                'format': '%(message)s'
            }
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'SF': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
                'filename': os.path.join(BASE_LOG_DIR, "info.log"),  # 日志文件
                'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
                'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
                'formatter': 'standard',
                'encoding': 'utf-8',
            },
            'TF': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，根据时间自动切
                'filename': os.path.join(BASE_LOG_DIR, "info.log"),  # 日志文件
                'backupCount': 3,  # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
                'when': 'D',  # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
                'formatter': 'standard',
                'encoding': 'utf-8',
            },
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
                'filename': os.path.join(BASE_LOG_DIR, "err.log"),  # 日志文件
                'maxBytes': 1024 * 1024 * 5,  # 日志大小 50M
                'backupCount': 5,
                'formatter': 'standard',
                'encoding': 'utf-8',
            }
        },
        'loggers': {
            '': {  # 默认的logger应用如下配置
                'handlers': ['SF', 'TF', 'error'],  # 上线之后可以把'console'移除
                'level': 'DEBUG',
                'propagate': True,
            }
        },
    }

"""
Django settings for Django_Blog project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!bvt-!&^zj-xqpdu$9xu#8*^fximunwhv@!4z1pd6+l-e381!#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',  # 后台
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',#博客应用
    'mdeditor',#Markdown编辑器
    'import_export',#导入导出插件
    'pure_pagination',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_params',#自定义全局变量
            ],
        },
    },
]

WSGI_APPLICATION = 'Django_Blog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#   'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'django_blog',
#        'USER': 'root',
#        'PASSWORD': 'root',
#        'HOST': 'localhost',
#        'PORT': '3306',
#        'OPTIONS': {'charset': 'utf8mb4'},
#    }
# }
#

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


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = True
#日期格式
DATETIME_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "bolg/static")
#]


#SimpleUi后台设置
SIMPLEUI_LOGO = 'https://i.loli.net/2021/07/18/tVSUv6DfFiaPMqH.gif' #登录页和后台logo
SIMPLEUI_ANALYSIS = False #是否向SimpleUi收集分析信息
SIMPLEUI_LOADING = False #是否打开Loading遮罩层
SIMPLEUI_LOGIN_PARTICLES = True #登录页粒子动画
SIMPLEUI_STATIC_OFFLINE = True #是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目，不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_HOME_INFO = False #是否打开SimpleUi服务器信息
SIMPLEUI_DEFAULT_THEME = 'simpleui.css' #默认主题 https://simpleui.88cto.com/docs/simpleui/QUICK.html#%E9%BB%98%E8%AE%A4%E4%B8%BB%E9%A2%98
SIMPLEUI_HOME_QUICK = True #后台页面是否显示最近动作
#自定义后台菜单
SIMPLEUI_CONFIG = {
    'system_keep': False,  #去除系统模块
    'menus': [{
        'name': '文章管理',
        'icon': 'fas fa-book-open',
        'models': [{
                'name': '文章',
                'icon': 'fas fa-book-open',
                'url': '/admin/blog/article/'
            },{
                'name': '分类',
                'icon': 'fas fa-list',
                'url': '/admin/blog/category/'
            },{
                'name': '标签',
                'icon': 'fas fa-tags',
                'url': '/admin/blog/tag/'
            }]
    }, {
        'name': '成员',
        'icon': 'far fa-user',
        'url': '/admin/blog/link/'
    }, {
        'name': '公告栏',
        'icon': 'fas fa-bullhorn',
        'url': '/admin/blog/notice/'
    },{
        'name': '关于设置',
        'icon': 'fas fa-address-card',
        'models': [{
            'name': '基本信息',
            'icon': 'far fa-file',
            'url': '/admin/blog/about/'
            },{
            'name': '社交',
            'icon': 'fas fa-comment-alt',
            'url': '/admin/blog/social/'
            },{
            'name': '技能',
            'icon': 'fas fa-drafting-compass',
            'url': '/admin/blog/skill/'
            }]
    }, {
        'name': '网站设置',
        'icon': 'fas fa-globe-americas',
        'url': '/admin/blog/site/'
    }, {
        'name': 'valine评论',
        'icon': 'far fa-comments',
        'url': '/admin/blog/valine/'
    }, {
        'app': 'auth',
        'name': '用户和授权',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },{
            'name': '权限组',
            'icon': 'fas fa-users-cog',
            'url': 'auth/group/'
        }]
    },
    #     {
    #     'name': '网页预览',
    #     'icon': 'fas fa-paper-plane',
    #     'models': [{
    #         'name': 'CovTeam',
    #         'url': 'http://covteam.jwt1399.top/',
    #         'icon': 'fab fa-wolf-pack-battalion'
    #     }, {
    #         'name': '简简',
    #         'url': 'https://jwt1399.top',
    #         'icon': 'fas fa-crown'
    #     }]
    # }
    ]
}

#mdeditor设置
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'   #你上传的文件和图片会默认存在/uploads/editor下
X_FRAME_OPTIONS = 'SAMEORIGIN'

# 日志记录
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' :"[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' :"%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'blog': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

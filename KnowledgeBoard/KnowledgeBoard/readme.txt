========================注意 settings 的配置 :==============================
"""
Django settings for Django2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gma6e_f)18rz1j=bkzpqr4mm2016=)608a$4i@cknay5b$90l$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
ADMINS = (('luokjy','luokjy2341@163.com'))
MANAGERS = ADMINS
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (         # to refer system or user-defined classes(lib)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'mvc',
)

MIDDLEWARE_CLASSES = (
     'django.middleware.cache.UpdateCacheMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
     'django.middleware.transaction.TransactionMiddleware',
     'django.middleware.cache.FetchFromCacheMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
     
 )

ROOT_URLCONF = 'KnowledgeBoard.urls'   # refer the urls.py 

WSGI_APPLICATION = 'KnowledgeBoard.wsgi.application'  # refer the wsgi.py 


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'knowledgeboard',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'  # For China User

SITE_ID = 1

TIME_ZONE = 'Asia/Shanghai' # For China User

USE_I18N = True

USE_L10N = True

USE_TZ = False  # it's import to leave USE_TZ False , or the time data instered into db will be 8h later than currenttime;

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/templates/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
     'django.contrib.staticfiles.finders.FileSystemFinder',  
     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_LOADERS = (
      'django.template.loaders.filesystem.Loader',  
      'django.template.loaders.app_directories.Loader',              
)

MIDDLEWARE_CLASSES = (
      'django.middleware.common.CommonMiddleware',  
      'django.contrib.sessions.middleware.SessionMiddleware',  
      'django.middleware.csrf.CsrfViewMiddleware',               # for security reason :anti-csrf ; and the other classes are common configurations;
      'django.contrib.auth.middleware.AuthenticationMiddleware',  
      'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
      'templates', # here to config the dir storing htmls(templates)       
)

LOGGING = {
       'version':1,
       'disable_existing_loggers': False,
       'filters':{
            'require_debug_false':{ 
                        '()':'django.utils.log.RequireDebugFalse' 
             }
        },
        'handlers':{
             'mail_admins':{
                  'level':'ERROR',
                  'filters':['require_debug_false'],
                  'class':'django.utils.log.AdminEmailHandler'  
              }
        },
        'loggers':{
             'django.request':{
                  'handlers':['mail_admins'],
                  'level':'ERROR',
                  'propagate':True
              }         
        
        }
}

========================注意 urls 的配置 :==============================

from django.conf.urls import patterns, include, url
from django.contrib import admin
from mvc.views import get_docs
from mvc.views import add_doc
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KnowledgeBoard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/$',get_docs),
)

========================注意 wsgi 的配置 :==============================

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KnowledgeBoard.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


========================注意 wsgi 的配置 :===============================


========================注意 session的使用 :==============================

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')
    
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')
    































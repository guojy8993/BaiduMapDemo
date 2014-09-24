from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jobs/$','jobs.views.index'),
    url(r'^jobs/(?P<job_id>\d+)/$','jobs.views.detail'),
    url(r'index','jobs.views.main'),
    url(r'^admin/', admin.site.urls),
)

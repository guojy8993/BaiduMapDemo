from django.conf.urls import patterns, include, url
from django.contrib import admin
from mvc.views import get_docs
from mvc.views import add_doc
from mvc.views import to_add_doc
from mvc.views import user_list
from mvc.views import goto_register
from mvc.views import user_register
from mvc.views import user_login
from mvc.views import goto_login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KnowledgeBoard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/$',get_docs),
    url(r'^docs/add/$',add_doc),
    url(r'^docs/to_adddoc/$',to_add_doc),
    url(r'^users/list$',user_list),
    url(r'^user/goto_register$',goto_register),
    url(r'^user/register$',user_register),
    url(r'^user/login$',user_login),
    url(r'^user/goto_login$',goto_login),
)

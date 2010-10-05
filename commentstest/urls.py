from django.conf.urls.defaults import *
from django.views.generic import list_detail
from weblog.models import Entry
from django.contrib import admin
admin.autodiscover()

info_dict = {
    'queryset': Entry.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^commentstest/', include('commentstest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', list_detail.object_list, info_dict, 'weblog_home'),

    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, info_dict, 'weblog_entry_detail'),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    
)

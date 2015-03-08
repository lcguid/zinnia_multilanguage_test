from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'zinnia_multilanguage_test.views.hello_world', name='home'),

    url(r'^admin/', include(admin.site.urls)),

   url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    # url(r'^comments/', include('django_comments.urls')),

)

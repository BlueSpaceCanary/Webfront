from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ASHMC.views.home', name='home'),
    # url(r'^ASHMC/', include('ASHMC.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^courses/', include('ASHMC.courses.urls')),

    url(r'^blog/', include('blogger.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^', include('ASHMC.main.urls')),
)

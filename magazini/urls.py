from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#import Views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home'),
    # url(r'^magazini/', include('magazini.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.default.urls')),

)

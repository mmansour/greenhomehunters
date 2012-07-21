from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from mezzanine.core.views import direct_to_template
admin.autodiscover()

urlpatterns = patterns('gogreen.views',
    url("^$", "home", name="home"),
)





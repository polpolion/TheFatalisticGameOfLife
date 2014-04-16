from django.conf.urls import patterns, include, url

from django.contrib import admin
from tfgol_web import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TFGOL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.mainpage)
)

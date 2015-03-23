from django.conf.urls import patterns, include, url

from django.contrib import admin
#from helloworld.views import greeting
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
	#url(r'^$',greeting),
    # Examples:
    # url(r'^$', 'suorganizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

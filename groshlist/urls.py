from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^groshlist/', include('groshlist.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	# (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),

    (r'^login/$', 'guide.views.userlogin'),
    (r'^logout/$', 'guide.views.userlogout'),
    (r'^register/', 'guide.views.register'),
    (r'^contact/', 'guide.views.contact'),
    (r'^imprint/', 'guide.views.imprint'),

	(r'^market/create/$', 'guide.views.createmarket'),
	(r'^market/detail/(?P<market_id>\d)', 'guide.views.market_detail'),
	(r'^market/edit/(?P<market_id>\d)', 'guide.views.market_edit'),
	(r'^market/$', 'guide.views.market'),
	(r'^$', 'guide.views.index'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
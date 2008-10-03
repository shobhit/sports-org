from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^org/', include('org.urls')),
)

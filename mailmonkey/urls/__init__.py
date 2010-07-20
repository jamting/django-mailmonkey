"""Default urls for the mailmonkey"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',                       
                       url(r'^mailing/', include('mailmonkey.urls.mailing_list')),
                       url(r'^tracking/', include('mailmonkey.urls.tracking')),
                       url(r'^statistics/', include('mailmonkey.urls.statistics')),
                       url(r'^', include('mailmonkey.urls.newsletter')),
                       )

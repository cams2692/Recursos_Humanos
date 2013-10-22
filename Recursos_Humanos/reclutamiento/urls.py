from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   
    url(r'^test/$', 'reclutamiento.views.view_test',name='test'),    
)
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
     (r'^courses/$', 'resource.views.CourseAll'),
     (r'^courses/(?P<courseslug>.*)/$', 'resource.views.SpecificCourse'),
     (r'^organisations/(?P<organisationslug>.*)/$', 'resource.views.SpecificOrganisation'),
     
     (r'^$', direct_to_template, {'template': 'index.html'})
)

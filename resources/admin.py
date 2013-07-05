from django.contrib import admin
from resources.models import Course, Organisation

class CourseAdmin(admin.ModelAdmin):
	    prepopulated_fields = {'slug': ('name',)}
	    list_display = ('name', 'organisation', 'description')
	    search_fields = ['name']


class OrganisationAdmin(admin.ModelAdmin):
	    prepopulated_fields = {'slug': ('name',)}	



admin.site.register(Course, CourseAdmin)
admin.site.register(Organisation, OrganisationAdmin)
from django.shortcuts import render_to_response
from django.template import RequestContext
from resource.models import Course


def CourseAll(request):
		courses = Course.objects.all().order_by('name')
		context = {'courses' : courses}
		return render_to_response('courses.html', context, context_instance=RequestContext(request))

def SpecificCourse(request, courseslug):
		course = Course.objects.get(slug=courseslug)
		context = {'course' : course}
		return render_to_response('course.html', context, context_instance=RequestContext(request))


def SpecificOrganisation(request, organisationslug):
		organisation = Course.objects.get(slug=organisationslug)
		context = {'organisation' : organisation}
		return render_to_response('organisation.html', context, context_instance=RequestContext(request))

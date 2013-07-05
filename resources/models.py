from django.db import models

class Course(models.Model):
		name              = models.CharField(max_length=200)
		slug              = models.SlugField(unique=True)
		organisation      = models.ForeignKey('Organisation')
		description       = models.TextField(blank=True)


		def __unicode__(self):
			    return self.name
			


class Organisation(models.Model):
		name = models.CharField(max_length=200)
		slug = models.SlugField(unique=True)
		description = models.TextField(blank=True)


		def __unicode__(self):
				return self.name
		       	       
from django.contrib import admin
from measurements.models import Measurement, Project


admin.site.register(Measurement)
admin.site.register(Project)

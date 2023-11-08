from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(CourseRegistration)

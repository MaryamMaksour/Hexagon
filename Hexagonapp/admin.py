from django.contrib import admin
from .models import Project, Project2, questions

# Register your models here.
admin.site.register(Project)
admin.site.register(Project2)
admin.site.register(questions)
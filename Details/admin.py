from django.contrib import admin
from .models import ArtStyle, Mentor, Student

# Register your models here.
admin.site.register(ArtStyle)
admin.site.register(Mentor)
admin.site.register(Student)

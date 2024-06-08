from django.contrib import admin
from .models import Klass, Teacher, Student

# Register your models here.


class KlassAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('number',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'price')
    list_display_links = ('full_name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'klass')
    list_display_links = ('full_name',)


admin.site.register(Klass, KlassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

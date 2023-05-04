from django.contrib import admin
from .models import ExamCenter,Student,Teacher,Page

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['cname','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['base_id', 'name','roll','cname','city','created_at','updated_at']

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','age','city','created_at','updated_at']

@admin.register(Page)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','date','date','user']


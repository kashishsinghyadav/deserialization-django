from django.contrib import admin
from .models import Student

class Stu_ad(admin.ModelAdmin):
    list_display=('id','name','roll_no','city')

admin.site.register(Student,Stu_ad)

# Register your models here.

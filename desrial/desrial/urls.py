
from django.contrib import admin
from django.urls import path
from kash import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/',views.student_create),
]

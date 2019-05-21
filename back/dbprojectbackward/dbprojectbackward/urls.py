"""dbprojectbackward URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from modelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('test2/', views.test2),
    path('search_studentinfo_all/', views.search_studentinfo_all),
    path('search_teacherinfo_all/', views.search_teacherinfo_all),
    path('search_courseinfo_all/', views.search_courseinfo_all),
    path('insert_studentinfo', views.insert_studentinfo),
    path('insert_teacherinfo', views.insert_teacherinfo),
    path('insert_courseinfo', views.insert_courseinfo),
    path('search_score_by_id', views.search_score_by_id),
    path('check_login', views.check_login),
    path('start_choose_course', views.start_choose_course),
    path('stop_choose_course', views.stop_choose_course),
    path('start_upload_score', views.start_upload_score),
    path('stop_upload_score', views.stop_upload_score),
    path('search_choose_course', views.search_choose_course),
    path('search_upload_score', views.search_upload_score),
    path('search_two_states', views.search_two_states),
    path('update_studentinfo', views.update_studentinfo),
    path('update_teacherinfo', views.update_teacherinfo),
    path('update_courseinfo', views.update_courseinfo),
    path('delete_studentinfo', views.delete_studentinfo),
    path('delete_teacherinfo', views.delete_teacherinfo),
    path('delete_courseinfo', views.delete_courseinfo),
    path('search_courseinfo_ownedby', views.search_courseinfo_ownedby),
    path('search_studentinfo_by_id', views.search_studentinfo_by_id),
    path('upload_grade', views.upload_grade),
    path('search_courseinfo_by', views.search_courseinfo_by),
    path('choose_course', views.choose_course),
    path('search_my_course', views.search_my_course),
    path('quit_course', views.quit_course),
    path('my_score_all', views.my_score_all)
]

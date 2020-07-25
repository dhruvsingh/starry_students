# -*- coding: utf-8 -*-
from django.urls import path

from starry_students.manager import views

app_name = "manager"
urlpatterns = [
    path(
        "students/",
        view=views.StudentListView.as_view(),
        name="student_list"
    ),
    path(
        "students/<int:id>",
        view=views.StudentDetailView.as_view(),
        name="student_detail"
    ),
    path(
        "students/add/",
        view=views.StudentAddView.as_view(),
        name="student_add"
    ),
]

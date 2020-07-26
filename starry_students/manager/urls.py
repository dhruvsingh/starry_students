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
        "students/<int:id>/",
        view=views.StudentDetailView.as_view(),
        name="student_detail"
    ),
    path(
        "students/<int:id>/update/",
        view=views.StudentUpdateView.as_view(),
        name="student_update"
    ),
    path(
        "students/add/",
        view=views.StudentAddView.as_view(),
        name="student_add"
    ),
    path(
        "students/<int:id>/delete/",
        view=views.StudentDeleteView.as_view(),
        name="student_delete"
    ),
    # teacher urls
    path(
        "teachers/",
        view=views.TeacherListView.as_view(),
        name="teacher_list"
    ),
    path(
        "teachers/<int:id>/",
        view=views.TeacherDetailView.as_view(),
        name="teacher_detail"
    ),
    path(
        "teachers/<int:id>/update/",
        view=views.TeacherUpdateView.as_view(),
        name="teacher_update"
    ),
    path(
        "teachers/add/",
        view=views.TeacherAddView.as_view(),
        name="teacher_add"
    ),
    path(
        "teachers/<int:id>/delete/",
        view=views.TeacherDeleteView.as_view(),
        name="teacher_delete"
    ),
    path(
        "teachers/<int:id>/<int:student_id>/",
        view=views.StudentStarView.as_view(),
        name="student_star_view"
    ),
]

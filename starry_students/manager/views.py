# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.
from starry_students.manager.forms import StudentAddUpdateForm
from starry_students.manager.models import Student


class StudentListView(ListView):
    """View to list all in/active students"""

    model = Student
    template_name = 'manager/student/list.html'


class StudentDetailView(DetailView):
    """View to list all in/active students"""

    model = Student
    pk_url_kwarg = 'id'
    template_name = 'manager/student/detail.html'


class StudentUpdateView(UpdateView):
    """View to update a student."""

    pk_url_kwarg = 'id'
    model = Student
    form_class = StudentAddUpdateForm
    success_url = reverse_lazy("manager:student_list")
    template_name = 'manager/student/update.html'


class StudentAddView(CreateView):
    """View to list all in/active students."""

    form_class = StudentAddUpdateForm
    success_url = reverse_lazy("manager:student_list")
    template_name = 'manager/student/add.html'


class StudentDeleteView(DeleteView):
    """View to delete student."""

    pk_url_kwarg = 'id'
    queryset = Student.objects.all()
    success_url = reverse_lazy("manager:student_list")
    template_name = 'manager/student/delete.html'

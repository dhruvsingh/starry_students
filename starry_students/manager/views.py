# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
from starry_students.manager.forms import StudentAddForm
from starry_students.manager.models import Student


class StudentListView(ListView):
    """View to list all in/active students"""

    model = Student
    template_name = 'manager/student_list.html'


class StudentDetailView(DetailView):
    """View to list all in/active students"""

    model = Student
    pk_url_kwarg = 'id'
    template_name = 'manager/student_detail.html'


class StudentAddView(CreateView):
    """View to list all in/active students"""

    form_class = StudentAddForm
    success_url = reverse_lazy("home")
    template_name = 'manager/student_add.html'

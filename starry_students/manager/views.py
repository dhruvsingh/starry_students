# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from starry_students.manager.forms import (
    StudentAddUpdateForm,
    TeacherAddUpdateForm,
)
from starry_students.manager.models import Student, Teacher, TeacherStudent


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


# ------------------------ Teacher Views --------------------------------------


class TeacherListView(ListView):
    """View to list all in/active teachers."""

    model = Teacher
    queryset = Teacher.objects.all().prefetch_related('students')
    template_name = 'manager/teacher/list.html'


class TeacherDetailView(DetailView):
    """View to list all in/active teachers"""

    model = Teacher
    pk_url_kwarg = 'id'
    queryset = Teacher.objects.all().prefetch_related('students')
    template_name = 'manager/teacher/detail.html'


class TeacherUpdateView(UpdateView):
    """View to update a teacher."""

    pk_url_kwarg = 'id'
    model = Teacher
    form_class = TeacherAddUpdateForm
    queryset = Teacher.objects.all().prefetch_related('students')
    success_url = reverse_lazy("manager:teacher_list")
    template_name = 'manager/teacher/update.html'


class TeacherAddView(CreateView):
    """View to list all in/active Teachers."""

    form_class = TeacherAddUpdateForm
    success_url = reverse_lazy("manager:teacher_list")
    template_name = 'manager/teacher/add.html'


class TeacherDeleteView(DeleteView):
    """View to delete student."""

    pk_url_kwarg = 'id'
    queryset = Teacher.objects.all()
    success_url = reverse_lazy("manager:teacher_list")
    template_name = 'manager/teacher/delete.html'


class StudentStarView(UpdateView):
    """View to delete student."""

    model = TeacherStudent
    queryset = TeacherStudent.objects.all()
    success_url = reverse_lazy("manager:teacher_list")

    def get_object(self, queryset=None):
        """Exact teacher student match."""
        return TeacherStudent.objects.filter(
            teacher_id=self.kwargs.get('id'),
            student_id=self.kwargs.get('student_id'),
        ).first()

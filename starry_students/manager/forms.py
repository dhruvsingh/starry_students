# -*- coding: utf-8 -*-
from django.forms import ModelForm

from starry_students.manager.models import Student, Teacher


class StudentAddUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name',)


class TeacherAddUpdateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'students')

    def save(self, *args, **kwargs):
        """Overridden since we need to save Many2Many."""
        instance = super().save(commit=False)
        self.instance.save()
        self.save_m2m()
        return instance

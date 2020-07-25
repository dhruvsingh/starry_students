# -*- coding: utf-8 -*-
from django.forms import ModelForm

from starry_students.manager.models import Student


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name',)

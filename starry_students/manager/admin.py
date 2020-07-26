# -*- coding: utf-8 -*-
from django.contrib import admin
from starry_students.manager.models import TeacherStudent, Teacher, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TeacherStudent)

# -*- coding: utf-8 -*-
import graphene

from graphene_django.types import DjangoObjectType

from starry_students.manager.models import Teacher, Student, TeacherStudent


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class TeacherStudentType(DjangoObjectType):
    class Meta:
        model = TeacherStudent


class Query(object):
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)
    starred_students = graphene.List(TeacherStudentType)

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_all_teachers(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Teacher.objects.prefetch_related('students').all()

    def resolve_starred_students(self, info, **kwargs):
        # list of all teacher and students they have starred
        return TeacherStudent.objects.filter(
            starred_student=True
        ).select_related(
            'student',
            'teacher'
        )

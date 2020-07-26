# -*- coding: utf-8 -*-
import graphene

from graphene_django.types import DjangoObjectType

from starry_students.manager.models import Teacher, Student


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(object):
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_all_teachers(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Teacher.objects.prefetch_related('students').all()

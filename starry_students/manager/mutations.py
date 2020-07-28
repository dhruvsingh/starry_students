# -*- coding: utf-8 -*-
import graphene

from .models import TeacherStudent
from .schema import TeacherStudentType



class StarMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        teacher_id = graphene.ID()
        student_id = graphene.ID()
        starred_student = graphene.Boolean(required=True)

    # The class attributes define the response of the mutation
    ts_obj = graphene.Field(TeacherStudentType)

    def mutate(self, info, teacher_id, student_id, starred_student):
        ts_obj = TeacherStudent.objects.get(teacher_id=teacher_id, student_id=student_id)
        ts_obj.starred_student = starred_student
        ts_obj.save()
        # Notice we return an instance of this mutation
        return StarMutation(ts_obj=ts_obj)


class Mutation(graphene.ObjectType):
    update_star = StarMutation.Field()

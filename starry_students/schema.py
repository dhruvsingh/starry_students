# -*- coding: utf-8 -*-
import graphene

import starry_students.manager.schema
from starry_students.manager.mutations import Mutation

class Query(starry_students.manager.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)


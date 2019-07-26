from graphene_django import DjangoObjectType
import graphene
from .models import Team
from organization.schema import OrganizationType

class DeleteTeam(graphene.Mutation):
    return False



class Mutation(graphene.ObjectType):
    delete_team = DeleteTeam.Field()
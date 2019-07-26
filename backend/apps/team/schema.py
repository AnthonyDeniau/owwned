from graphene_django import DjangoObjectType
import graphene
from .models import Team
from organization.schema import OrganizationType


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


class Query(graphene.ObjectType):
    team = graphene.Field(TeamType, id=graphene.Int(), name=graphene.String())
    teams = graphene.List(TeamType)

    def resolve_team(self, context, id=None, name=None):
        if id is not None:
            return Team.objects.get(pk=id)

        if name is not None:
            return Team.objects.get(name=name)

        return None

    def resolve_teams(self, context):
        return Team.objects.all()


class CreateTeam(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    user = graphene.ID()
    organization = graphene.Field(OrganizationType)

    class Arguments:
        name = graphene.String(required=True)
        organization = graphene.ID()
        user = graphene.ID()

    def mutate(self, info, name, organization, user):
        team = Team(name=name, organization_id=organization, user_id=user)
        team.save()
        return CreateTeam(id=team.id,
                          name=team.name,
                          organization=team.organization)
    
class DeleteTeam(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
    
    def mutate(self,info,id):
        team = Team.objects.get(pk=id)
        team.delete()
        return DeleteTeam(is_delete=True)


class UpdateTeam(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    user = graphene.ID()
    organization = graphene.Field(OrganizationType)

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        user = graphene.ID()
        organization = graphene.ID()
    
    def mutate(self,info,id,name,user,organization):
        team = Team.objects.get(pk=id)
        team.name = name
        team.user = user
        team.organization = organization
        team.save()
        return UpdateTeam(id,name,user,organization)




class Mutation(graphene.ObjectType):
    create_team = CreateTeam.Field()
    delete_team = DeleteTeam.Field()
    update_team = UpdateTeam.Field()
   


schema = graphene.Schema(query=Query, mutation=Mutation)
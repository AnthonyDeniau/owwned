from .models import Organization
from team.models import Team
from graphene_django import DjangoObjectType
import graphene


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization


class Query(graphene.ObjectType):

    organization = graphene.Field(OrganizationType,
                                  id=graphene.Int(),
                                  name=graphene.String())
    organizations = graphene.List(OrganizationType)

    def resolve_organizations(self, context):
        return Organization.objects.all()

    def resolve_organization(self, context, id=None, name=None):
        if id is not None:
            return Organization.objects.get(pk=id)

        if name is not None:
            return Organization.objects.get(name=name)

        return None


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


class Mutation(graphene.ObjectType):
    create_team = CreateTeam.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
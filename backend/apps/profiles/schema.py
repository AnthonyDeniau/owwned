from graphene_django import DjangoObjectType
import graphene
from .models import Profiles


class ProfilesType(DjangoObjectType):
    class Meta:
        model = Profiles


class Query(graphene.ObjectType):
    profile = graphene.Field(ProfilesType, id=graphene.Int())
    profiles = graphene.List(ProfilesType)

    def resolve_profile(self, context, id=None):
        if id is not None:
            return Profiles.objects.get(pk=id)
        return None

    def resolve_profiles(self, context):
        return Profiles.objects.all()


class CreateProfiles(graphene.Mutation):
    id = graphene.Int()
    user = graphene.ID()
    team = graphene.ID()

    class Arguments:
        user = graphene.ID()
        team = graphene.ID()

    def mutate(self, info, user, team):
        profile = Profiles(user_id=user, team_id=team)
        profile.save()
        return CreateProfiles(id=profile.id,
                              user=profile.user,
                              team=profile.team)


class Mutation(graphene.ObjectType):
    create_profile = CreateProfiles.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

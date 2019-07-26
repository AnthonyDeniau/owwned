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


class UpdateProfiles(graphene.Mutation):
    id = graphene.Int()
    user = graphene.ID()
    team = graphene.ID()

    class Arguments:
        id = graphene.Int()
        user = graphene.ID()
        team = graphene.ID()

    def mutate(self, info, id, user=None, team=None):
        profile = Profiles.objects.get(pk=id)
        if (user is not None):
            profile.user_id = user
        if (team is not None):
            profile.team_id = team
        profile.save()
        return UpdateProfiles(id=profile.id,
                              user=profile.user,
                              team=profile.team)


class DeleteProfiles(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        profile = Profiles.objects.get(pk=id)
        profile.delete()
        return DeleteProfiles(is_delete=True)


class Mutation(graphene.ObjectType):
    create_profile = CreateProfiles.Field()
    update_profile = UpdateProfiles.Field()
    delete_profile = DeleteProfiles.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

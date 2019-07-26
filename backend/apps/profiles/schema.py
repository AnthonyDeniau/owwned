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


schema = graphene.Schema(query=Query)

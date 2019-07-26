from graphene_django import DjangoObjectType
import graphene
from .models import Profiles


class ProfilesType(DjangoObjectType):
    class Meta:
        model = Profiles

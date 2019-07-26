from graphene_django import DjangoObjectType
import graphene
from .models import Batitment, Floor, Room


class BatiementType(DjangoObjectType):
    class Meta:
        model = Batitment


class Query(graphene.ObjectType):
    batiement = graphene.Field(BatiementType, id=graphene.Int())
    batiement = graphene.List(BatiementType)

    def resolve_batiement(self, context, id=None):
        if id is not None:
            return batiement.objects.get(pk=id)
        return None

    def resolve_batiement(self, context):
        return batiement.objects.all()
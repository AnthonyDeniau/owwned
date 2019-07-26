from graphene_django import DjangoObjectType
import graphene
from .models import Batiment


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)
        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()


schema = graphene.Schema(query=Query)

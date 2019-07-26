from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room
from asset.schema import AssetType


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class Query(graphene.ObjectType):
    Batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String())
    Batiment = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None, name=None):
        if id is not None:
            return batiment.objects.get(pk=id)

        if name is not None:
            return batiment.objects.get(name=name)

        return None

    def resolve_batiments(self, context):
        return batiment.objects.all()


class Createbatiment(graphene.Mutation):
    latitude = graphene.Int()
    longitude = graphene.Int()
    name = graphene.String()
    

    class Arguments:        
        latitude = graphene.Int()
        longitude = graphene.Int()
        name = graphene.String()
    

    def mutate(self, latitude, longitude, name):
        batiment = batiment(latitude = latitude, longitude = longitude, name = name)
        batiment.save()
        return Createbatiment(latitude = batiment.latitude, longitude = batiment.longitude, name = batiment.name)

class Mutation(graphene.ObjectType):
    Createbatiment = Createbatiment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room



class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None, name=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        if name is not None:
            return Batiment.objects.get(name=name)

        return None

    def resolve_batiments(self, context):
        return Documentation.objects.all()


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    latitude = graphene.Float()
    longitude = graphene.Float()
    name = graphene.String()

    class Arguments:        
        latitude = graphene.Float()
        longitude = graphene.Float()
        name = graphene.String(required=True)
        

    def mutate(self, info, latitude, longitude, name):
        batiment = Batiment(latitude=latitude,longitude=longitude,name=name)
        batiment.save()
        return CreateBatiment(latitude = batiment.latitude,
                                   longitude = batiment.longitude,
                                   name = batiment.name)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)

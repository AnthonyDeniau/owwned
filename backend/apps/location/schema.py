from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class FloorType(DjangoObjectType):
    class Meta:
        model = Floor


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType,
                              id=graphene.Int(),
                              name=graphene.String(),
                              lat=graphene.Float(),
                              long=graphene.Float())
    batiments = graphene.List(BatimentType)

    def resolve_batiments(self, context):
        return Batiment.objects.all()

    def resolve_batiment(self,
                         context,
                         id=None,
                         name=None,
                         lat=None,
                         long=None):
        if id is not None:
            return Batiment.objects.get(pk=id)
        if name is not None:
            return Batiment.objects.get(name=name)

        return None


class CreateBatiment(graphene.Mutation):
    id = graphene.ID()
    lat = graphene.Float()
    long = graphene.Float()
    name = graphene.String()

    class Arguments:
        lat = graphene.Float()
        long = graphene.Float()
        name = graphene.String()

    def mutate(self, info, lat, long, name):
        batiment = Batiment(lat=lat, long=long, name=name)
        batiment.save()
        return CreateBatiment(id=batiment.pk,
                              lat=batiment.lat,
                              long=batiment.long,
                              name=batiment.name)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()


# schema = graphene.Schema(query=Query)

from graphene_django import DjangoObjectType
import graphene
from .models import Batiment


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String, lat=graphene.Int(),
                              long=graphene.Int())
    batiments = graphene.List(BatimentType)

    def resolve_organizations(self, context):
        return Batiment.objects.all()

    def resolve_batiment(self, context, id=None, name=None, lat=None, long=None):
        if id is not None:
            return Batiment.objects.get(pk=id)
        if name is not None:
            return Batiment.objects.get(name=name)
        if lat is not None:
            return Batiment.objects.get(name=lat)
        if long is not None:
            return Batiment.objects.get(name=long)

        return None


class CreateBatiment(graphene.Mutation):
    lat = graphene.Int()
    long = graphene.Int()
    name = graphene.String()

    class Arguments:
        lat = graphene.Int()
        long = graphene.Int()
        name = graphene.String()

    def mutate(self, info, lat, long, name):
        batiment = Batiment(lat=lat, long=long, name=name)
        batiment.save()
        return CreateBatiment(lat=batiment.lat,
                              long=batiment.long,
                              name=batiment.name)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

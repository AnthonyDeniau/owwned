from graphene_django import DjangoObjectType
import graphene
from .models import Building


class BuildingType(DjangoObjectType):
    class Meta:
        model = Building


class CreateBuilding(graphene.Mutation):
    id = graphene.Int()
    long = graphene.String()
    lat = graphene.String()

    def mutate(self, name, long, lat):
        building = Building(name=name, lat=lat, long=long)
        building.save()
        return CreateBuilding(name=building.name,
                              long=building.lat,
                              lat=building.long)


class Query(graphene.ObjectType):
    building = graphene.Field(CreateBuilding, id=graphene.Int())
    buildings = graphene.List(CreateBuilding)

    def resolve_building(self, context, id=None):
        if id is not None:
            return Building.objects.get(pk=id)

    def resolve_building(self, context):
        return Building.objects.all()


class Mutation(graphene.ObjectType):
    create_building = CreateBuilding.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

from graphene_django import DjangoObjectType
import graphene
from .models import Building, Floor, Room


class BuildingType(DjangoObjectType):
    class Meta:
        model = Building


class FloorType(DjangoObjectType):
    class Meta:
        model = Floor


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class Query(graphene.ObjectType):
    building = graphene.Field(BuildingType,
                              id=graphene.Int(),
                              name=graphene.String())
    buildings = graphene.List(BuildingType)

    def resolve_building(self, context, id=None, name=None):
        if id is not None:
            return Building.objects.get(pk=id)

        if name is not None:
            return Building.objects.get(name=name)

        return None

    def resolve_buildings(self, context):
        return Building.objects.all()


class CreateBuilding(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()

    class Arguments:
        name = graphene.String(required=True)
        latitude = graphene.Float(required=True)
        longitude = graphene.Float(required=True)

    def mutate(self, info, name, latitude, longitude):
        building = Building(name=name, latitude=latitude, longitude=longitude)
        building.save()
        return CreateBuilding(id=building.id,
                              name=building.name,
                              latitude=building.latitude,
                              longitude=building.longitude)


class Mutation(graphene.ObjectType):
    create_building = CreateBuilding.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

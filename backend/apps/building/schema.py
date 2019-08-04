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


class CreateBuilding(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    long = graphene.Decimal()
    lat = graphene.Decimal()

    class Arguments:
        name = graphene.String()
        long = graphene.Decimal()
        lat = graphene.Decimal()

    def mutate(self, info, name, long, lat):
        building = Building(name=name, lat=lat, long=long)
        building.save()
        return CreateBuilding(id=building.pk,
                              name=building.name,
                              long=building.lat,
                              lat=building.long)


class DeleteBuilding(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        building = Building.objects.get(pk=id)
        building.delete()
        return DeleteBuilding(status=True)


class UpdateBuilding(graphene.Mutation):
    name = graphene.String()
    long = graphene.Decimal()
    lat = graphene.Decimal()

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        long = graphene.Decimal()
        lat = graphene.Decimal()

    def mutate(self, info, id, name=None, long=None, lat=None):
        building = Building.objects.get(pk=id)
        if lat is not None:
            building.name = name
        if lat is not None:
            building.lat = lat
        if long is not None:
            building.long = long

        building.save()
        return UpdateBuilding(name=building.name,
                              long=building.lat,
                              lat=building.long)


class Query(graphene.ObjectType):
    building = graphene.Field(BuildingType, id=graphene.Int())
    buildings = graphene.List(BuildingType)

    def resolve_building(self, context, id=None):
        if id is not None:
            return Building.objects.get(pk=id)

    def resolve_buildings(self, context):
        return Building.objects.all()


class Mutation(graphene.ObjectType):
    create_building = CreateBuilding.Field()
    delete_building = DeleteBuilding.Field()
    update_building = UpdateBuilding.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

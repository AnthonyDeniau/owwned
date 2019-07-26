from graphene_django import DjangoObjectType
import graphene
from .models import Localization

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
    building = graphene.Field(BuildingType, id=graphene.Int(), name=graphene.String())
    buildings = graphene.List(BuildingType)

    floor = graphene.Field(FloorType, id=graphene.Int(), name=graphene.String())
    floors = graphene.List(FloorType) 

    room = graphene.Field(RoomType, id=graphene.Int(), name=graphene.String())
    rooms = graphene.List(RoomType)

    def resolve_building(self, context, id=None, name=None):
        if id is not None:
            return Building.objects.get(pk=id)

        if name is not None:
            return Building.objects.get(name=name)

        return None

    def resolve_buildings(self, context):
        return Building.objects.all()
    
    def resolve_floor(self, context, id=None, name=None):
        if id is not None:
            return Floor.objects.get(pk=id)

        if name is not None:
            return Floor.objects.get(name=name)

        return None

    def resolve_floors(self, context):
        return Floor.objects.all()

    def resolve_room(self, context, id=None, name=None):
        if id is not None:
            return Room.objects.get(pk=id)

        if name is not None:
            return Room.objects.get(name=name)

        return None

    def resolve_rooms(self, context):
        return Room.objects.all()


class CreateBuilding(graphene.Mutation):
    id = graphene.Int()
    Lat = graphene.Decimal()
    Long = graphene.Decimal()
    Name = graphene.String

    class Arguments:
        Lat = graphene.Decimal()
        Long = graphene.Decimal()
        Name = graphene.String(required=True)

    def mutate(self, info, Lat, Long, Name):
        Building = Building(Lat=Lat, Long=Long, Name=Name)
        Building.save()
        return CreateBuilding(id=Building.id,
                            Lat=Building.lat,
                            Long=Building.long,
                            name=Building.name)


    
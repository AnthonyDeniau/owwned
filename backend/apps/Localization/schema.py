from graphene_django import DjangoObjectType
import graphene
from .models import Building
from .models import Floor
from .models import Room

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
    building = graphene.Field(BuildingType, id=graphene.Int(), Name=graphene.String())
    buildings = graphene.List(BuildingType)

    floor = graphene.Field(FloorType, id=graphene.Int(), Name=graphene.String())
    floors = graphene.List(FloorType) 

    room = graphene.Field(RoomType, id=graphene.Int(), Name=graphene.String())
    rooms = graphene.List(RoomType)

    def resolve_building(self, context, id=None, Name=None):
        if id is not None:
            return Building.objects.get(pk=id)

        if Name is not None:
            return Building.objects.get(Name=Name)

        return None

    def resolve_buildings(self, context):
        return Building.objects.all()
    
    def resolve_floor(self, context, id=None, Name=None):
        if id is not None:
            return Floor.objects.get(pk=id)

        if Name is not None:
            return Floor.objects.get(Name=Name)

        return None

    def resolve_floors(self, context):
        return Floor.objects.all()

    def resolve_room(self, context, id=None, Name=None):
        if id is not None:
            return Room.objects.get(pk=id)

        if Name is not None:
            return Room.objects.get(Name=Name)

        return None

    def resolve_rooms(self, context):
        return Room.objects.all()


class CreateBuilding(graphene.Mutation):
    id = graphene.Int()
    Lat = graphene.Decimal()
    Long = graphene.Decimal()
    Name = graphene.String()

    class Arguments:
        Lat = graphene.Decimal()
        Long = graphene.Decimal()
        Name = graphene.String(required=True)

    def mutate(self, info, Lat, Long, Name):
        building = Building(Lat=Lat, Long=Long, Name=Name)
        building.save()
        return CreateBuilding(id=building.id,
                            Lat=building.Lat,
                            Long=building.Long,
                            Name=building.Name)

class Mutation(graphene.ObjectType):
    createbuilding = CreateBuilding.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
    
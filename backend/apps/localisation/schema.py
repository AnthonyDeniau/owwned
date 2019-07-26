from graphene_django import DjangoObjectType
import graphene
from .models import Batiment
from .models import Floor
from .models import Room


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class FloorType(DjangoObjectType):
    class Meta:
        model = Floor


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Decimal()
    long = graphene.Decimal()
    name = graphene.String()

    class Arguments:
        long = graphene.Decimal(required=True)
        lat = graphene.Decimal(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, long, lat, name):
        batiment = Batiment(long=long, lat=lat, name=name)
        batiment.save()
        return CreateBatiment(
            id=batiment.id,
            long=batiment.long,
            lat=batiment.lat,
            name=batiment.name)


class QueryBatiment(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None, name=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        if name is not None:
            return Batiment.objects.get(name=name)

        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Decimal()
    long = graphene.Decimal()
    name = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        long = graphene.Decimal(required=True)
        lat = graphene.Decimal(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, id, long=None, lat=None, name=None):
        batiment = Batiment.objects.get(pk=id)
        if long is not None:
            batiment.asset_id = long
        if lat is not None:
            batiment.name = lat
        if name is not None:
            batiment.description = name
        batiment.save()
        return UpdateBatiment(id=batiment.id,
                              long=batiment.long,
                              lat=batiment.lat,
                              name=batiment.name)


class DeleteBatiment(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(is_delete=True)


class DeleteFloor(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        floor = Floor.objects.get(pk=id)
        floor.delete()
        return DeleteFloor(is_delete=True)


class DeleteRoom(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        room = Room.objects.get(pk=id)
        room.delete()
        return DeleteRoom(is_delete=True)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    update_batiment = UpdateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    delete_floor = DeleteFloor.Field()
    delete_room = DeleteRoom.Field()


schema = graphene.Schema(query=QueryBatiment, mutation=Mutation)

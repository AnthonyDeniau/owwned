from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room
from asset.models import Asset

from asset.schema import AssetType


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
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)
    assetsBatiment = graphene.List(AssetType, batimentId=graphene.Int())

    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()

    def resolve_assetsBatiment(self, context, batimentId):
        # return Asset.objects.filter(Floor_id__in =  Floor.objects.filter(Room_id__in = ))
        return Asset.objects.filter(room__floor__batiment_id=batimentId)


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Float()
    longBat = graphene.Float()
    name = graphene.String()

    class Arguments:
        lat = graphene.Float()
        longBat = graphene.Float()
        name = graphene.String(required=True)

    def mutate(self, info, lat, longBat, name):
        batiment = Batiment(lat=lat, longBat=longBat, name=name)
        batiment.save()
        return CreateBatiment(id=batiment.id,
                              lat=batiment.lat,
                              longBat=batiment.longBat,
                              name=batiment.name)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Float()
    longBat = graphene.Int()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        lat = graphene.Float()
        longBat = graphene.Int()
        name = graphene.String()

    def mutate(self, info, id, lat=None, longBat=None, name=None):
        batiment = Batiment.objects.get(pk=id)
        if lat is not None:
            batiment.lat = lat
        if longBat is not None:
            batiment.longBat = longBat
        if name is not None:
            batiment.name = name

        batiment.save()
        return UpdateBatiment(lat=batiment.lat,
                              longBat=batiment.longBat,
                              name=batiment.name)

    #test


class DeleteBatiment(graphene.Mutation):
    batimentBool = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(batimentBool=True)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

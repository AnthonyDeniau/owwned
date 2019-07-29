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
                              name=graphene.String())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None, name=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        if name is not None:
            return Batiment.objects.get(name=name)

        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Float()
    lon = graphene.Float()
    name = graphene.String()

    class Arguments:
        lat = graphene.Float()
        lon = graphene.Float()
        name = graphene.String()

    def mutate(self, info, lat, lon, name):
        batiment = Batiment(lat=lat, lon=lon, name=name)
        batiment.save()
        return CreateBatiment(id=batiment.pk, lat=lat, lon=lon, name=name)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.Float()
    lon = graphene.Float()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        lat = graphene.Float()
        lon = graphene.Float()
        name = graphene.String()

    def mutate(self, info, id, lat, lon, name):
        batiment = Batiment.objects.get(pk=id)
        if lat is not None:
            batiment.lat = lat
        if lon is not None:
            batiment.lon = lon
        if name is not None:
            batiment.name = name
        batiment.save()
        return UpdateBatiment(lat=batiment.lat,
                              lon=batiment.lon,
                              name=batiment.name)


class DeleteBatiment(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        Batiment.delete()
        return DeleteBatiment(is_delete=True)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

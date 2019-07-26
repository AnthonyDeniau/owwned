from graphene_django import DjangoObjectType
import graphene
from .models import Batiment


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)
        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    longitude = graphene.Float()
    latitude = graphene.Float()

    class Arguments:
        name = graphene.String()
        longitude = graphene.Float()
        latitude = graphene.Float()

    def mutate(self, info, name, longitude, latitude):
        batiment = Batiment(name=name, longitude=longitude, latitude=latitude)
        batiment.save()
        return CreateBatiment(id=batiment.id,
                              name=batiment.name,
                              longitude=batiment.longitude,
                              latitude=batiment.latitude)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    longitude = graphene.Float()
    latitude = graphene.Float()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        longitude = graphene.Float()
        latitude = graphene.Float()

    def mutate(self, info, id, name=None, longitude=None, latitude=None):
        batiment = Batiment.objects.get(pk=id)
        if (name is not None):
            batiment.name = name
        if (longitude is not None):
            batiment.longitude = longitude
        if (latitude is not None):
            batiment.latitude = latitude
        batiment.save()
        return UpdateBatiment(id=batiment.id,
                              name=batiment.name,
                              longitude=batiment.longitude,
                              latitude=batiment.latitude)


class DeleteBatiement(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiement(is_delete=True)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    update_batiment = UpdateBatiment.Field()
    delete_batiment = DeleteBatiement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

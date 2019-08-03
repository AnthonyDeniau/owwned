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


class CreateBatiment(graphene.Mutation):

    id = graphene.ID()
    latBatiment = graphene.Float()
    longBatiment = graphene.Float()
    nameBatiment = graphene.String()

    class Arguments:
        latBatiment = graphene.Float()
        longBatiment = graphene.Float()
        nameBatiment = graphene.String()

    def mutate(self, info, latBatiment, longBatiment, nameBatiment):
        batiment = Batiment(latBatiment=latBatiment,
                            longBatiment=longBatiment,
                            nameBatiment=nameBatiment)
        batiment.save()
        return CreateBatiment(id=batiment.pk,
                              latBatiment=batiment.latBatiment,
                              longBatiment=batiment.longBatiment,
                              nameBatiment=batiment.nameBatiment)


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.ID())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()


class UpdateBatiment(graphene.Mutation):
    id = graphene.ID()
    latBatiment = graphene.Float()
    longBatiment = graphene.Float()
    nameBatiment = graphene.String()

    class Arguments:
        id = graphene.Int()
        latBatiment = graphene.Float()
        longBatiment = graphene.Float()
        nameBatiment = graphene.String()

    def mutate(self,
               info,
               id,
               latBatiment=None,
               longBatiment=None,
               nameBatiment=None):
        batiment = Batiment.objects.get(pk=id)
        if latBatiment is not None:
            batiment.latBatiment = latBatiment
        if longBatiment is not None:
            batiment.longBatiment = latBatiment
        if nameBatiment is not None:
            batiment.nameBatiment = nameBatiment

        batiment.save()
        return UpdateBatiment(latBatiment=batiment.latBatiment,
                              longBatiment=batiment.longBatiment,
                              nameBatiment=batiment.nameBatiment)


class DeleteBatiment(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        batimentId = graphene.ID(required=True)

    def mutate(self, info, batimentId):
        batiment = Batiment.objects.get(pk=batimentId)
        batiment.delete()
        return DeleteBatiment(status=True)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()


schema = graphene.Schema(mutation=Mutation, query=Query)

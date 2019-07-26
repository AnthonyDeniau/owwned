from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment



class CreateBatiment(graphene.Mutation):
    
    id = graphene.Int()
    latBatiment = graphene.Int()
    longBatiment = graphene.Int()
    nameBatiment = graphene.String()

    class Arguments:
        latBatiment = graphene.Int()
        longBatiment = graphene.Int()
        nameBatiment = graphene.String()

    def mutate(self, info, latBatiment, longBatiment, nameBatiment):
        batiment = Batiment(latBatiment=latBatiment,longBatiment=longBatiment,nameBatiment=nameBatiment)
        batiment.save()
        return CreateBatiment(latBatiment=batiment.latBatiment,
                                    longBatiment=batiment.longBatiment,
                                    nameBatiment=batiment.nameBatiment)

class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        return None


    def resolve_batiments(self, context):
        return Batiment.objects.all()

        
class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    latBatiment = graphene.Int()
    longBatiment = graphene.Int()
    nameBatiment = graphene.String()

    class Arguments:
        id = graphene.Int()
        latBatiment = graphene.Int()
        longBatiment = graphene.Int()
        nameBatiment = graphene.String()

    def mutate(self, info,id, latBatiment=None, longBatiment=None, nameBatiment=None):
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
    deleteBatimentBool = graphene.Boolean()

    class Arguments:
        batimentId = graphene.ID(required=True)

    def mutate(self, info, batimentId):
        batiment = Batiment.objects.get(pk=batimentId)
        batiment.delete()
        return DeleteBatiment(deleteBatimentBool=True)



class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()
schema = graphene.Schema(mutation=Mutation,query=Query)

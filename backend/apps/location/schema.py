import graphene
from graphene_django import DjangoObjectType
from .models import Batiment

class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment

class Query(graphene.ObjectType)
    batimentType = graphene.Field(BatimentType, id=graphene.Int())
    batimentType = graphene.List(BatimentType)

    def resolve_batimenttype(self, context, id=None):
        if id is not None:
            return BatimentType.objects.get(pk=id)

        return None

    def resolve_batimenttype(self, context):
        return BatimentType.objects.all()

class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.ID()
    long = graphene.ID()
    name = graphene.String()
    

    class Arguments:
        lat = graphene.Float()
        long = graphene.Float()
        name = graphene.String()

    def mutate(self, info, lat, long, name):
        batimentType = BatimentType(lat=lat, long=long, name=name)
        batimentType.save()
        return CreateBatiment(id=batimentType.id,
                                    lat=batimentType.lat,
                                    endDate=batimentType.long,
                                    name=batimentType.name

class Mutation(graphene.ObjectType):
    create_batimentType = CreateBatiment.Field()
    
schema = graphene.Schema(mutation=Mutation)
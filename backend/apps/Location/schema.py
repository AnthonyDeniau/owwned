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

class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)

class CreateBatiment(graphene.Mutation):
    Lat = graphene.Float()
    Long = graphene.Float()
    Name = graphene.String()

    class Arguments:
        Lat = graphene.Float()
        Long = graphene.Float()
        Name = graphene.String()
    
    def mutate(self, info):
        batiment = Batiment(Lat=Lat, Long=Long, Name=Name)
        batiment.save()
        return CreateBatiment(Lat=batiment.Lat, Long=batiment.Long, Name=batiment.name)

class Mutation(graphene.ObjectType):
    create_Batiment = CreateBatiment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
from graphene_django import DjangoObjectType
import graphene
from Location import Batiment

class CreateBatiment(graphene.Mutation):
    Lat = graphene.DecimalField()
    Long = graphene.DecimalField()
    Name = graphene.String()

    class Arguments:
        Lat = graphene.types.DecimalField()
        Long = graphene.types.DecimalField()
        Name = graphene.String()
    
    def mutate(self, info):
        batiment = Location.Batiment(Lat=Lat, Long=Long, Name=Name)
        batiment.save()
        return CreateBatiment(Lat=batiment.Lat, Long=batiment.Long, Name=batiment.name)

from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Floor, Room

class BatimentType(DjangoObjectType):   
    class Meta:
        model = Batiment

class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    lat = graphene.Decimal()
    long = graphene.Decimal()

    class Arguments:
        name = graphene.String()
        lat = graphene.Decimal()
        long = graphene.Decimal()

    def mutate(self, info, name, lat, long):
        batiment = Batiment(name=name, long=long, lat=lat)
        batiment.save()
        return CreateBatiment(name=batiment.name,
                            lat=batiment.lat,
                            long=batiment.long)

class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    lat = graphene.Decimal()
    long = graphene.Decimal()

    class Arguments:
        name = graphene.String()
        lat = graphene.Decimal()
        long = graphene.Decimal()

    def mutate(self, info, id, name, lat, long):
        batiment = Batiment.objects.get(pk=id)
        batiment.name = name
        batiment.lat = lat
        batiment.long = long
        batiment.save()
        
        return UpdateBatimen(id = batiment.id,
                            name=batiment.name,
                            lat=batiment.lat,
                            long=batiment.long)

class DeleteBatiment(graphene.Mutation):
    status = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(
            status=True
        )

class FloorType(DjangoObjectType):   
    class Meta:
        model = Floor

class CreateFloor(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    batiment = graphene.Field(BatimentType)
   
    class Arguments:
        name = graphene.String()
        batiment = graphene.ID()

    def mutate(self, info, name, batiment):
        floor = Floor(name=name, batiment=batiment)
        floor.save()
        return CreateFloor(name=name, batiment=batiment)   

class UpdateFloor(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    batiment = graphene.Field(BatimentType)
   

    class Arguments:
        name = graphene.String()
        batiment = graphene.ID()

    def mutate(self, info, id, name, batiment):
        floor = Floor.objects.get(pk=id)
        floor.name = name
        floor.batiment = batiment
        floor.save()
        
        return UpdateBatimen(id = floor.id,
                            name=name, 
                            batiment=batiment)

class DeleteFloor(graphene.Mutation):
    status = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        floor = Floor.objects.get(pk=id)
        floor.delete()
        return DeleteFloor(
            status=True
        )

class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()
    create_floor = CreateFloor.Field()
    delete_floor = DeleteFloor.Field()
    update_floor = UpdateFloor.Field()

class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int())
    batiments = graphene.List(BatimentType)
    floor = graphene.Field(FloorType, id=graphene.Int())
    floors = graphene.List(FloorType)
    
    def resolve_batiment(self, context, id=None):
        if id is not None:
            return Batiment.objects.get(pk=id)
    
    def resolve_batiments(self, context):
        return Batiment.objects.all()

    def resolve_floor(self, context, id=None):
        if id is not None:
            return Floor.objects.get(pk=id)
    
    def resolve_floor(self, context):
        return Floor.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
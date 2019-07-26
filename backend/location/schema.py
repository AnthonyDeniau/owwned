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
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String(), long=graphene.Decimal(), lat=graphene.Decimal())
    batiments = graphene.List(BatimentType)

    def resolve_batiment(self, context, id=None, name=None, long=None, lat=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        if name is not None:
            return Batiment.objects.get(name=name)

        return None

    def resolve_teams(self, context):
        return Batiment.objects.all()


class CreateBatiment (graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    lat = graphene.Decimal()
    long = graphene.Decimal()

    class Arguments :
        name = graphene.String(required=True)
        lat = graphene.Decimal()
        long = graphene.Decimal()

    def mutate (self, info, name, lat, long) :
        batiment = Batiment(name=name, lat = lat, long=long)
        batiment.save()
        return CreateBatiment(id = batiment.pk,
                              name = batiment.name,
                              lat = batiment.lat,
                              long = batiment.long)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    lat = graphene.Decimal()
    long = graphene.Decimal()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        lat = graphene.Decimal()
        long = graphene.Decimal()
    
    def mutate(self,info,id,name,lat,long):
        batiment = Batiment.objects.get(pk=id)
        batiment.name = name
        batiment.lat = lat
        batiment.long = long
        batiment.save()
        return UpdateBatiment(id,name,lat,long)

class DeleteBatiment(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
    
    def mutate(self,info,id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(is_delete=True)



class Mutation (graphene.ObjectType):
    create_Batiment = CreateBatiment.Field()
    update_Batiment = UpdateBatiment.Field()
    delete_Batiment = DeleteBatiment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
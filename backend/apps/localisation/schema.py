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


class BatimentQuery(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String())
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
    name = graphene.String()
    lat = graphene.Decimal()
    lng = graphene.Decimal()

    class Arguments:        
        name = graphene.String()
        lat = graphene.Decimal()
        lng = graphene.Decimal()

    def mutate(self, info, name, lat, lng):
        batiment = Batiment(name=name, lat=lat, lng=lng)
        batiment.save()
        return CreateBatiment(id=batiment.id,
                                name=batiment.name,
                                lat=batiment.lat,
                                lng=batiment.lng)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    lat = graphene.Decimal()
    lng = graphene.Decimal()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        lat = graphene.Decimal()
        lng = graphene.Decimal()

    def mutate(self, info, id, name=None, lat=None, lng=None):
        batiment = Batiment.objects.get(pk=id)
         
        if name is not None:
            batiment.name = name

        if lat is not None:
            batiment.lat = lat

        if lng is not None:
            batiment.lng = lng

        batiment.save()
        return UpdateBatiment(  id=batiment.id,
                                name=batiment.name,
                                lat=batiment.lat,
                                lng=batiment.lng)


class DeleteBatiment(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(is_delete=True)


class BatimentMutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    update_batiment = UpdateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()

schema = graphene.Schema(query=BatimentQuery, mutation=BatimentMutation);

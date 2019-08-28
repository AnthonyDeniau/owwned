from graphene_django import DjangoObjectType
import graphene
from .models import Batiment, Etage, Piece
from organization.schema import OrganizationType


class BatimentType(DjangoObjectType):
    class Meta:
        model = Batiment


class EtageType(DjangoObjectType):
    class Meta:
        model = Etage


class PieceType(DjangoObjectType):
    class Meta:
        model = Piece


class Query(graphene.ObjectType):
    batiment = graphene.Field(BatimentType, id=graphene.Int(), name=graphene.String())
    batiments = graphene.List(BatimentType)
    etage = graphene.Field(EtageType, id=graphene.Int())
    etages = graphene.List(EtageType)
    piece = graphene.Field(PieceType, id=graphene.Int())
    pieces = graphene.List(PieceType)

    def resolve_batiment(self, context, id=None, name=None):
        if id is not None:
            return Batiment.objects.get(pk=id)

        if name is not None:
            return Batiment.objects.get(name=name)

        return None

    def resolve_batiments(self, context):
        return Batiment.objects.all()

    def resolve_etage(self, context, id=None, name=None):
        if id is not None:
            return Etage.objects.get(pk=id)

        return None

    def resolve_etages(self, context):
        return Etage.objects.all()

    def resolve_piece(self, context, id=None, name=None):
        if id is not None:
            return Piece.objects.get(pk=id)

        return None

    def resolve_pieces(self, context):
        return Piece.objects.all()


class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    long = graphene.Float()
    lat = graphene.Float()

    class Arguments:
        name = graphene.String(required=True)
        long = graphene.Float(required=True)
        lat = graphene.Float(required=True)

    def mutate(self, info, name, long, lat):
        batiment = Batiment(name=name, long=long, lat=lat)
        batiment.save()
        return CreateBatiment(id=batiment.id,
                              name=batiment.name,
                              long=batiment.long,
                              lat=batiment.lat)


class DeleteBatiment(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        batiment = Batiment.objects.get(pk=id)
        batiment.delete()
        return DeleteBatiment(is_delete=True)


class UpdateBatiment(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    long = graphene.Float()
    lat = graphene.Float()

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        long = graphene.Float()
        lat = graphene.Float()

    def mutate(self, info, id, name=None, long=None, lat=None):
        batiment = Batiment.objects.get(pk=id)
        if name is not None:
            batiment.name = name
        if long is not None:
            batiment.long = long
        if lat is not None:
            batiment.lat = lat
        batiment.save()
        return UpdateBatiment(id, name, long, lat)


class Mutation(graphene.ObjectType):
    create_batiment = CreateBatiment.Field()
    delete_batiment = DeleteBatiment.Field()
    update_batiment = UpdateBatiment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

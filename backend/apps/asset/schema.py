from graphene_django import DjangoObjectType
import graphene
from .models import Asset
from supplier.schema import SupplierType


class AssetType(DjangoObjectType):
    class Meta:
        model = Asset


class Query(graphene.ObjectType):
    asset = graphene.Field(AssetType, id=graphene.Int(), name=graphene.String(), description=graphene.String(), cost=graphene.Float())
    assets = graphene.List(AssetType)

    def resolve_asset(self, context, id=None, name=None):
        if id is not None:
            return Asset.objects.get(pk=id)

        if name is not None:
            return Asset.objects.get(name=name)

        return None

    def resolve_assets(self, context):
        return Asset.objects.all()

class CreateAsset(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    cost = graphene.Float()
    supplier = graphene.Field(SupplierType)

    class Arguments: 
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        cost = graphene.Float()
        supplier =  graphene.ID()
    
    def mutate(self, info, name, description, cost, supplier):
        asset = Asset(name=name, description=description, cost=cost, supplier_id=supplier)
        asset.save()
        return CreateAsset(id=asset.id, name=asset.name, supplier=asset.supplier) 

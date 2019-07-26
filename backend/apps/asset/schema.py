from graphene_django import DjangoObjectType
import graphene
from .models import Asset
from organization.schema import OrganizationType


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

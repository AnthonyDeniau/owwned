from graphene_django import DjangoObjectType
import graphene
from .models import Supplier
from organization.schema import OrganizationType


class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier
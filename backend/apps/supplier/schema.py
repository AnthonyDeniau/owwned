from graphene_django import DjangoObjectType
import graphene
from .models import Supplier

class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier


class CreateSupplier(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    login = graphene.String()
    password = graphene.String()
    webSite = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        login = graphene.String()
        password = graphene.String()
        webSite = graphene.String()

    def mutate(self, info, name, login, password, webSite):
        supplier = Supplier(name=name, login=login, password=password, webSite=webSite)
        supplier.save()
        return CreateSupplier(name=supplier.name,
                              login=supplier.login,
                              password=supplier.password,
                              webSite=supplier.webSite)

class Query(graphene.ObjectType):
    supplier = graphene.Field(SupplierType, id=graphene.Int())
    suppliers = graphene.List(SupplierType)

    def resolve_supplier(self, context, id=None):
        if id is not None:
            return Supplier.objects.get(pk=id)
    
    def resolve_suppliers(self, context):
        return Suppliers.objects.all()


class Mutation(graphene.ObjectType):
    create_supplier = CreateSupplier.Field()


schema = graphene.Schema(mutation=Mutation)

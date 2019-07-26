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
        return Supplier.objects.all()


class DeleteSupplier(graphene.Mutation):
    status = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        supplier = Supplier.objects.get(pk=id)
        supplier.delete()
        return DeleteSupplier(
            status=True
        )


class UpdateSupplier(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    login = graphene.String()
    password = graphene.String()
    webSite = graphene.String()

    class Arguments:
        id = graphene.ID(required = True)
        name = graphene.String(required=True)
        login = graphene.String()
        password = graphene.String()
        webSite = graphene.String()

    def mutate(self, info, id, name, login, password, webSite):
        supplier = Supplier.objects.get(pk=id)
        supplier.name = name
        supplier.login = login
        supplier.password = password
        supplier.webSite = webSite        
        supplier.save()
        return UpdateSupplier(id = supplier.id,
                              name=supplier.name,
                              login=supplier.login,
                              password=supplier.password,
                              webSite=supplier.webSite)


class Mutation(graphene.ObjectType):
    create_supplier = CreateSupplier.Field()
    delete_supplier = DeleteSupplier.Field()
    update_supplier = UpdateSupplier.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

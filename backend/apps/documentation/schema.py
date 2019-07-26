from graphene_django import DjangoObjectType
import graphene
from .models import Documentation

class DocumentationType(DjangoObjectType):
    class Meta:
        model = Documentation

class Query(graphene.ObjectType):
    documentation = graphene.Field(DocumentationType, id=graphene.Int(), name=graphene.String())
    documentations = graphene.List(DocumentationType)

    def resolve_documentation(self, context, id=None, name=None):
        if id is not None:
            return Documentation.objects.get(pk=id)

        if name is not None:
            return Documentation.objects.get(name=name)

        return None

    def resolve_documentations(self, context):
        return Documentation.objects.all()

schema = graphene.Schema(query=Query)
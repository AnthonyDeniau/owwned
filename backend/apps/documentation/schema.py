from graphene_django import DjangoObjectType
import graphene
from .models import Documentation


class DocumentationType(DjangoObjectType):
    class Meta:
        model = Documentation


class Query(graphene.ObjectType):
    is_query = graphene.Boolean()


class DeleteDocumentation(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        documentation = Documentation.objects.get(pk=id)
        documentation.delete()
        return DeleteDocumentation(is_delete=True)


class Mutation(graphene.ObjectType):
    deleteDocumentation = DeleteDocumentation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

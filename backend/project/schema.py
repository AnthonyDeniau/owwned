import graphene
import organization


class Query(organization.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
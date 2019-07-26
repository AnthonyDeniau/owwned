import graphene
import organization.schema
import team.schema
import documentation.schema


class Query(organization.schema.Query, documentation.schema.Query, team.schema.Query, graphene.ObjectType):
    pass


class Mutation(team.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
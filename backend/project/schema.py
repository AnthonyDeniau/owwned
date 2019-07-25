import graphene
import organization.schema
import team.schema


class Query(organization.schema.Query, team.schema.Query, graphene.ObjectType):
    pass


class Mutation(team.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
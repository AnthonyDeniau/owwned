import graphene
import organization.schema
import team.schema
import historyevent.schema


class Query(organization.schema.Query, team.schema.Query, historyevent.schema.Query, graphene.ObjectType):
    pass


class Mutation(team.schema.Mutation, historyevent.schema.Mutation graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
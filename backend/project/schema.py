import graphene
import organization.schema
import team.schema
import profiles.schema


class Query(organization.schema.Query, team.schema.Query, profiles.schem.Query,
            graphene.ObjectType):
    pass


class Mutation(team.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
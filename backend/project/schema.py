import graphene
import organization.schema
import team.schema
import asset.schema
import documentation.schema


class Query(organization.schema.Query, team.schema.Query, asset.schema.Query,
            profiles.schema.Query, documentation.schema.Query, graphene.ObjectType):
    pass


class Mutation(team.schema.Mutation, documentation.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

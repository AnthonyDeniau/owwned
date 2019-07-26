import graphene
import organization.schema
import team.schema
import asset.schema
import documentation.schema
import profiles.schema
import supplier.schema


class Query(organization.schema.Query, team.schema.Query, asset.schema.Query,
            profiles.schema.Query, documentation.schema.Query, graphene.ObjectType):
    pass


class Mutation(supplier.schema.Mutation, team.schema.Mutation, documentation.schema.Mutation, profiles.schema.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

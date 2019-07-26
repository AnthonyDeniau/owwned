import graphene
import organization.schema
import team.schema
import asset.schema
import documentation.schema
import profiles.schema
import supplier.schema
import historyevent.schema
import location.schema


class Query(organization.schema.Query, team.schema.Query, asset.schema.Query,
            profiles.schema.Query, documentation.schema.Query, historyevent.schema.Query, supplier.schema.Query, location.schema.Query, graphene.ObjectType):

    pass

class Mutation(supplier.schema.Mutation,team.schema.Mutation, documentation.schema.Mutation, historyevent.schema.Mutation, profiles.schema.Mutation, location.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

from graphene_django import DjangoObjectType
import graphene
from .models import Documentation

class CreateDocumentation(graphene.Mutation):
    id = graphene.Int()
    asset = graphene.Field(AssetType)
    name = graphene.String()
    description = graphene.String()
    url = graphene.String()
    docfile = graphene.String()

    class Arguments:        
        asset = graphene.ID()
        name = graphene.String(required=True)
        description = graphene.String()
        url = graphene.String()
        docfile = graphene.String()

    def mutate(self, info, asset, name, description, url, docfile):
        documentation = Documentation(asset_id=asset, name=name, description=description, url=url, docfile=docfile)
        documentation.save()
        return CreateDocumentation(id=documentation.id,
                                    asset=documentation.asset,
                                    name=documentation.name,
                                    description=documentation.description,
                                    url=documentation.url,
                                    docfile=documentation.docfile)


class Mutation(graphene.ObjectType):
    create_documentation = CreateDocumentation.Field()


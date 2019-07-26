from graphene_django import DjangoObjectType
import graphene
from .models import HistoryEvent
from asset.schema import AssetType

class HistoryEventType(DjangoObjectType):
    class Meta:
        model = HistoryEvent

class CreateHistoryEvent(graphene.Mutation):
    id = graphene.Int()
    user = graphene.ID()
    asset = graphene.ID()
    startDate = graphene.types.datetime.DateTime()
    endDate = graphene.types.datetime.DateTime()
    typeEvent = graphene.String()
    description = graphene.String()

    class Arguments:
        user = graphene.ID(required=True)
        asset = graphene.ID()
        startDate = graphene.types.datetime.DateTime(required=True)
        endDate = graphene.types.datetime.DateTime()
        typeEvent = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, user, asset, startDate, endDate, typeEvent, description):
        historyEvent = HistoryEvent(user_id=user,asset_id=1, startDate=startDate, endDate=endDate, typeEvent=typeEvent, description=description)
        historyEvent.save()
        return CreateHistoryEvent(id=historyEvent.id,
                                    startDate=historyEvent.startDate,
                                    endDate=historyEvent.endDate,
                                    typeEvent=historyEvent.typeEvent,
                                    description=historyEvent.description)

class Mutation(graphene.ObjectType):
    create_historyevent = CreateHistoryEvent.Field()
schema = graphene.Schema(mutation=Mutation)





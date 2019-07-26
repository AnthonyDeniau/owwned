from graphene_django import DjangoObjectType
import graphene
from .models import HistoryEvent
from asset.schema import AssetType

class HistoryEventType(DjangoObjectType)
    class Meta:
        model = HistoryEvent

class CreateHistoryEvent(graphene.Mutation):
    Id = graphene.Int()
    user = graphene.ID()
    asset = graphene.ID()
    startDate = graphene.types.datetime.DateTime()
    endDate = graphene.types.datetime.DateTime()
    typeEvent = graphene.String()
    description = graphene.String()

    class Arguments
        user = graphene.ID(required=True)
        asset = graphene.ID(required=True)
        startDate = graphene.types.datetime.DateTime(required=True)
        endDate = graphene.types.datetime.DateTime()
        typeEvent = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, user, asset, startDate, endDate, typeEvent, description):
        historyEvent = HistoryEvent(user=user, asset=asset, startDate=startDate, endDate=endDate, typeEvent=typeEvent, description=description)
        HistoryEvent.save()
        return CreateHistoryEvent(id=historyEvent.id,
                                    user=historyEvent.user,
                                    asset=historyEvent.asset,
                                    startDate=historyEvent.startDate,
                                    endDate=historyEvent.endDate,
                                    typeEvent=historyEvent.typeEvent,
                                    description=historyEvent.description)


class Deletehistoryevent(graphene.Mutation):
    return False

class Mutation(graphene.ObjectType):
    create_historyevent = CreateHistoryEvent.Field()
    delete_historyevent = Deletehistoryevent.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)





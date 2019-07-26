from graphene_django import DjangoObjectType
import graphene
from .models import HistoryEvent
from asset.schema import AssetType

class HistoryEventType(DjangoObjectType):
    class Meta:
        model = HistoryEvent

class Query(graphene.ObjectType):
    historyEvent = graphene.Field(HistoryEventType, id=graphene.Int())
    historyEvents = graphene.List(HistoryEventType)
    def resolve_historyEvent(self, context, id=None):
        if id is not None:
            return HistoryEvent.objects.get(pk=id)

        return None

    def resolve_historyEvents(self, context):
        return HistoryEvent.objects.all()

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

class UpdateHistoryEvent(graphene.Mutation):
    id = graphene.Int()
    user = graphene.ID()
    asset = graphene.ID()
    startDate = graphene.types.datetime.DateTime()
    endDate = graphene.types.datetime.DateTime()
    typeEvent = graphene.String()
    description = graphene.String()

    class Arguments:
        id = graphene.Int()
        user = graphene.ID()
        asset = graphene.ID()
        startDate = graphene.types.datetime.DateTime()
        endDate = graphene.types.datetime.DateTime()
        typeEvent = graphene.String()
        description = graphene.String()

    def mutate(self, info, id,user=None , asset=None, startDate=None, endDate=None, typeEvent=None, description=None):
        historyEvent = HistoryEvent.objects.get(pk=id)
        if user is not None:
            historyEvent.user = user
        if asset is not None:
            historyEvent.asset = asset 
        if startDate is not None:
            historyEvent.startDate = startDate
        if endDate is not None:
            historyEvent.endDate = endDate
        if typeEvent is not None:
            historyEvent.typeEvent = typeEvent
        if description is not None:
            historyEvent.description = description

        historyEvent.save()
        return UpdateHistoryEvent(user=historyEvent.user,
                                    asset=historyEvent.asset,
                                    startDate=historyEvent.startDate,
                                    endDate=historyEvent.endDate,
                                    typeEvent=historyEvent.typeEvent,
                                    description=historyEvent.description)
    #test


class DeleteHistoryEvent(graphene.Mutation):
    historyEventBool = graphene.Boolean()

    class Arguments:
        historyEventId = graphene.ID(required=True)

    def mutate(self, info, historyEventId):
        historyEvent = HistoryEvent.objects.get(pk=historyEventId)
        historyEvent.delete()
        return DeleteHistoryEvent(historyEventBool=True)



class Mutation(graphene.ObjectType):
    create_historyevent = CreateHistoryEvent.Field()
    delete_historyevent = DeleteHistoryEvent.Field()
    update_historyevent = UpdateHistoryEvent.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)





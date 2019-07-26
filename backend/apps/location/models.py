from django.db import models

class Batiment(models.Model):
    lat = models.DecimalField()
    long = models.DecimalField()
    name = models.CharField(max_length = 30)

class CreateBatiment(graphene.Mutation):
    id = graphene.Int()
    lat = graphene.ID()
    long = graphene.ID()
    name = graphene.String()
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
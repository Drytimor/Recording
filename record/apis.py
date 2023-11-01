from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from record.models import PaymentTariffChoices, StatusOpeningChoices, Events
from record.selectors.home import events_category


class EventsListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=255)
        date_event = serializers.DateField()
        start_time = serializers.TimeField()
        end_time = serializers.TimeField()
        status_tariff = serializers.ChoiceField(choices=PaymentTariffChoices.choices)
        status_opening = serializers.ChoiceField(choices=StatusOpeningChoices.choices,
                                                 default=StatusOpeningChoices.OPEN)
        limit_clients = serializers.IntegerField()
        quantity_clients = serializers.IntegerField(default=0)
        price_event = serializers.DecimalField(max_digits=10,
                                               decimal_places=2)

    def get(self, request):
        events = events_category()
        data = self.OutputSerializer(events, many=True).data
        return Response(data)

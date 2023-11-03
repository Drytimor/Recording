from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from record.models import PaymentTariffChoices, StatusOpeningChoices
from record.selectors.events import events_category


class EventsListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSetSerializer(serializers.Serializer):
        activitys = serializers.CharField()
        tariff = serializers.CharField()
        open = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        organization__name = serializers.CharField()
        name = serializers.CharField()
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
        filter_serializer = self.FilterSetSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        events = events_category(filters=filter_serializer.validated_data).qs
        data = self.OutputSerializer(events, many=True).data
        return Response(data)


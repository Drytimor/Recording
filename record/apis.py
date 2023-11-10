from rest_framework.pagination import LimitOffsetPagination
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from record.models import PaymentTariffChoices, StatusOpeningChoices
from record.selectors.events import events_category


class EventsListApi(APIView):

    class Pagination(LimitOffsetPagination):
        def get_paginated_response(self, data):
            return Response(OrderedDict([
                ('count', self.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
                ('results', data),
                ('page_links', self.get_html_context().get('page_links'))
            ]))

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
        events = events_category(filters=request.query_params)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=events,
            request=request,
            view=self
        )


def get_paginated_response(*, pagination_class, serializer_class, queryset, request, view):
    paginator = pagination_class()
    page = paginator.paginate_queryset(queryset, request, view=view)
    if page is not None:
        serializer = serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)

    return Response(data=serializer.data)

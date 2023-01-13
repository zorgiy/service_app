from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializers


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        'service',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email'))
    )
    serializer_class = SubscriptionSerializers

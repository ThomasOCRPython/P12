from rest_framework import viewsets
from . import serializers, models
from rest_framework.permissions import IsAuthenticated
from contracts.permissions import IsManagementOrSaleOrSupportInContractView


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsManagementOrSaleOrSupportInContractView]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ContractSerializer

    def get_queryset(self):
        return models.Contract.objects.filter()

    def create(self, request, *args, **kwargs):

        request.POST._mutable = True
        request.data["sales_contact"] = request.user.pk
        request.POST._mutable = False
        return super(ContractViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        request.POST._mutable = True
        request.data["sales_contact"] = request.user.pk
        request.POST._mutable = False
        return super(ContractViewSet, self).update(request, *args, **kwargs)

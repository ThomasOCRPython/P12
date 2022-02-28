from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from events import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated




class EventViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,permissions.IsManagementOrSaleOrSupportInEventView]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.EventSerializer
    

    def get_queryset(self):

        user_type = self.request.user.user_type

        if user_type == 'SUPPORT':
            return models.Event.objects.filter(support_contact=self.request.user).distinct()
        return models.Event.objects.all()


    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        request.data["contracts"] = self.kwargs['contracts_pk']
        print (request.data["event_status"],'nnnnnnnnnnnnnnnnnnnnnnnnnn')
        
        request.POST._mutable = False
        return super(EventViewSet, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
       
        request.POST._mutable = True
        request.data["contracts"] = self.kwargs['contracts_pk']
        request.POST._mutable = False
        return super(EventViewSet, self).update(request, *args, **kwargs)

class EventStatusViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.EventStatusSerializer
    

    def get_queryset(self):
        
        return models.EventStatus.objects.all()

    

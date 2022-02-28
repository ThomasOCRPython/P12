from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from clients import serializers, models
from rest_framework.permissions import IsAuthenticated
from clients.permissions import IsManagementOrSaleOrSupportInClientView
from django.shortcuts import get_object_or_404
from events.models import Event
from accounts.models import User




class ClientViewSet(viewsets.ModelViewSet):
    
    
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ClientSerializer
    permission_classes = [IsAuthenticated, IsManagementOrSaleOrSupportInClientView]

    

    def get_queryset(self):
        
        
        user_type = self.request.user.user_type
        if user_type == 'SUPPORT':
            return models.Client.objects.filter(event__support_contact=self.request.user).distinct()
        return models.Client.objects.all()


    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        request.data["sale_user"] = request.user.pk
        print(request.data["sale_user"] , request.user.pk,11111111111,request.user.user_type)
        request.POST._mutable = False

        
        return super(ClientViewSet, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        print (request.data,444444444444444444444444444444444444)
        request.data["sale_user"] = request.user.pk
        request.POST._mutable = False
        return super(ClientViewSet, self).update(request, *args, **kwargs)
from contracts.models import Contract
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist 
from events import models
from contracts.models import Contract

class IsContractAuthor(permissions.BasePermission):
    def is_contract_author(self, pk, user):
        
        try:
            content =  Contract.objects.get(pk=pk)
            print(content.sales_contact.id)
        except ObjectDoesNotExist:
            return False
        return content.sales_contact.id == user



class IsAuthor(permissions.BasePermission):
    def is_author(self,pk, user):
        try:
            content = models.Event.objects.get(pk=pk)
                  
        except ObjectDoesNotExist:
            return False
        return content.support_contact.id == user


class IsManagementOrSaleOrSupportInEventView( IsAuthor,IsContractAuthor):

    def has_permission(self, request, view):
        
        user= request.user
        if view.action == "destroy":
            return False
        if view.action == "create":
            return user.user_type == "SALE" or user.user_type == "MANAGEMENT"
        if view.action == "update":
            print(view.kwargs)

            return self.is_author(view.kwargs["pk"], request.user.id) or user.user_type == "MANAGEMENT" or self.is_contract_author(view.kwargs["contracts_pk"],request.user.id)
        return True
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from contracts import models


class IsAuthor(permissions.BasePermission):
    def is_author(self, pk, user):
        try:
            content = models.Contract.objects.get(pk=pk)

        except ObjectDoesNotExist:
            return True
        return content.sales_contact.id == user


class IsManagementOrSaleOrSupportInContractView(IsAuthor):
    def has_permission(self, request, view):

        user = request.user
        if view.action == "destroy":
            return False
        if view.action == "create":
            return user.user_type == "SALE" or user.user_type == "MANAGEMENT"
        if view.action == "update":

            return (
                self.is_author(view.kwargs["pk"], request.user.id)
                or user.user_type == "MANAGEMENT"
            )
        return True

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_nested import routers
from clients.views import ClientViewSet
from events.views import EventViewSet
from contracts.views import ContractViewSet


clients_router = routers.SimpleRouter(trailing_slash=False)
clients_router.register(r"client/?", ClientViewSet, basename="client")

contracts_router = routers.NestedSimpleRouter(
    clients_router, r"client/?", lookup="project"
)
contracts_router.register(r"contracts/?", ContractViewSet, basename="contracts")

events_router = routers.NestedSimpleRouter(
    contracts_router, r"contracts/?", lookup="contracts"
)
events_router.register(r"events", EventViewSet, basename="events")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(clients_router.urls)),
    path("", include(contracts_router.urls)),
    path("", include(events_router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="login"),
]

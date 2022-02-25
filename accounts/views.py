
from rest_framework import viewsets
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# class UserViewset(viewsets.ModelViewSet):

#     permission_classes = [IsAuthenticated]

#     http_method_names = ["get", "post", "put", "delete"]
#     serializer_class = UserSerializer

    
#     def get_queryset(self, request, queryset):
#         if request.user.is_superuser:
#             return super().queryset(request, queryset)

#     def create(self, request, *args, **kwargs):
        
#         request.POST._mutable = True
#         request.data["project"] = self.kwargs["project_pk"]
#         request.POST._mutable = False
#         return super(UserViewset, self).create(request, *args, **kwargs)
class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )
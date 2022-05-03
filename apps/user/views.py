from rest_framework import viewsets
from rest_framework import permissions

from apps.user.models import User
from apps.user.serializers import UserSerializer, UserSerializerList


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserSerializer
        return UserSerializerList

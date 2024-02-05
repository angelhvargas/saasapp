from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from saas_app.api.v1 import serializer as serializers
from saas_app.users.models import User


class CurrentUserView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = serializers.UserSerializer(request.user, data=request.data)
        if request.data and serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

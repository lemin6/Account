from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [permissions.IsAuthenticated]

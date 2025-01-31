from rest_framework import viewsets
from .serializers import *
from .models import *

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

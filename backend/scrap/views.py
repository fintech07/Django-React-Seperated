from rest_framework import generics

from .models import Scrap
from .serializers import ScrapSerializer

class ListScrap(generics.ListCreateAPIView):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer

class DetailScrap(generics.RetrieveUpdateDestroyAPIView):
    qeuryset = Scrap.objects.all()
    serializer_class = ScrapSerializer

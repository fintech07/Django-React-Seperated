from rest_framework import serializers
from .models import Scrap

class ScrapSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Scrap
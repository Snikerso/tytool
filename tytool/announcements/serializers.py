
from rest_framework import serializers
from .models import AnnouncmentsScienceTool




class AnnouncmentsScienceToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncmentsScienceTool
        fields = ['id','title']
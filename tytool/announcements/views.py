
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import AnnouncmentsScienceTool
from .serializers import AnnouncmentsScienceToolSerializer
from rest_framework import status


class  AnnouncmentsScienceToolViewSet(viewsets.ModelViewSet):
        queryset = AnnouncmentsScienceTool.objects.all()
        serializer_class = AnnouncmentsScienceToolSerializer
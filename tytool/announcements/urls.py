from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import  AnnouncmentsScienceToolViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'announcements',AnnouncmentsScienceToolViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

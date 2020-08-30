from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

class AnnouncmentsScienceTool(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    description = models.TextField(max_length=32,blank=False,null=False)
    announcementType = models.TextField(default=False , max_length=4,blank=False,null=False)
    author =  models.ForeignKey(get_user_model(),to_field='username', on_delete=models.CASCADE)
    createAt = models.DateTimeField(default=timezone.now)
    isWorker = models.BooleanField(default=False)
    isHelper = models.BooleanField(default=False)
    isPayment = models.BooleanField(default=False)
    timeToEnd = models.CharField(default=False, max_length=20, blank=True)
    place = models.CharField(default=False , max_length=30)
    tags = models.TextField(default=False , max_length=100,blank=True)
    linkFirstName =  models.CharField(default=False, max_length=20, blank=True)
    linkFirst = models.TextField(default=False , max_length=100,blank=True)
    linkSecond = models.TextField(default=False , max_length=100,blank=True)
    linkSecondName =  models.CharField(default=False, max_length=20, blank=True)
    
    # zapisani użytkownicy 
    # ulubione
    # zainteresowani
    # opis1 , opis2 , opis3 
    # tak sie zastanaiwam czy kazdy typ Announcment science tool powinien miec osobny model
    
    
    
    def __str__(self):
        return self.title



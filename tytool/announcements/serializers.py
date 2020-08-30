
from rest_framework import serializers
from .models import AnnouncmentsScienceTool
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only':True, 'required':True}} # To robi tak że nie pobiera passwordu przy zapytaniu ale jest konieczny do założenia nowego
        
    def create(self,validated_data): 
        user = User.objects.create_user(**validated_data) 
        Token.objects.create(user=user) # tworzy token dla każdaego użytkownika
        return user

class AnnouncmentsScienceToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncmentsScienceTool
        fields = '__all__'
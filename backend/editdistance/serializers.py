from django.contrib.auth.models import User,  Group

from rest_framework import serializers
from .models import EditDistanceWords


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EditDistanceWords
        fields = ['word_one', 'word_two', 'word_one_calc', 'word_two_calc', 'distance']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import EditDistanceWords
from .serializers import WordsSerializer, GroupSerializer, UserSerializer


class EditDistanceWordsViewSet(viewsets.ModelViewSet):
    queryset = EditDistanceWords.objects.all()
    serializer_class = WordsSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

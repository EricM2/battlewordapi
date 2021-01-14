from django.contrib.auth.models import User, Group
from .models import Word, Subscriber
from rest_framework import serializers


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'hint', 'stage']


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'date']
from rest_framework import viewsets

from .serializers import WordSerializer,SubscriberSerializer
from .models import Word,Subscriber
from datetime import datetime
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import uuid
import json
import random



@csrf_exempt
@api_view(['POST'])
def addWord(request):
    print(request.headers)
    data = JSONParser().parse(request)
    print(data)
    serializer = WordSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
def addSubscriber(request):
    data = JSONParser().parse(request)
    now = datetime.now()
    dateJoined= {"date":now}
    data.update(dateJoined)
    serializer = SubscriberSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)



@api_view()
def listWord(request,stage,limit,language):
    words = Word.objects.filter(stage=stage).filter(lang_code=language)
    
    serializer = WordSerializer(words, many=True)
    data = serializer.data
    print(type(data))
    random.shuffle(data)
    print(type(data))
    top10 = []
    if(len(data) > 10):
        top10 = data[:10]
    else:
        top10 = data
    print(type(top10))
    return JsonResponse(top10, safe=False)


@api_view()
def listSubscriber(request):
    subscribers = Subscriber.objects.all()
    serializer = SubscriberSerializer(subscribers, many=True)
    return JsonResponse(serializer.data, safe=False)



    

    
    










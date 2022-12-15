import numbers
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from PIL import Image    
import requests
import threading
import time
# Create your views here.

def homepage(request):

    # print)
    return render(request, 'Emails.html')

def proxy(request):
    return render(request, 'proxies.html')

def user(request):
    
    return render(request, 'users.html')
# baibars313Rajput

  
@api_view(['GET','POST'])
def allItems(request):
    if request.method=="GET":
        if request.GET.get("category")=='all':
            allob=Items.objects.all()
            serialized=Itemserializer(allob, many=True)
            return Response(serialized.data)
        else:
            cat=request.GET.get("category")
            print(cat)
            allob=Items.objects.filter(category=cat)
            serialized=Itemserializer(allob, many=True)
            return Response(serialized.data)


    if request.method=="POST":
        serializer = Itemserializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"200"})
        else:
            return Response({"failed":"faild"})

@api_view(['GET'])
def allItemsbyaddress(request):
    if request.method=="GET":
        cat=request.GET.get("address")
        print(cat)
        allob=Items.objects.filter(owner=cat)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def allItemsauction(request):
    if request.method=="GET":
        allob=Items.objects.filter(auction=True)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def allItemslicense(request):
    if request.method=="GET":
        allob=Items.objects.filter(license=True)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})


@api_view(['GET','POST'])
def Adduser(request):
    if request.method=="GET":
        cat=request.GET.get("address")
        allob=Userr.objects.get(address=cat)
        serialized=Useserilizer(allob, many=False)
        return Response(serialized.data)
    if request.method=='POST':
        cat=request.POST.get("address")
        try:
            allob=Userr.objects.get(address=cat)
            serializer=Useserilizer(instance=allob, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"update":"ok"})
        except:
            serializer=Useserilizer( data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"creaded":"ok"})


@api_view(['GET'])
def itemids(request):
    if request.method=='GET':
        cat=cat=request.GET.get("address")
        ids=Items.objects.filter(owner=cat).values('tokenId','chain')
       
        ids=str(ids).split('t ')[1].removesuffix('>').strip().replace("'",'''"''').replace('\\','')
        jsonid=json.loads(ids)
        print(ids)
        return Response({"ids":jsonid})

@api_view(['GET','POST'])
def getBids(request):
    if request.method=='GET':
        itemid=request.GET.get("itemid")
        chainid=request.GET.get("chainId")
        all_bids=Bids.objects.filter(itemId=itemid,chainId=chainid).order_by('-id')
        serialized=Bidserializer(all_bids, many=True)
        return Response(serialized.data)
    if request.method=='POST':
        serializer=Bidserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"update":"ok"})

        






    


   






@api_view(['GET'])
def detail(request,pk):
    if request.method=="GET":
        allob=Items.objects.get(itemId=pk)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)













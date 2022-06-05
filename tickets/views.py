from django.http import JsonResponse
from django.shortcuts import render
from . models import Geust,Reserivation,Moive
from . serializers import GuestSerializer, MoiveSerializer, ReserviationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

def firts_way(request):
    guests=[
        {
            "id":1,
            "name":"Mostafa",
            "age":20
        },
        {
            "id":2,
            "name":"Mamdouh",
            "age":50
        }

    ]

    return JsonResponse(guests,safe=False)

def seconed_way(request):

    data=Geust.objects.all()
    print(data)
    response={
        "geust":list(data.values())
    }

    return JsonResponse(response)

@api_view(["GET","POST"])
def RestWay(request):
    method=request.method
    if method=="GET":
        data=Geust.objects.all()
        serializer=GuestSerializer(data,many=True)
        return Response(serializer.data)
    
    elif method=="POST":
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def Rest_Framework_Way(request,pk):

    method=request.method
    data=Geust.objects.get(pk=pk)
    if method=='GET':
        serializer=GuestSerializer(data)
        return Response(serializer.data)

    if method=='PUT':
        serializer=GuestSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if method=='DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Rest_FBV1(APIView):
    def get(self,request):
        data=Geust.objects.all()
        serializer=GuestSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Rest_FBV2(APIView):
    def get(self,request,pk):
        data=Geust.objects.get(pk=pk)
        serializer=GuestSerializer(data)
        return Response(serializer.data)

    def put(self,request,pk):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk):
        data=Geust.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class mixins_list_create(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.post(request)

class  mixins_retrive_update_destory(

    generics.GenericAPIView,mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,mixins.DestroyModelMixin
    ):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)

class generics(ListCreateAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer
    
class generics_pk(RetrieveUpdateDestroyAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer


class viewset(viewsets.ModelViewSet):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer


class viewset_moive(viewsets.ModelViewSet):
    queryset=Moive.objects.all()
    serializer_class=MoiveSerializer


class viewset_reserivation(viewsets.ModelViewSet):
    queryset=Reserivation.objects.all()
    serializer_class=ReserviationSerializer


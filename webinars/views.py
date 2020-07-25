from django.shortcuts import render
from .models import(
    webinarsmodel
)
from .serializer import(
    Taskserializer
)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

class webinarAdder(APIView):
    permissions_classes=[permissions.IsAuthenticated]
    parser_classes=[JSONParser]
    def get(self,request):
        obj=webinarsmodel.objects.filter(user=request.user.id)
        serializer=Taskserializer(obj,many=True)
        return Response(serializer.data,status=200)


    def post(self,request):
        print(request.data)
        request.data['user']=request.user.id
        print(request.data)
        obj=Taskserializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                'status':'added'
            },status=201)

class webinarModifier(APIView):
    permissions_classes=[permissions.IsAuthenticated]
    parser_classes=[JSONParser]
    
    def post(self,request):
        obj=webinarsmodel.objects.filter(id=request.data['id'])
        obj.update(status=request.data['status'])
        return Response(status=202)
        try:
            obj=webinarsmodel.objects.filter(id=request.data['id'])
            obj.update(status=request.data['status'])
            return Response(status=202)
        except:
            return Response(status=404)

class webinarDelete(APIView):
    permissions_classes=[permissions.IsAuthenticated]
    parser_classes=[JSONParser]
    def get(self,request,pk):
        try:
            obj=webinarsmodel.objects.filter(id=pk)
            obj.delete()
            return Response(status=202)
        except:
            return Response(status=404)
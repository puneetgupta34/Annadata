from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

global data
data = ["text"]


class Person(APIView):
    def get(self, request, formate=None):
        message = {
            'Response': 200,
            'message': "welcome",
            'data': data
        }

        return Response(message)

    def post(self, request, formate=None):
        datam = request.data
        name = datam.get('name', None)
        data.append(name)
        message = {
            'Response': 200,
            'message': "welcome"
            
        }

        return Response(message)

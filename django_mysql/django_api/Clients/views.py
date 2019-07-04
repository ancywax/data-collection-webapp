from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.db.models import Q
from . models import Surveyor
from . serializers import SurveyorSerializer

"""
    API endpoint that allows Surveyor to be viewed.
"""


class SurveyorView(APIView):

    def get(self, request):
        queryset = Surveyor.objects.all()
        serializer = SurveyorSerializer(queryset, many=True)
        return Response(serializer.data)


"""
    API endpoint that allows a Surveyor instance to be viewed.
"""


class SurveyorDetail(APIView):
    def get_object(self, username):
        try:
            return Surveyor.objects.get(userName=username)
        except Surveyor.DoesNotExist:
            raise Http404

    def get(self, request, username):
        print(request)
        queryset = self.get_object(username)
        serializer = SurveyorSerializer(queryset)
        return Response(serializer.data)


"""
    API endpoint that allows a Surveyor instance to be registered.
"""


class SurveyorRegistration(APIView):
    def get(self, request, username, email):
        print(request.data)
        if Surveyor.objects.filter(userName=username, email=email).exists():
            queryset = Surveyor.objects.get(userName=username, email=email)
            serializer = SurveyorSerializer(queryset)
            return Response(serializer.data)
        return HttpResponse("Surveyor Does Not Exist", content_type="text/plain")

    def post(self, request, username, email):
        print(request.data)
        if Surveyor.objects.filter(Q(userName=username) | Q(email=email)).exists():
            return HttpResponse("Already Exist", content_type="text/plain")
        serializer = SurveyorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Success", content_type="text/plain")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    API endpoint that allows a Surveyor instance to be logged in.
"""


class SurveyorLogin(APIView):
    def get(self, request, username, password):
        if Surveyor.objects.filter(userName=username, password=password).exists():
            queryset = Surveyor.objects.get(userName=username, password=password)
            serializer = SurveyorSerializer(queryset)
            return HttpResponse("True", content_type="text/plain")
        return HttpResponse("False", content_type="text/plain")

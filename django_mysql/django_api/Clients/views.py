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
from . models import Surveyor, Survey, SurveyQuestion, SurveyFile, Respondent
from . serializers import SurveyorSerializer, SurveySerializer, SurveyQuestionSerializer, SurveyFileSerializer, RespondentSerializer
import json

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
        print("starting")
        if Surveyor.objects.filter(userName=username, email=email).exists():
            queryset = Surveyor.objects.get(userName=username, email=email)
            serializer = SurveyorSerializer(queryset)
            return Response(serializer.data)
        return HttpResponse("Surveyor Does Not Exist", content_type="text/plain")

    def post(self, request, username, email):
        print(request.data["firstName"])
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


"""
    API endpoint that allows a Survey instance to be added to the database.
"""


class SurveyCRUD(APIView):
    def get(self, request):
        print(request.data)
        if 'id' not in request.data["survey"] and 'title' not in request.data["survey"]:
            if Survey.objects.filter(userName=request.data["survey"]["userName"]).exists():
                queryset = Survey.objects.filter(userName=request.data["survey"]["userName"])
                serializer = SurveySerializer(queryset, many=True)
                return Response(serializer.data)
            return HttpResponse("False", content_type="text/plain")
        else:
            if Survey.objects.filter(id=request.data["survey"]["id"], userName=request.data["survey"]["userName"]).exists():
                queryset = Survey.objects.get(id=request.data["survey"]["id"], userName=request.data["survey"]["userName"])
                serializer = SurveySerializer(queryset)
                return Response(serializer.data)
            return HttpResponse("False", content_type="text/plain")

    def post(self, request):
        print(request.data)
        if Surveyor.objects.filter(userName=request.data["survey"]["userName"]).exists():
            serializer = SurveySerializer(data=request.data["survey"])
            if serializer.is_valid():
                serializer.save()
                survey_id = serializer.data["id"]
                print(survey_id)
                for obj in request.data["surveyQuestion"]:
                    obj["surveyID"] = survey_id
                #survey_question = {}
                queryset = request.data["surveyQuestion"]
                serializer_q = SurveyQuestionSerializer(data=queryset, many=True)
                if serializer_q.is_valid():
                    serializer_q.save()
                    print(serializer_q.data)
                    #return HttpResponse(survey_id, content_type="text/plain")
                    return Response(survey_id)
                return Response(serializer_q.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse("user does not exist", content_type="text/plain")


"""
    API endpoint that allows a Respondent instance to be added to the database.
"""


class RespondentCRUD(APIView):
    def get(self, request):
        print(request.data)
        queryset = Respondent.objects.all()
        serializer = RespondentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = RespondentSerializer(data=request.data["respondent"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

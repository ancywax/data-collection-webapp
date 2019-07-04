from rest_framework import serializers
from .models import Surveyor, Survey, SurveyQuestion, SurveyFile


class SurveyorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Surveyor
#        fields = ('firstName','LastName')
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = '__all__'


class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveyFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyFile
        fields = '__all__'

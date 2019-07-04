from django.contrib import admin
from . models import Surveyor, Survey, SurveyQuestion, SurveyFile

# Register your models here.
admin.site.register(Surveyor)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyFile)

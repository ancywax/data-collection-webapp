from django.contrib import admin
from . models import Surveyor, Survey, SurveyQuestion, SurveyFile, Respondent

# Register your models here.
admin.site.register(Surveyor)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyFile)
admin.site.register(Respondent)

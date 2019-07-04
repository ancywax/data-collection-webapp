from django.db import models
from django.db.models import CharField


# Create your models here.
class Surveyor(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default='Password')

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)


class Survey(models.Model):
    # surveyID = models.AutoField(primary_key=True)
    userName = models.ForeignKey(Surveyor, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s' % (self.title, self.userName)


class SurveyQuestion(models.Model):
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE)
    questionID = models.IntegerField()
    question = models.CharField(max_length=1000)
    questionType = models.CharField(max_length=50)
    options = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '%s %s' % (self.question, self.questionType)


class SurveyFile(models.Model):
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE)
    file = models.FileField(default='none.php')

    def __str__(self):
        return '%s %s' % (self.file, self.surveyID)

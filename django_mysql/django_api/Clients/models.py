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


class Respondent(models.Model):
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=50)
    familySize = models.IntegerField()
    religion = models.CharField(max_length=50)
    educationLevel = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    monthlyEarningRange = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='null')
    telephone = models.CharField(max_length=50, default='null')

    def __str__(self):
        return '%s %s %s' % (self.gender, self.dob, self.region)

from django.db import models
from accounts.models import User


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_description = models.TextField()
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    c_op = models.IntegerField('Correct Option')

    def __str__(self):
        return self.question_description[:50]


class Test(models.Model):
    name = models.CharField('Test Name', max_length=250)
    each_questions_marks = models.IntegerField("Each Question's Mark")
    total_questions = models.IntegerField('No. of Questions')
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.shortcuts import render
from .models import *


# Create your views here.
def test(request, test_id):
    tst = Test.objects.filter(id=test_id)[0]
    questions = Question.objects.filter(test=tst)
    return render(request, 'teachers/test.html', {'questions': questions})

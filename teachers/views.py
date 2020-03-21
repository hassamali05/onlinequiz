from django.shortcuts import render
from .models import *


# Create your views here.
def test(request, test_id):
    tst = Test.objects.get(id=test_id)
    questions = Question.objects.filter(tests=tst)
    return render(request, 'teachers/test.html', {'questions': questions})

from django.shortcuts import render, redirect
from .models import *
from accounts.models import User


# Create your views here.
def teachers(request):
    t_id = request.session['userID']
    teacher = User.objects.get(id=t_id)
    tests = Test.objects.filter(teacher=teacher)
    return render(request, 'teachers/teacher.html', {'user': teacher, 'Test': tests})


def test(request, test_id):
    tst = Test.objects.get(id=test_id)
    questions = Question.objects.filter(tests=tst)
    return render(request, 'teachers/test.html', {'questions': questions})


def create_quiz(request, teacher_id):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        return render(request, 'teachers/create_quiz.html', {'subjects': subjects, 'teacher': teacher_id})
    else:
        name_of_quiz = request.POST['name']
        each_marks = request.POST['each_questions_marks']
        total_question = request.POST['total_questions']
        sub = request.POST['dropdown']
        sub = Subject.object.get(name=sub)
        new_test = Test.objects.create(name=name_of_quiz, each_questions_marks=each_marks,
                                       total_questions=total_question, sub_id=sub, teacher=teacher_id)
        print(f'Test Created with teacher ID = {teacher_id}')
        return render(request, 'teachers/add_questions.html',
                      {"Test_id": new_test.id})


def add_subject(request):
    if request.method == 'GET':
        return render(request, 'teachers/add_subject.html')
    else:
        name = request.POST['subject_name']
        subs = Subject.objects.filter(name=name)
        if subs.exists() > 0:
            return render(request, 'teachers/add_subject.html', {'error': 'Subject already exists '})
        else:
            Subject.objects.create(name=name)
            return redirect("create_quiz", request.session['userID'])


def add_questions(request, test_id):
    des = request.POST['description']
    opt1 = request.POST['opt1']
    opt2 = request.POST['opt2']
    opt3 = request.POST['opt3']
    opt4 = request.POST['opt4']
    c_opt = request.POST['opt5']
    tst = Test.objects.filter(id=test_id)
    q = Question.objects.create(question_description=des, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4, c_op=c_opt,
                                tests=tst)
    if tst.total_questions.count() < Question.objects.filter(tests=tst).cout():
        return render(request, 'teachers/add_questions.html', {"Test_id": tst.id})
    else:
        return redirect('teachers')

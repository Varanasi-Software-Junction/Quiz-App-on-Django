from django.shortcuts import render

from . import ProgrammingQuestions as questionsbank


def quiz(request):
    currentquizno = 0
    currentquestion = questionsbank.questions[currentquizno]
    return render(request, "quiz.html")
    # return HttpResponse("Home")

from django.shortcuts import render

from . import ProgrammingQuestions as questionsbank


def quiz(request):
    correctresult='<span class="material-icons" style="color: green">check</span>'
    wrongresult='<span class="material-icons" style="color: red">close</span>'
    currentquestionno = -1
    currentquestion = 'Press any key to start'
    questions = questionsbank.questions
    n = len(questions)

    if request.GET:
        currentquestionno = int(request.GET["questionno"])
        print(currentquestionno)
        currentquestionno += 1
        # currentquestion = questionsbank.questions[currentquizno]

        if currentquestionno >= n:
            currentquestion = 'Test over'
        else:
            if currentquestionno == -1:
                currentquestionno += 1
            currentquestion = questions[currentquestionno]
    return render(request, "quiz.html", {'qno': currentquestionno, "question": currentquestion,"results":correctresult})
    # return HttpResponse("Home")

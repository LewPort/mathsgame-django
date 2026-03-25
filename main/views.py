from django.shortcuts import render
from . import logic

# Create your views here.

def index(request):
    question = request.session.get('question')
    guess = request.GET.get('guess', None)
    answer = request.session.get('answer')
    try:
        guess = int(guess)
    except (ValueError, TypeError):
        pass    
    if guess == answer:
        verdict = True
        question, answer = logic.ask_question()
        request.session['question'] = question
        request.session['answer'] = answer
        request.session['score'] = request.session.get('score', 0) + 1
    elif guess is not None:
        verdict = False
    else:
        verdict = None
        request.session['score'] = 0
        question, answer = logic.ask_question()
        request.session['question'] = question
        request.session['answer'] = answer
    return render(request, 'main/index.html', 
                  {'title': 'Maths Game',
                   'question': question,
                   'verdict': verdict,
                   'score': request.session.get('score', 0)})
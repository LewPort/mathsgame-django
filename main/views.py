from django.shortcuts import render
from . import logic

# Create your views here.

def index(request):
    question = request.session.get('question')
    guess = request.GET.get('guess')
    answer = request.session.get('answer')
    try:
        guess = int(guess)
    except (ValueError, TypeError):
        pass    
    if guess == answer:
        print ('Correct answer!')
        verdict = True
        question, answer = logic.ask_question()
        request.session['question'] = question
        request.session['answer'] = answer
        request.session['score'] += 1
    elif guess is not None:
        print('Incorrect answer!')
        verdict = False
    else:
        print('No guess yet.')
        verdict = None
        request.session['score'] = 0
        question, answer = logic.ask_question()
        request.session['question'] = question
        request.session['answer'] = answer
    print(f'Guess is {guess}')
    print(f'Answer is {answer}')
    return render(request, 'main/index.html', 
                  {'title': 'Maths Game',
                   'question': question,
                   'verdict': verdict,
                   'score': request.session.get('score', 0)})
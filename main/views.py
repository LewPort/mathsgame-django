from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html', 
                  {'title': 'Welcome to the Maths Game!',
                   'question': 'What is 2 + 2?'})
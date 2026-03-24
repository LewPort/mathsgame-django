import random

MAX_NUM_A = 10
MAX_NUM_B = 5
NEGATIVES_ALLOWED = False

def gen_nums():
    '''
    Generate two random numbers.
    '''
    a = random.randint(0,MAX_NUM_A)
    b = random.randint(0, MAX_NUM_B)
    return a, b

def add(a, b):
    '''
    Takes 2 numbers (a, b) and adds them.
    Returns the question in readable form as a string,
    and the answer as an int.
    '''
    question = f'What is {a} + {b}? '
    answer = a + b
    return question, answer

def subtract(a, b):
    '''
    Takes two numbers (a, b) and subtracts a - b.
    Returns the question in readable form as
    a string, and the answer as an int.
    '''
    question = f'What is {a} - {b}? '
    answer = a - b
    return question, answer

functions = [add, subtract]

def ask_question():
    '''
    Generate two random numbers and a random function.
    Use the function to generate a question and answer.
    Return the question and answer.
    '''
    a, b = gen_nums()
    func = random.choice(functions)
    question, answer = func(a, b)

    while not NEGATIVES_ALLOWED and answer < 0:
        print('Generated a negative answer, regenerating...')
        question, answer = ask_question()
    return question, answer

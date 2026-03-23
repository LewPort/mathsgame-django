import random

def gen_nums():
    '''
    Generate two random numbers.
    '''
    a = randint(0,MAX_NUM_A)
    b = randint(0, MAX_NUM_B)
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



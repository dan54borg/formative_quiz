import random   # Importing random to generate random numbers for the questions

def questions():
    """Returns a random question and its correct result."""
    num_1 = random.randint(1,15)    
    num_2 = random.randint(1,15)    
    operator = random.choice(['+', '-', '*'])  

    # Calcultes result based on chosen operator
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    return num_1, num_2, operator, result

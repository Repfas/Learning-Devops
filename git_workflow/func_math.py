def math_problem(a,b):
    '''This function is for experimental calculation'''
    equation = (a + b)**2/a**2
    if equation > 15 :
        return f'the result is {equation}. its to complex'
    elif equation > 5:
        return f'the result is {equation}. its normal'
    elif equation >=1:
        return f'the result is {equation}. good result'
    elif equation <1 and equation>0:
        return f'the result is {equation}. good result'
    else:
        return f'wrong result. please do experimental again'
    
exp_1 = math_problem(7,1)
print(exp_1)
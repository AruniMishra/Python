
def add(x,y):

    '''
    simple return statement
    '''
    return x+y

def divide(x,y):
    
    if y == 0:
        raise ValueError('cannot divide by Zero')
    return x/y
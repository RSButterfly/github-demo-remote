#Add implementation
def add(x,y):
    c = x+y
    return c

#Subtract implementation
def subtract(x,y):
    c = x-y
    return c         # on remote repo

#Multiply implementation
def multiply(x,y):
    return x*-y         # on branch Bug456

#Divide implementation
def divide(x,y):
    if y==0:                        # on master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y       

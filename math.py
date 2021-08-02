#Add implementation
def add(x,y):
    c = x+y
    return c

#Subtract implementation
def subtract(x,y):
    return x-y         # on master branch

#Multiply implementation
def multiply(x,y):
    c = x*y
    return c         # on local repo

#Divide implementation
def divide(x,y):
    if y==0:                        # on master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y       
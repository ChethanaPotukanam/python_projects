import math
print("*********Calculator*********")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def p(x,y):
    return math.pow(x,y)
l=[0,0]
r=0
c='n'
while(True):
    if(c=='y'):
        l[0]=r
    if(c=='n'):
        l[0]=int(input('Enter a num:'))
    l[1]=int(input('Enter another num:'))
    s=input('Enter + for addition - for subraction * for multiplication / for division p for power:')
    if(s=='+'):
        r=add(l[0],l[1])
        print(f'{l[0]}+{l[1]}={r}')
    elif(s=='-'):
        r=sub(l[0],l[1])
        print(f'{l[0]}-{l[1]}={r}')
    elif(s=='*'):
        r=mul(l[0],l[1])
        print(f'{l[0]}*{l[1]}={r}')
    elif(s=='/'):
        r=div(l[0],l[1])
        print(f'{l[0]}/{l[1]}={r}')
    elif(s=='p'):
        r=p(l[0],l[1])
        print(f'{l[0]}power{l[1]}={r}')
    else:
        print("Sorry....Try again")
    print(f'To continue calculation with {r}:y\nFor new calculation:n\nTo exit:e')
    f=input('Enter y or n or e:')
    if(f=='e'):
        break
    c=f
    
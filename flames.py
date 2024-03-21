x=input('Enter your name:')
y=input('Enter another name:')
xl=list(x)
yl=list(y)
print(xl)
print(yl)
for i in xl:
    if i in yl:
        xl.remove(i)
        yl.remove(i)
print(xl)
print(yl)
s='flames'
n=len(xl)+len(yl)
for j in range(n):
    j=j%len(s)+1
var=s[j-1]
print(var)
if(var=='f'):
    print('friends')
elif(var=='l'):
    print('lorry')
elif(var=='a'):
    print('anime')
elif(var=='m'):
    print('mountain')
elif(var=='e'):
    print('entertain')
elif(var=='s'):
    print('sweet')
    

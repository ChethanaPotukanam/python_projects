print('Give some input only alphabets allowed you will get encrypted output')
x=input('Enter some text here(no spaces,numbers):')
n=int(input('Enter a single digit number(except 0):'))
alpha=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
#num=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
l=list(x)
for i in range(len(l)):
    j=alpha.index(l[i])
    jj=(j+n)%26
    l[i]=alpha[jj]
print('Encryptedd code:')
for i in l:
    print(i,end='')
print('\n')
print('Do you want to see actual text:')
print('Enter 1 if yes 0 for no:')
s=int(input())
if(s==0):
    pass
elif(s==1):
    for i in range(len(l)):
        j=alpha.index(l[i])
        jj=(j-n)%26
        l[i]=alpha[jj]
    for i in l:
        print(i,end='')
    print('\n')


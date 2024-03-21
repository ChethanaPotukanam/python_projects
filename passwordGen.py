import random
l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l3=['1','2','3','4','5','6','7','8','9','0']
l5=['!','@','#','$','%','^','&','*','(',')','+','_','-']
n=0
while(True):
    n=int(input('Enter length of password(>=8 and <=35):'))
    if(n>=8 and n<=35):
        break
s=n//4
a=random.sample(l,k=s)
b=random.sample(l2,k=s)
c=random.sample(l3,k=s)
d=random.sample(l5,k=s)
r=n-(s*4)
a2=random.sample(l,k=r)
b2=random.sample(l2,k=r)
c2=random.sample(l3,k=r)
d2=random.sample(l5,k=r)
e=[]
e.extend(a2)
e.extend(b2)
e.extend(c2)
e.extend(d2)
f=random.sample(e,k=r)
p=[]
p.extend(a)
p.extend(b)
p.extend(c)
p.extend(d)
p.extend(f)
random.shuffle(p)
p=''.join(p)
print('Your SECURE password:',end='')
for i in p:
    print(i,end='')
print('\n')

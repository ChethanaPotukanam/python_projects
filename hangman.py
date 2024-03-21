import random
# h1='''
#       _____
#         | '''
# h2='''
#       _____
#         |
#         0  '''
# h3='''
#       _____
#         |
#         0  
#         |'''
# h4='''
#       _____
#         |
#         0  
#        /|\ '''
# h5='''
#       _____
#         |
#         0  
#        /|\ 
#        / \ '''
#ACTUALLY THIS IS ALSO CORRECT
import hang_stages as hs
l=['blue','white','black','orange','red','yellow','green','violet','pink','grey']
print('****Welcome to Hangman Game****')
print('Guess a letter in color that matches with the given blanks')
print('Remember if you made mistake more than 5 times you will be lost....')
s=random.choice(l)
n=len(s)
sl=list(s)
word=[]
for i in range(n):
    word.append('_')
print(':::::Game started:::::')
for i in range(n):
    print(word[i],end=' ')
print('\n')
count=5
while(True):
    c=input('\nEnter a letter:')
    if c in sl:
        i=sl.index(c)
        sl[i]='_'
        word[i]=c
        for i in range(n):
            print(word[i],end=' ')
        print('\n')
    else:
        count-=1
        for i in range(n):
            print(word[i],end=' ')
        print('\n')
        #print(f'Only {count} chances left')
        # if(count==5):
        #     print(h5)
        # elif(count==4):
        #     print(h4)
        # elif(count==3):
        #     print(h3)
        # elif(count==2):
        #     print(h2)
        # elif(count==1):
        #     print(h1)
        print(hs.stages[count-1])
    if(('_' in word) and count==0):
        print('You lost the game')
        break
    if('_' not in word):
        print('\nYou are a gem you got it right')
        for i in range(n):
            print(word[i],end='')
        print('\n')
        break



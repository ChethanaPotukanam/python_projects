import data
import random
print("\n................WELCOME TO HIGHER LOWER GAME................\n")
score=0
while(True):
    c=random.choice(data.l)
    c2=random.choice(data.l)
    while(c==c2):
        c2=random.choice(data.l)
    print(c)
    print(c2)
    print(f'compare these two who has more followers according to you?\n')
    print(f"2:{c['name']} or 3:{c2['name']}\n")
    guess=int(input('Enter:'))
    win= 2 if c['followers']>c2['followers'] else 3
    if(win==guess):
        score+=1
        print(f'Your score is {score}\n')
    else:
        print(f'Your final score is {score}\n')
        print('Your game is over\n')
        break
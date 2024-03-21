import random
print("\n^^^^^^WELCOME TO GUESS THE NUMBER GAME^^^^^^\n")
n=0
while(True):
    hardness=input("Enter hardness level (easy or hard)\t").lower()
    if(hardness=='easy' or hardness=='hard'):
        if(hardness=='easy'):
            n=9
            print('\n....You have 9 chances....\n')
        else:
            n=5
            print('\n....You have 5 chances....\n')
        break
num=random.randint(0,90)
g=-2
print('\nGuess a number between 0 and 90')
while(g!=num and n!=0):
    g=int(input('\nenter the num:\t'))
    if(g<num):
        print('\nyour guess is too low')
        n-=1
        print(f'\nonly {n} chances left')
    elif(g>num):
        print('\nyour guess is too high')
        n-=1
        print(f'\nonly {n} chances left')
    elif(g==num):
        print("\n........  (: You Won The Game :)  ........\n")
        exit()
print('\n):You lose the game:(\n')
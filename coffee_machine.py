print('Welcome to the Restaurant')
profit=0
today_cost=200
items_list=['Dosa','Idly','Puri','Vada']
quantity=[5,5,5,5]
cost=[20,30,41,25]
while(True):
    flag=0
    for i in quantity:
        if(i==0):
            flag+=1
    if(flag==4):
        ('All Items over restaurant closed')
        break
    print('Enter which item you want:')
    print(items_list)
    item=input().capitalize()
    ind=items_list.index(item)
    c=2
    while(quantity[ind]<=0):
        n=int(input("Item completed.Do you want to order other item(Enter 0 or 1):"))
        if(n==1):
            item=input().capitalize()
            ind=items_list.index(item)
        if(n==0):
            c=int(input('Any more customers(If yes enter 1 otherwise 0):'))
    if(c==1):   
        continue
    if(c==0):
        break       
    m=cost[ind]
    quantity[ind]-=1
    print(f'Cost of {item} is {m}')
    n=int(input('Enter money:'))
    while(n<m):
            n=int(input('Enter enough money:'))
    if(n<m):
        print('Not enough money')
    elif(n>m):
        print('Return money:',n-m)
        print(f'Hot Hot Tasty Tasty {item}')
    else:
        print(f'Hot Hot Tasty Tasty {item}')
    profit+=m
    n=int(input('Any more customers(If yes enter 1 otherwise 0):'))
    if(n!=1):
        break
print("Today Profit:",profit-today_cost)


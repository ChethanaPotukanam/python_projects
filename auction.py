import auc
d={}
print("*****Silent Auction program****")
while(True):
    l=auc.auc()
    d[l[0]]=l[1]
    s=input("Any more bidders(Enter 'yes' or 'no' only):")
    if(s=='no'):
        break
    while(s!='no' and s!='yes'):
        s=input('Enter yes or no only(case sensitive)')
max=0
name=''

for i,j in d.items():
    if(j>max):
        max=j
        name=i
print(f"{name} won with bid {max}")

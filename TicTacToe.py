def Board(b):
    x=['','','','','','','','','']
    for i in range(9):
        x[i]=b[i] if b[i]==' x ' or b[i]==' o ' else f' {i} '
    print(f"{x[0]}|{x[1]}|{x[2]}\n---|---|---\n{x[3]}|{x[4]}|{x[5]}\n---|---|---\n{x[6]}|{x[7]}|{x[8]}\n---|---|---\n")
def checkWin(b):
    if((b[0]==' o ' and b[1]==' o ' and b[2]==' o ') 
    or (b[3]==' o ' and b[4]==' o ' and b[5]==' o ')
    or (b[6]==' o ' and b[7]==' o ' and b[8]==' o ')
    or (b[0]==' o ' and b[3]==' o ' and b[6]==' o ')
    or (b[1]==' o ' and b[4]==' o ' and b[7]==' o ')
    or (b[2]==' o ' and b[5]==' o ' and b[8]==' o ')
    or (b[0]==' o ' and b[4]==' o ' and b[8]==' o ')
    or (b[2]==' o ' and b[4]==' o ' and b[6]==' o ')):
        print("\n****Player o wins****\n")
        exit()
    elif((b[0]==' x ' and b[1]==' x ' and b[2]==' x ') 
    or (b[3]==' x ' and b[4]==' x ' and b[5]==' x ')
    or (b[6]==' x ' and b[7]==' x ' and b[8]==' x ')
    or (b[0]==' x ' and b[3]==' x ' and b[6]==' x ')
    or (b[1]==' x ' and b[4]==' x ' and b[7]==' x ')
    or (b[2]==' x ' and b[5]==' x ' and b[8]==' x ')
    or (b[0]==' x ' and b[4]==' x ' and b[8]==' x ')
    or (b[2]==' x ' and b[4]==' x ' and b[6]==' x ')):
        print("\n****Player x wins****\n")
        exit()
    elif('   ' not in b):
        print('\n****Both of you lost the game****\n')
        exit()
    else:
        return
if __name__=="__main__":
    b=['   ','   ','   ','   ','   ','   ','   ','   ','   ']
    print("****Player 1 considered as x Player 2 considered as o****")
    print("****Start The Game****")
    c=0
    Board(b)
    while(True):
        if(c%2==0):
            print("Player x turn")
        else:
            print("Player o turn")
        n=int(input('Enter a number between 0-8:'))
        while(b[n]!='   '):
            n=int(input('Enter a number between 0-8:'))
        if(c%2==0):
            b[n]=' x '
        else:
            b[n]=' o '
        c+=1
        Board(b)
        checkWin(b)

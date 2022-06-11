list=[0,1,2,3,4,5,6,7,8]
for i in range(8):
    for x in list[0:3]:
        print(x,'',end="")
    print()
    for y in list[3:6]:
        print(y,'',end="")
    print()
    for z in list[6:9]:
        print(z,'',end="")
    print()
    p_1=int(input("enter p_1"))
    list[p_1]='X'
    count=list.count('X')
    if list[0]==list[1]==list[2]=='X':
        print('Player 1 wins')
        break
    elif list[3]==list[4]==list[5]=='X':
        print('Player 1 wins')
        break
    elif list[6]==list[7]==list[8]=='X':
        print('Player 1 wins')
        break
    elif list[0]==list[3]==list[6]=='X':
        print('Player 1 wins')
        break
    elif list[1]==list[4]==list[7]=='X':
        print('Player 1 wins')
        break
    elif list[2]==list[5]==list[8]=='X':
        print('Player 1 wins')
        break
    elif list[0]==list[4]==list[8]=='X':
        print('Player 1 wins')
        break
    elif list[6]==list[4]==list[2]=='X':
        print('Player 1 wins')
        break
    elif count==5:
        print('Match draw')
        break
    for i in range(8):
        for x in list[0:3]:
            print(x,'',end="")
        print()
        for y in list[3:6]:
            print(y,'',end="")
        print()
        for z in list[6:9]:
            print(z,'',end="")
        print()
        p_2=int(input("enter p_2"))
        list[p_2]="O"
        count=list.count('O')
        if list[0]==list[1]==list[2]=='O':
            print('Player 2 wins')
            break
        elif list[3]==list[4]==list[5]=='O':
            print('Player 2 wins')
            break
        elif list[6]==list[7]==list[8]=='O':
            print('Player 2 wins')
            break
        elif list[0]==list[3]==list[6]=='O':
            print('Player 2 wins')
            break
        elif list[1]==list[4]==list[7]=='O':
            print('Player 2 wins')
            break
        elif list[2]==list[5]==list[8]=='O':
            print('Player 2 wins')
            break
        elif list[0]==list[4]==list[8]=='O':
            print('Player 2 wins')
            break
        elif list[6]==list[4]==list[2]=='O':
            print('Player 2 wins')
            break
        elif count==5:
             print('Match draw')
             break
        break

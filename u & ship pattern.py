import random
def u_pattern():
    x=random.choice([1,2,3])
    a=['.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ']
    if x==1:
        a[0]=a[2]=a[5]=a[7]=a[10]=a[11]=a[12]='* '
    elif x==2:
        a[12]=a[14]=a[17]=a[19]=a[22]=a[23]=a[24]='* '
    elif x==3:
        a[6]=a[8]=a[11]=a[13]=a[16]=a[17]=a[18]='* '
    for i in range(25):
        for x in a[0:5]:
            print(x,'',end="")
        print()
        for y in a[5:10]:
            print(y,'',end="")
        print()
        for z in a[10:15]:
            print(z,'',end="")
        print()
        for k in a[15:20]:
            print(k,'',end="")
        print()
        for q in a[20:25]:
            print(q,'',end="")
        print()
        break
def ship():
    x=random.choice([1,2,3])
    a=['.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ','.  ']
    if x==1:
        a[0]=a[1]=a[5]=a[11]=a[12]=a[7]='* '
    elif x==2:
        a[12]=a[13]=a[17]=a[23]=a[19]=a[24]='* '
    elif x==3:
        a[6]=a[7]=a[11]=a[17]=a[13]=a[18]='* '
    for i in range(25):
        for x in a[0:5]:
            print(x,'',end="")
        print()
        for y in a[5:10]:
            print(y,'',end="")
        print()
        for z in a[10:15]:
            print(z,'',end="")
        print()
        for k in a[15:20]:
            print(k,'',end="")
        print()
        for q in a[20:25]:
            print(q,'',end="")
        print()
        break

random.choice([u_pattern(),ship()])



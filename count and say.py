n=int(input('n'))
s='1'
for i in range(1,n):
    if s.count('1')>0 and s.count('2')==0:
        new=str(s.count('1'))+'1'
        print(new)
        s=new
    elif s.count('1')>0 and s.count('2')>0 and s.count('3')==0:
        new=str(s.count('1'))+'1'+str(s.count('2'))+'2'
        print(new)
        s=new
    elif s.count('1')>0 and s.count('2')>0 and s.count('3')>0:
        new=str(s.count('1'))+'1'+str(s.count('2'))+'2'+str(s.count('3'))+'3'
        print(new)
        s=new
    
        

        
    
        



    

    
    

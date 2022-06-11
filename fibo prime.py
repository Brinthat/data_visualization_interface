import math
n=int(input('sd'))
a=0
b=1
fibo=[]
for x in range(n):
    c=a+b
    if c<n:
        if c>1:
            fibo.append(c)
    a=b
    b=c
print(fibo)
prime=[]
for i in fibo:
    for j in range(2,i):
        s=i%j
        if s==0 :
            break
    else:
        prime.append(i)
print(prime)


'''prime=set(prime)
newprime=list(prime)
print(newprime)
sum=sum(newprime)
print(sum)'''






            
            
    
                
     
  
       
    
    

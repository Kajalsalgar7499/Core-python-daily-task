#for loop 10 program
#print 1 to 10 series
for i in range(1,11,1):
    print(i)
  
#print 10 to 1 series    
for j in range(11,0,-1):
    print(j,end="")
    
for k in range(0,6):
    print("*" * k)


# while 

k=1
while(k<=10):
    print(k,end="")
    k+=1
    
x=1
while(x<=100):
    if(x%2==0):
        print(x)
        x+=1
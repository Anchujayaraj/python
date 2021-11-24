a=input("enter numbers")
b=a.split(",")
c=list(map(int,b))
n=len(c)
for i in range(n):
    if(c[i]>100):
        print("over")
    else:
        print(c[i])
            
         

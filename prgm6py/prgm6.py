a=input("enter numbers")
b=list(map(int,a.split(",")))
c=[i for i in range(len(b)) if(i%2!=0)]
print(c)

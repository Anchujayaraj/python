a=input("enter the numbers")
b=a.split(",")
c=list(map(int,b))
d=input("enter the numbers")
e=d.split(",")
f=list(map(int,e))
if(len(c)==len(f)):
                   print("The lists are of same length")
else:
       print("The lists are of different length")
sum(c)
sum(f)
if(sum(c)==sum(f)):
    print("The lists sums to same value")
else:
    print("The lists sums to different value")
list3=[i for i in c if i in f]
print("numbers occurs in both lists are:",list3)


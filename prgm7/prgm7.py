a=input("Enter the first color list:")
b=list(a.split(","))
c=input("Enter the second color list:")
d=list(c.split(","))
list1=[i for i in b if i not in d]
print("list of colors from list 1 not contained in list2 are:",list1)

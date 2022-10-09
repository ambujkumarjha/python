lst=list()
n = int(input("Enter the size of list:"))
for i  in range(0,n):
    e= int (input())
    lst.append(e)
print(lst)
l1=list()
r=int(input("Enter the row size-"))
c=int(input("Enter the column size-"))

matrix=[]

for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
    
max2=matrix[0][0]
min2=matrix[0][0]

for i in range(r):
    for j in range(c):
        if matrix[i][j]>max2:
            max2=matrix[i][j]
        if matrix[i][j]<min2:
            min2=matrix[i][j]

print("max=",max2,"min=",min2)
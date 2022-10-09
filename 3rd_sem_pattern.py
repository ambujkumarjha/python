r=int(input("Enter the no of rows-"))

for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print("\n")
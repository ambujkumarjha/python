r=int(input("Enter the no of rows-"))

for i in range(1,(r//2)+2):
    for j in range ((r//2)-i+1):
        print(" ",end=" ")
    for j in range ((i*2)-1):
        print("*",end=" ")
    print()

for i in range(r//2,0,-1):
    for j in range (r//2-i+1):
        print(" ",end=" ")
    for j in range (0,2*i-1):
        print("*",end=" ")
    print()
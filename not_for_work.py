def toh(n,A,B,C):
    if (n>0):
        toh(n-1,A,C,B)
        print("Move disk from ",A,"to ",C)
        toh(n-1,B,A,C)
    
n=int(input("Enter no of disk - "))
toh(n,'A','B','C')

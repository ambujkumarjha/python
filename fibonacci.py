n = int (input("Enter the number of terms :"))
a,b,i=0,1,1
print("The fibonacco series is")
while i<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
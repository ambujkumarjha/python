import math as m
for i in range(100,1000):
    s=0
    j=i
    while(j>0):
        r=j%10
        fact=m.factorial(r)
        s=s+fact
        j=j//10
    if i==s:
        print("Speical numbers are:",i)
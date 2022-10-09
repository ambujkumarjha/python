#write a program to find whether a given number is prime or not
num=int ( input (" enter the no."))
prime = True

for i in range ( 2,num):
    if (num % i==0):
        prime = False
        break
if prime :
    print (" this is the prime number ")
else :
    print ( ' this  number is not a prime')
    

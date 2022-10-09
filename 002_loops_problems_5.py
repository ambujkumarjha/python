# write a program  to find whether a given number is prime or not 
n1 = int(input("Enter lower range: "))
n2= int(input("Enter upper range: "))

print("The prime numbers are :")
for num in range(n1, n2 + 1):
    if num > 1:
        for i in range(2, int(num ** .5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
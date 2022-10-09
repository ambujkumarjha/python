value = int(input("Enter no. of terms : "))
n1 = 0
n2 = 1
print(f"\nYour Fibonacci series of {value} terms are :")
for i in range(0,value):
  print(n1,end=" ")
  n3 = n2
  n2 = n1 + n2
  n1 = n3
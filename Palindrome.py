n = int(input("Enter a number:"))
rev = 0
temp = n

while n>0 :
  rev = rev*10 + (n%10)
  n = n//10

print(f"\nReverse of {temp} is {rev}")

if(temp==rev):
  print(f"The number {temp} is a pallindrome number.")
else:
  print(f"The number {temp} is not a pallindrome number.")
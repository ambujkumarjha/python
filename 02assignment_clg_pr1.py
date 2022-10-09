'''Q. A) Write a python program to swap two variables using and without using
third variable.

Note: The values be integer or float

Output:
Enter the value for the first variable (a):
Enter the value for the second variable (b) :
Before swapping: a = <value>, b = <value>
After swapping: a = <value>, b = <value>'''

a=eval(input("Enter value for variable a:")) 
b=eval(input("Enter value for variable b:"))

print(f"Before swapping: a= {a} , b= {b}")
a,b = b,a
print(f"After swaping: a= {a} , b= {b}")




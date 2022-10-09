# in genral , an equation  of the form ax^2+bx+c=0 is known as the qudratic equation accept the values of
#  a,b and c from the user and write a python program to calculate the roots of the given quardratic equation. 
# you must be able to handel imaginary roots.
a=int(input("Enter the the value of a:"))
b=int(input("Enter the the value of b:"))
c=int(input("Enter the the value of c:"))
d = b**2-4*a*c
if d>0:
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("your roots r1 and r2 are :",r1,r2)
elif d==0:
    r1=-b/(2*a)
    print ("your root is ",r1)
else:
    d=-1*d
    rl=-b/(2*a)
    imag=(d**0.5/(2*a))
    r1=complex(rl,imag)
    r2=r1.conjugate()
    print("your root r1 and r2 are",format(r1 ,r2),'0.2f')



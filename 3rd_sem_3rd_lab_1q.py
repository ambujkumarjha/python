#Write a program to find the greatest among three numbers.
n1=eval(input("Enter the 1st no."))
n2=eval(input("Enter the 2nd no."))
n3=eval(input("Enter the 3rd no."))
if(n1>=n2 and n2>=n3):
    print("The first no is greatest no. =",n1)
elif(n2>=n1 and n1>=n3):
    print("The second no is greatest no. =",n2)
else:
    print("The third no is gretest no is =",n3)

    
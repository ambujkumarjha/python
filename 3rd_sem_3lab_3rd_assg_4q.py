a = int(input("Enter the unit :"))
if(a>=0)and(a<=200):
    print("your electric bill is : ",format(a*0.5,'0.2f'))
elif(a>=201)and(a<=400):
    print("your electric bill is: ",format(100+(a*0.65),'0.2f'))
elif(a>=401)and(a<=600):
    print('your electric bill is: ',format(200+(a*0.80),'0.2f'))
else:
    print("your electric bill is: ",format(300+(a*1),'0.2f'))

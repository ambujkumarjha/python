
f1=open("new_10_c1.txt","w")
num =int(input("Enter the number :"))
a,b=0,1
sum=0
count=0
while(count<num):
    f1.write(str(sum)+" ")
    a=b
    b=sum
    sum = a+b
    count+=1
f1.close()
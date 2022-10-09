
f1=open("new_text2.txt","w")
n=int(input("Enter upper limit: "))
count=0
i=2
while count<n:
    for j in range (2,i):
        if (i%j==0):
            break
    else:
        f1.write(str( i )+" \n ")
        count= count+1
    i=i+1
f1.close()
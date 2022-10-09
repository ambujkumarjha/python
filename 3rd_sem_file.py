


'''w -Write
'r'-Read
"a"-Append'''
#"f1 =open("A:\\text123.txt","w")
#f1.write("welcome to my world in 2022")
#f1.close()""
#f1 =open("text123.txt","w")
#f1=open("A:\\text123.txt","r")
#s1=f1.readlines()
#print(s1)
f2=open("test321.txt","w")
for i in range (1,11):
    f2.write(str(i)+" ")
f2.close
f2=open("test321.txt","r")
print(f2.tell())
s1 =f2.readlines()
s2 =s1[0].split(" ")
for i in s2:
    print(int(i))
f2.close()
f2.seek(-2,2),#whence0 - starting.1 current and - End 
print(f2.tell())
s1=f2.read()
print(s1)

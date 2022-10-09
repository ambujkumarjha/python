str1=input("Enter an string:")
l2=[]
l3=[]
l1=str1.split()
for n in l1:
    if n.isalpha():
        l2.append(n)
        l3.append(l1.count(n))
t1= tuple(zip(l2,l3))
s1=set(t1)
d1=dict(s1)

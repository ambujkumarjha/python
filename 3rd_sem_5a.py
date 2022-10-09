print("Automorphic numbers are:-")
for i in range(10,100):
    sq=i**2
    rem=sq%100
    if i==rem:
        print(i,end=",")
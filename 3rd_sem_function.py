'''def func1(a,b,c):#default value (a,b=4,c=5)
    d = (a+b)//c
    e = (a+b)%c
    print(a,b,c)
    return d,e
l,m = func1(10,3,5)#positional assignemt
print(l,m)'''
'''def func2(l1,l2):
    13 = l1+l2
    return 13


a = [1,2,3]
b = [4,5,6]
print(func2(a,b))'''
# we can handel the logical errors : exception handling
#division by 0
#Built - in exception and user defined  exception;
#all the exception are child of exception class
'''def func1(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print ("DEvision by zero is not possible  try a different divisor ")
        b =eval(input("Enter a new value of b: "))
    finally:
            print("good bye ")
print(func1(10,0))'''
#user Defind exception


class MyException(Exception):
    pass
def func2(a,b):# a will be tne list and b will be an integer 
 #if b is greater  than ythe length of a - 1 than it will raise an exception (my exception) 
    try:
         if b> (len(a)-1):
             raise MyException
             print (a[b])
    except MyException:
            print("the ")



class MyException(Exception):
    pass

def rotatelst(l, n= 1,d="Left"):
    rl=[]
    length =len(1)
    try:
      if n>=length:
        raise MyException
        if d =="Left":  
          rl=[n:length]+1[0:n]
        if d =="Right":
         rl=[length-]+1[0:n]
    except MyException:
        print("The number of rotation is greater than the number of element")
        l1=l.copy
    finally:
            return l1


        
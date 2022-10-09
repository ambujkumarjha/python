def  wellbracketed(exp):
    stck =[]
    for i in exp:
        if i == "(":
            stck.append ("(")
            if  i==")":
                try:
                   stck.pop()
                except IndexError:
                    return False
    if len(stck)==0:
        return True
    else:
        return False
exp = input ("Enter an expression ")
if wellbracketed(exp):
    print(exp," is not well bracketed")
else:
    print(exp,"is not well bracketed")
    

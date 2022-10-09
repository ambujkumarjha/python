#A SPAM COMMENT IS DEFINDED AS A TEST CONTAINING FOLLOWING KEYWORDS 
# "MAKE A LOT OF MONEY ","BUY NOW","SUBSCRIBE THIS ","CL
# ICK THIS ",
# WRITE A PROGRAM TO DETECT THESE SPAMS.
text = input("Enter the text \n")

if("make a lot of money"in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True    
else:
    spam = False
    
if( spam ):
    print("This text is spam")
else:
    print("This is not a spam")
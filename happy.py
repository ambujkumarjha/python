s1 = "Hello world! "  
up= 0 
lw = 0 
for i in s1: 
 if(65 <= ord(i) <= 90): 
  up+=1 
 if(97 <= ord(i) < 122): 
    lw+=1 
 print(up,lw)


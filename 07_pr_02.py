# WRITE A PROGRAM TO FIND OUT WHETHER A STUDENT IS PASS OR FAIL
#  IF IT REQUIRES TOTAL 40% AND  AT LEAST  33% IN EACH SUBJECT TO PASS
#  ASSUME 3 SUBJECT AND TAKE MARKS  AS INPUT FROM THE USER
sub1 = int(input("Enter the marks of hindi: \n " ))
sub2 = int(input("Enter the marks of english: \n" ))
sub3 = int(input("Enter the marks of math : \n" ))
if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less marks in")
elif(sub1+sub2+sub3)/3<40:
     print("you are fail due to total percentage lessthan 40")
else:
     print("congatulations! you passed the exam")
# write a python program to check whether a year is leap year.
year= int(input("enter the year: "))
if (year%4==0 and year%100!=0)or(year%400==0):
    print("you entered year is leap year")
else :
    print("this is not a leap year ")
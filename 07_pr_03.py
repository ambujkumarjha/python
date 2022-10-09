# write a program to detect double spaces in a string
string = "write a program to detect double  spaces in a string"
#doublespaces = string.find("  ")
#print( doublespaces)
change = string.replace("  ","       ")
print(change)
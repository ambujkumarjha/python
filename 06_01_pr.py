# write a program to wrote a dictionary of hindi word with values as their english transltion provide 
# user with an option to look it up!
dict = {
    "mango":"aam",
    "monkey":"bander",
    "dog":"kutta"
}
print("option are ",dict.keys())
a = input("Enter the english word\n")
print("yahh!! here is your answer :",dict.get(a))
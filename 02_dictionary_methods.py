mydict = {
    "Fast": " In a quick manner ",
    "Harry": "A coder",
    "Marks": [1,2,5],
    "anotherdict": {'harry': 'player'},
    1: 2
}

#dictonary methods
print(list(mydict.keys()))# prints the keys of the dictionary
print(mydict.values())#print the all keys of the dictionary
print(mydict.items())# prints the (key, value) for all contant of the dictionary
print(mydict)
updatedict = {
    "kundan":"friend",
    "harsh":"friend",
    "rohit":"friend",
    "adil":"friend",
    "harry": "A bakchod"
    
    
}

mydict.update(updatedict) # update the dictionary by adding key - values pairs from updatedict
print(mydict)
print(mydict.get("harry"))# prints value associated with key "harry"
print(mydict.get["harry"])# it also print the value associated with key "harry" 
# THE DIFFERENCE  BETWEEN .get AND [] SYNTAX IN DICTIONARIES
print(mydict.get("harry2"))# it returns none as harry2 is not present in the dictionary
print(mydict.get("harry2"))# BUT it throws an error as harry2 is not present in the dictionary
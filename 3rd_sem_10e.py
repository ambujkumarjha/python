
f2 = open("new_text2.txt","r")
f2.seek(0,2)

print("size of file :", f2.tell(),"bytes")
f2.close()
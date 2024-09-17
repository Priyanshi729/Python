friendname = ["Chirag" , " Nikita" , "Shipra" , "Anupama"]
print("Before:",friendname)
friendname.append("Nidhi")
friendname.append("Khushi")
print("After : ",friendname)
friendname.insert(1,"Tushar")
print("After using indexing insert : ",friendname)
friendname.remove("Khushi")
print("After using remove function : ",friendname)
friendname.clear()
print(friendname)
friendname = ["Chirag" , " Nikita" , "Shipra" , "Anupama"]
print(friendname)
friendname.pop()
print("After using pop function : " , friendname)
friendname.pop(1)
print("After giving index in pop function : ",friendname)
friendname = ["Chirag" , " Nikita" , "Shipra" , "Anupama"]
friendname.sort()
print("After using sort function : ", friendname)
print("Printing using for loop")
for i in friendname:
    print(i)
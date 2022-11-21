# List operators
Languages = ["Yoruba", "English", "Spanish"]
print("List:", Languages)


Languages = ["Yoruba", "English", "Spanish",10 ]
print("List:", Languages)


# append -> add new line at the end of the list
Languages.append("Hausa")
print("append:", Languages)

# insert -> add a new at any position in the list
Languages.insert(0,"Igbo")
Languages.insert(4,"Japanese")
Languages.insert(7,"7")
print("insert:", Languages)

# POP -> remove an item from the specified  position
Languages.pop(6)
Languages.pop(0)
print("pop:", Languages)

# Remove -> remove an item by value
Languages.remove(10)
print("remove:", Languages)
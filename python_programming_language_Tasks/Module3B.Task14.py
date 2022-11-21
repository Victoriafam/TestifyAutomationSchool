#Lesson 14 Task
#Declare a string variable with any value
#Print out the string in the upper case form
#Note: you can experiment with the other functions call too in the task.

name = "My name is Ire Bada and my sister's name is Oreofe Bada"
# upper -> convert a string to upper case
upper_value = name.upper()
print("upper_value:", upper_value)

# lower_value -> convert a string to lower case
lower_value = name.lower()
print("lower_value:",lower_value)

#count => count the occurence of a value in a string
name_count = name.count("name")
print("name count:", name_count)

#count => count the occurence of a value in a string
Bada_count = name.count("Bada")
print("Bada count:", Bada_count)

#count => count the occurence of a value in a string
Ire_count = name.count("Ire")
print("Ire count:",Ire_count)

# find => find the postion of a value in a string
Ire_find =  name.find("Ire")
print("Ire find:", Ire_find)





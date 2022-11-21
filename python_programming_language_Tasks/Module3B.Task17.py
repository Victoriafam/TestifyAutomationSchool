#
#Lesson 17 Task
#1.	Create a class called Human
#2.	Initialize the class

# class
class Human:
    name = "Negroid"
    group = "Black"

    def get_name_group(self):
        return self.name + ":" + self.group
# objects
Negroid = Human()
print(Negroid.name, Negroid.group, Negroid.get_name_group())

Negroid2 = Human()
Negroid3 = Human()
Negroid4 = Human()
Negroid5 = Human()

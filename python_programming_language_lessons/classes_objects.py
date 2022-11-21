# class
class Animal:
    name = "Cow"
    group = "Mammal"

    def get_name_group(self):
        return self.name + ":" + self.group
# objects
Cow = Animal()
print(Cow.name, Cow.group, Cow.get_name_group())






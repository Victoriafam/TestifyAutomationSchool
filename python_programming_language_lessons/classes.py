class Animal:
    name = "cow"
    group = "mammal"

    def get_name_group(self):
        return self.name + ":" + self.group
    # objects
cow = Animal()
print(cow.name, cow.group, cow.get_name_group)()

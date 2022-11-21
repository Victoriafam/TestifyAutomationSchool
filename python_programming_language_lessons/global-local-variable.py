name = "Testify" # Global Variable 
def greetings():
    language = "Python" # local variable
    print("language", language)

    def hello():
        framework = "Selenium" # local variable
        print("Framework", framework)

greetings()
hello()

name = "Testify" # Global Variable
def greetings():
    language = "Python" # local variable
    print("language",name, "Language" language)
    def hello():
        framework ="Selenium" # local variable
        print("Framework",name ""framework", framework)

greetings()
hello()
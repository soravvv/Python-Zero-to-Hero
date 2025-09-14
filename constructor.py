class Person:
    def __init__(self, name, occupation):
        print("Hey I am a person")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Sorav", "SDE-2")
b = Person("Srishti", "Sales Executive")
a.info()
b.info()
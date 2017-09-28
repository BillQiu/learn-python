class Person():
    def __init__(self, name):
        self.name = name
    def sayName(self):
        print(self.name)

p = Person('Bill')
p.sayName()

class Person():
    def __init__(self, name='Incognito', age=0):
        self.name = name
        self.age = age

    def sayHello(self):
        print('Hello')

    def sayMyName(self):
        print(f'name is {self.name}')

    def __str__(self):
        return f'Person {self.name} {self.age}'


marizza = Person('Mary', 18)
print(marizza.name, marizza.age)
marizza.sayMyName()

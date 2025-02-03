class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()


    @classmethod
    def increase_population(cls) :
        cls.population += 1 # 생성될때 자동으로 올라갈때



person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #

Person.increase_population() 
print(Person.population)  


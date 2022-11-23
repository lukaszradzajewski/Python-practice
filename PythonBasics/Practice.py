class Animal:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def Hello(self):
        print(f"I am {self.name} and I am {self.age} and my owner is {self.owner}")

    def speak(self):
        print("I am some kind of animal :)")

    def change_owner(self, owner):
        self.owner = owner
        print(f"New owner is: {self.owner}")


class Dog(Animal):
    def __init__(self, name, age, owner, breed):
        super().__init__(name, age, owner)
        self.breed = breed

    def speak(self):
        print("Baark bark")


class Cat(Animal):
    def __init__(self, name, age, owner, breed):
        super().__init__(name, age, owner)
        self.breed = breed

    def speak(self):
        print("Meoow!")


misiek = Dog('misiek', 10, 'lukasz', 'kundel')
misiek.Hello()
misiek.speak()

misiek.change_owner('Ania')

# This is my return to OOP

class Dog:

    species = "lupus lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

    def jump(self):
        height = self.age * 0.20
        print(f"{self.name} is jumping some {height} mts. Amazing!")

    def describe(self):
        print(f"Our dog is called {self.name}. Age: {self.age}, and Breed: {self.breed}")

    def getSpecies(cls):
        return cls.species


#Objects (instances) of the class:
dog1 = Dog("Buddy", 4, "Cocker Spanniel")
dog2 = Dog("Pantufa", 5, "Grand Dannois")

#Callinga method on an object:
dog1.bark()
dog2.jump()

#Inheritance
class Goldenretriever(Dog):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed) # Calling the parent class constructor
        self.color = color

    def fetch(self):
        print(f"{self.name} is great at fetching balls!")

    def colorGrabber(self):
        print(f"The doggo will paint the walls {self.color}")

gold1 = Goldenretriever("Pete", 1, "Golden Retriever", "Purple")

gold1.bark()
gold1.jump()
gold1.colorGrabber()
gold1.describe()
print(gold1.color)

print(dog1.getSpecies())
print(dog2.species)
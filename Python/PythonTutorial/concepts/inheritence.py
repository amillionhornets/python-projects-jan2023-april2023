
#Super class that defines a dog
class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness
    def likeWalks(self):
        return True
    def bark(self):
        return "Woof!"
#Class the takes attributes from the super class to descibe a dog breed.
class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness) #Super takes all the attributes from the Dog's init

class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    def SheedingAmount(self):
        return 0
    def bark(self):
        return "Arf! Arf!"

class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    def fetchAbility(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7

class GoldenDoodle(Poodle, GoldenRetriever):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    def bark(self):
        return "AROOOOO!"



sammy = Samoyed('Sammy', 2, 10)
# print(sammy.name, sammy.age, sammy.friendliness)
# print(f"Does {sammy.name} like walks?: {sammy.likeWalks()}")

goldie = GoldenDoodle('Goldie', 3 , 10)
# print(goldie.name, goldie.age, goldie.friendliness)
# print(goldie.likeWalks())
# print(goldie.fetchAbility())
# print(goldie.SheedingAmount())
coolDog = Poodle("SWAG", 1 , 10)

print(goldie.bark())
print(sammy.bark())
print(coolDog.bark())
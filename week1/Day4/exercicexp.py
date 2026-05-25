# Exercise 1 : Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} walks quietly."


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"


bengal1 = Bengal("Leo", 3)
chartreux1 = Chartreux("Mimi", 5)
siamese1 = Siamese("Nala", 2)

all_cats = [bengal1, chartreux1, siamese1]
sara_pets = Pets(all_cats)

print("Exercise 1 : animals walking")
sara_pets.walk()


# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} barks."

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        if other_power > my_power:
            return f"{other_dog.name} won the fight!"
        return "It's a draw!"


dog1 = Dog("Rex", 3, 30)
dog2 = Dog("Buddy", 5, 20)
dog3 = Dog("Titan", 2, 40)

print("\nExercise 2 : dogs")
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"The running speed of {dog1.name} is {dog1.run_speed()}.")
print(f"The running speed of {dog2.name} is {dog2.run_speed()}.")
print(f"The running speed of {dog3.name} is {dog3.run_speed()}.")

print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog2.fight(dog3))


# Exercise 4 : Family
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        f"You are over 18 years old, your parents Jane and John "
                        f"allow you to go out with your friends."
                    )
                else:
                    print(
                        f"Sorry {first_name}, you are not allowed to "
                        f"go out with your friends."
                    )
                return
        print(f"Member {first_name} not found in the family.")

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"- {member.first_name} {member.last_name}, {member.age} years old")


famille = Family("Dupont")

famille.born("Alice", 20)
famille.born("Lucas", 15)
famille.born("Emma", 18)

print("\nExercise 4 : family")
famille.check_majority("Alice")
famille.check_majority("Lucas")
famille.check_majority("Emma")
famille.family_presentation()

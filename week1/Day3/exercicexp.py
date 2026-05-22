# ===== EXERCISE 1: CATS =====
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Shadow", 5)


# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest = max(cats, key=lambda cat: cat.age)
    return oldest


# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# ===== EXERCISE 2: DOGS =====
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 45)


# Step 3: Print dog details and call methods
print(f"\nDavid's dog: {davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"\nSarah's dog: {sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()


# Step 4: Compare dog sizes
print(f"\n{davids_dog.name} is {'taller' if davids_dog.height > sarahs_dog.height else 'shorter' if davids_dog.height < sarahs_dog.height else 'the same height as'} {sarahs_dog.name}")


# ===== EXERCISE 3: SONG =====
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Example usage
stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
print("\n--- Song Lyrics ---")
stairway.sing_me_a_song()


# ===== EXERCISE 4: ZOO =====
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
    
    def get_animals(self):
        print(f"Animals in {self.zoo_name}: {self.animals}")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
        self.animals.sort()
        return self._group_animals()
    
    def _group_animals(self):
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups
    
    def get_groups(self):
        groups = self.sort_animals()
        for letter in sorted(groups.keys()):
            print(f"{letter}: {groups[letter]}")


# Step 2: Create a zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the zoo methods
print("\n--- Zoo Management ---")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon")
brooklyn_safari.get_animals()

brooklyn_safari.add_animal("Lion", "Cougar", "Cat", "Zebra")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

print("\nGrouped animals (sorted by first letter):")
brooklyn_safari.get_groups()
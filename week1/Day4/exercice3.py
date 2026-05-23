# Exercice 3 : Chiens domestiqués
import random
from exercicexp import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        dog_names = [self.name] + list(args)
        dogs_string = ", ".join(dog_names)
        print(f"{dogs_string} jouent tous ensemble")
    
    def do_a_trick(self):
        if self.trained:
            tricks = ["fait une tonneau", "se tient sur ses pattes arrière", "te serre la main", "fait le mort"]
            print(f"{self.name} {random.choice(tricks)}")


# Tester les méthodes PetDog
print("=== Tests de la classe PetDog ===\n")

# Créer des instances PetDog
my_dog = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 3, 15)
max_dog = PetDog("Max", 4, 20)

# Tester la méthode train()
print("--- Entraînement de Fido ---")
my_dog.train()

# Tester la méthode play() avec plusieurs chiens
print("\n--- Jouer avec plusieurs chiens ---")
my_dog.play("Buddy", "Max")

# Tester la méthode do_a_trick()
print("\n--- Fido fait des tours ---")
my_dog.do_a_trick()

# Essayer un tour sans entraînement
print("\n--- Buddy essaie de faire un tour (non entraîné) ---")
buddy.do_a_trick()

# Entraîner Buddy et réessayer
print("\n--- Entraînement de Buddy ---")
buddy.train()
print("--- Buddy fait des tours ---")
buddy.do_a_trick()
buddy.do_a_trick()  # Le tour aléatoire sera différent
buddy.do_a_trick()

# Tester play() avec seulement le chien lui-même
print("\n--- Max joue seul ---")
max_dog.play()

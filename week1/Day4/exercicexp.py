# Exercice 1 : Animaux de compagnie
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} se promène simplement.'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Étape 1 — Classe Siamese (hérite de Cat)
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Étape 2 — Instances de chats
bengal1   = Bengal('Leo', 3)
chartreux1 = Chartreux('Mimi', 5)
siamese1  = Siamese('Nala', 2)

all_cats = [bengal1, chartreux1, siamese1]

# Étape 3 — Instance de Pets
sara_pets = Pets(all_cats)

# Étape 4 — Promenade
sara_pets.walk()

#Exercice 2

class Dog:
    # Étape 1 — Constructeur avec 3 attributs
    def __init__(self, name, age, weight):
        self.name   = name
        self.age    = age
        self.weight = weight

    def bark(self):
        return f'{self.name} aboie'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power    = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f'{self.name} a gagné le combat !'
        elif other_power > my_power:
            return f'{other_dog.name} a gagné le combat !'
        else:
            return 'Match nul !'


# Étape 2 — Trois instances de chien
dog1 = Dog('Rex',    3, 30)
dog2 = Dog('Buddy',  5, 20)
dog3 = Dog('Titan',  2, 40)

# Étape 3 — Tests
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())   # 30/3*10 = 100.0
print(dog2.run_speed())   # 20/5*10 = 40.0
print(dog3.run_speed())   # 40/2*10 = 200.0

print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog2.fight(dog3))

#Exercice 4

# ─── Étape 1 : Classe Person ───────────────────────────────

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age        = age
        self.last_name  = ""          # initialisé vide, assigné par Family

    def is_18(self):
        return self.age >= 18


# ─── Étape 2 : Classe Family ───────────────────────────────

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members   = []            # liste vide au départ

    # ── Étape 3 : ajouter un membre ──
    def born(self, first_name, age):
        new_person           = Person(first_name, age)
        new_person.last_name = self.last_name   # hérite du nom de famille
        self.members.append(new_person)

    # ── Étape 4 : vérifier la majorité ──
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"Tu as plus de 18 ans, tes parents Jane et John "
                          f"acceptent que tu sortes avec tes amis.")
                else:
                    print(f"Désolé {first_name}, tu n'as pas le droit de "
                          f"sortir avec tes amis.")
                return
        print(f"Membre '{first_name}' introuvable dans la famille.")

    # ── Présentation de la famille ──
    def family_presentation(self):
        print(f"=== Famille {self.last_name} ===")
        for member in self.members:
            print(f"  - {member.first_name} {member.last_name}, {member.age} ans")


# ─── Tests ─────────────────────────────────────────────────

famille = Family("Dupont")

famille.born("Alice", 20)
famille.born("Lucas", 15)
famille.born("Emma",  18)

famille.check_majority("Alice")
famille.check_majority("Lucas")
famille.check_majority("Emma")

famille.family_presentation()


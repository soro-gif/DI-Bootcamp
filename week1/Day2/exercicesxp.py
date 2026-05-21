# Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

#Exercice 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0

for name, age in family.items():
    if age < 3:
        ticket = 0
    elif age <= 12:
        ticket = 10
    else:
        ticket = 15
    total += ticket
    print(f"{name.capitalize()} ({age} ans) : ${ticket}")

print(f"Total : ${total}")

# Exercice 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print("Clients :", ", ".join(brand["type_of_clothes"]))
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")
print("Dernier compétiteur :", brand["international_competitors"][-1])
print("Couleurs US :", brand["major_color"]["US"])
print("Nb clés :", len(brand))
print("Clés :", list(brand.keys()))

# BONUS : fusion
more_on_zara = {"creation_date": 1975, "number_stores": 2}
brand.update(more_on_zara)
print("Après fusion :", brand)

#Exercice 4

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Abidjan", "Côte d'Ivoire")

#Exercice 5
import random

def check_number(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random: {random_number}")

check_number(50)
#Exercice 6

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")

# Bonus : arguments nommés
make_shirt(size="small", text="Hello!")

#Exercice 7

import random

def get_random_temp(month=None):
    if month is None:
        return round(random.uniform(-10, 40), 1)
    elif month in [12, 1, 2]:
        return round(random.uniform(-10, 5), 1)
    elif month in [3, 4, 5]:
        return round(random.uniform(8, 20), 1)
    elif month in [6, 7, 8]:
        return round(random.uniform(22, 40), 1)
    else:
        return round(random.uniform(5, 18), 1)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp}°C.")
    if temp < 0:
        print("Brrr, il fait froid ! Mets des vêtements chauds.")
    elif temp < 16:
        print("Il fait assez froid, n'oublie pas ton manteau.")
    elif temp < 24:
        print("Beau temps !")
    elif temp <= 32:
        print("Il fait chaud, pense à t'hydrater.")
    else:
        print("Il fait vraiment chaud ! Reste au frais.")

main()

#Exercice 8

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Entrez une garniture (ou 'quit') : ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total = base_price + len(toppings) * topping_price
print("\nYour pizza toppings:", toppings)
print(f"Total price: ${total:.2f}")

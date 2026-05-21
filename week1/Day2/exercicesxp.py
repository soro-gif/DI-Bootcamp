# Exercise 1: Convert Lists to Dictionaries

# Method 1: Using zip()
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Convert lists to dictionary using zip()
result = dict(zip(keys, values))
print("Method 1 (using zip()):")
print(result)

# Method 2: Using dictionary comprehension
result2 = {k: v for k, v in zip(keys, values)}
print("\nMethod 2 (using dictionary comprehension):")
print(result2)



# Exercise 2: Cinemax #2 - Movie Ticket Pricing


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Ticket pricing rules:
# Less than 3 years: free
# 3 to 12 years: $10
# More than 12 years: $15

print("=== BASIC SOLUTION ===\n")

total_cost = 0

for member, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(f"{member}'s ticket: ${ticket_price}")
    total_cost += ticket_price

print(f"\nTotal cost: ${total_cost}")

# Bonus: Interactive version with user input
print("\n=== BONUS: INTERACTIVE VERSION ===\n")

family_interactive = {}
total_interactive = 0

while True:
    name = input("Enter family member's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    
    try:
        age = int(input(f"Enter {name}'s age: "))
        family_interactive[name] = age
    except ValueError:
        print("Please enter a valid age.")
        continue

print("\n--- Ticket Prices ---")
for member, age in family_interactive.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(f"{member}'s ticket: ${ticket_price}")
    total_interactive += ticket_price

print(f"\nTotal cost: ${total_interactive}")

# Exercise 3: Zara - Dictionary Manipulation

# Create the Zara brand dictionary
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

print("=== ORIGINAL DICTIONARY ===")
print(brand)
print("\n")

# 1. Modify the number_stores to 2
brand["number_stores"] = 2
print("1. Modified number_stores to 2")
print(f"   number_stores: {brand['number_stores']}\n")

# 2. Print a sentence describing Zara's customers
print("2. Customer Description:")
clothes_types = ", ".join(brand["type_of_clothes"])
print(f"   Zara sells clothes for {clothes_types}.\n")

# 3. Add a new key country_creation with value Spain
brand["country_creation"] = "Spain"
print("3. Added country_creation key:")
print(f"   country_creation: {brand['country_creation']}\n")

# 4. Check if international_competitors exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print("4. Added 'Desigual' to international_competitors")
    print(f"   international_competitors: {brand['international_competitors']}\n")

# 5. Delete the creation_date key
del brand["creation_date"]
print("5. Deleted creation_date key\n")

# 6. Print the last element in international_competitors
print(f"6. Last competitor: {brand['international_competitors'][-1]}\n")

# 7. Print the major colors in the US
print(f"7. Major colors in US: {brand['major_color']['US']}\n")

# 8. Print the number of keys in the dictionary
print(f"8. Number of keys in brand dictionary: {len(brand)}\n")

# 9. Print all keys in the dictionary
print(f"9. All keys: {list(brand.keys())}\n")

# BONUS: Merge with another dictionary
print("=== BONUS SECTION ===\n")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

print("more_on_zara dictionary:")
print(more_on_zara)

# Merge the dictionaries
brand.update(more_on_zara)
print("\nAfter merging with brand:")
print(brand)

# Exercise 4: A Little Geography

def describe_city(city, country="Unknown"):
    """
    Describes a city and its country.
    
    Args:
        city (str): The name of the city
        country (str): The name of the country (default: "Unknown")
    """
    print(f"{city} is in {country}.")


# Test cases
print("=== Testing describe_city() ===\n")

# Example 1: With both city and country
describe_city("Reykjavik", "Iceland")

# Example 2: With only city (using default country)
describe_city("Paris")

# Example 3: More examples
describe_city("Tokyo", "Japan")
describe_city("New York")
describe_city("Berlin", "Germany")

# Example 4: Using keyword arguments
print("\n=== Using keyword arguments ===\n")
describe_city(city="Barcelona", country="Spain")
describe_city(country="France", city="Lyon")

# Exercise 5: Random

import random


def guess_number(user_number):
    """
    Compares user's number with a random number between 1 and 100.
    
    Args:
        user_number (int): The number to guess (between 1 and 100)
    """
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


# Test cases
print("=== Testing guess_number() ===\n")

# Example 1: Match scenario (unlikely but possible)
print("Test 1:")
guess_number(50)

print("\nTest 2:")
guess_number(75)

print("\nTest 3:")
guess_number(1)

# Interactive version
print("\n=== INTERACTIVE VERSION ===\n")

try:
    user_input = int(input("Enter a number between 1 and 100: "))
    
    if 1 <= user_input <= 100:
        guess_number(user_input)
    else:
        print("Please enter a number between 1 and 100.")
except ValueError:
    print("Please enter a valid number.")

# Exercise 6: Create Custom T-shirts!

def make_shirt(size="large", text="I love Python"):
    """
    Describes a custom t-shirt with size and message.
    
    Args:
        size (str): Size of the t-shirt (default: "large")
        text (str): Message on the t-shirt (default: "I love Python")
    """
    print(f"The size of the shirt is {size} and the text is {text}.")


# Test cases without modifications
print("=== INITIAL TESTS ===\n")

# Example 1: Large shirt with default message
make_shirt()

# Example 2: Custom size with default message
make_shirt("medium")

# Example 3: Custom size and message
make_shirt("small", "Hello World")

print("\n=== MODIFIED WITH DEFAULT VALUES ===\n")

# Step 5: Call with different configurations

# 1. Order a large t-shirt with default message
make_shirt()

# 2. Order a medium t-shirt with default message
make_shirt("medium")

# 3. Order a custom t-shirt with different size and message
make_shirt("small", "Custom message")

# Step 6 (Bonus): Using keyword arguments
print("\n=== USING KEYWORD ARGUMENTS ===\n")

make_shirt(size="extra-large", text="Python Developer")
make_shirt(text="Hello!", size="small")
make_shirt(size="XL")
make_shirt(text="Bootcamp 2024")

# Exercise 7: Temperature Advice

import random


def get_random_temp():
    """
    Returns a random temperature between -10 and 40 degrees Celsius.
    Basic version returns integer, bonus version returns float.
    """
    # Basic version: returns integer
    return random.randint(-10, 40)


def get_random_temp_float():
    """
    Bonus: Returns a random temperature between -10 and 40 degrees Celsius (float).
    """
    return random.uniform(-10, 40)


def main():
    """
    Main function that displays temperature and provides advice.
    """
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Provide advice based on temperature
    if temp < 0:
        print("Brrr, it's freezing! Wear extra clothes today.")
    elif 0 <= temp < 16:
        print("It's quite cold! Don't forget your coat.")
    elif 16 <= temp < 23:
        print("Beautiful weather.")
    elif 24 <= temp < 32:
        print("It's a bit hot, make sure to hydrate well.")
    elif temp >= 32:
        print("It's really hot! Stay cool.")


def main_float():
    """
    Bonus version with floating point temperatures.
    """
    temp = get_random_temp_float()
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")
    
    # Provide advice based on temperature
    if temp < 0:
        print("Brrr, it's freezing! Wear extra clothes today.")
    elif 0 <= temp < 16:
        print("It's quite cold! Don't forget your coat.")
    elif 16 <= temp < 23:
        print("Beautiful weather.")
    elif 24 <= temp < 32:
        print("It's a bit hot, make sure to hydrate well.")
    elif temp >= 32:
        print("It's really hot! Stay cool.")


def main_with_season():
    """
    Bonus version 2: Ask for month and determine season-specific temperature.
    """
    try:
        month = int(input("Enter a month (1-12): "))
        
        if not 1 <= month <= 12:
            print("Please enter a month between 1 and 12.")
            return
        
        # Determine season and get appropriate temperature
        if month in [12, 1, 2]:  # Winter
            temp = random.randint(-10, 0)
            season = "Winter"
        elif month in [3, 4, 5]:  # Spring
            temp = random.randint(5, 15)
            season = "Spring"
        elif month in [6, 7, 8]:  # Summer
            temp = random.randint(25, 40)
            season = "Summer"
        else:  # Fall (9, 10, 11)
            temp = random.randint(10, 20)
            season = "Fall"
        
        print(f"\n{season} - The temperature right now is {temp} degrees Celsius.")
        
        # Provide advice based on temperature
        if temp < 0:
            print("Brrr, it's freezing! Wear extra clothes today.")
        elif 0 <= temp < 16:
            print("It's quite cold! Don't forget your coat.")
        elif 16 <= temp < 23:
            print("Beautiful weather.")
        elif 24 <= temp < 32:
            print("It's a bit hot, make sure to hydrate well.")
        elif temp >= 32:
            print("It's really hot! Stay cool.")
    
    except ValueError:
        print("Please enter a valid month number.")


# Run the basic version
print("=== BASIC VERSION ===\n")
main()

# Run the float version
print("\n=== BONUS: FLOAT VERSION ===\n")
main_float()

# Run the seasonal version (interactive)
print("\n=== BONUS: SEASONAL VERSION (INTERACTIVE) ===\n")
main_with_season()

# Exercise 8: Pizza Toppings

def add_pizza_toppings():
    """
    Asks user to input pizza toppings one by one and calculates total price.
    Base price: $10, each topping adds $2.50
    """
    toppings = []
    base_price = 10
    price_per_topping = 2.50
    
    print("=== PIZZA BUILDER ===")
    print("Enter pizza toppings one by one. Type 'quit' to finish.\n")
    
    while True:
        topping = input("Enter a topping (or 'quit' to finish): ")
        
        if topping.lower() == 'quit':
            break
        
        if topping.strip():  # Check if input is not empty
            toppings.append(topping)
            print(f"Adding {topping} to your pizza.")
    
    # Calculate total price
    total_price = base_price + (len(toppings) * price_per_topping)
    
    # Display summary
    print("\n=== PIZZA SUMMARY ===")
    print(f"Base price: ${base_price}")
    print(f"Number of toppings: {len(toppings)}")
    
    if toppings:
        print("\nToppings:")
        for i, topping in enumerate(toppings, 1):
            print(f"  {i}. {topping}")
    else:
        print("\nNo toppings added.")
    
    print(f"\nPrice per topping: ${price_per_topping}")
    print(f"Total price: ${total_price:.2f}")


# Run the pizza builder
add_pizza_toppings()

# Optional: Alternative version with additional features
def add_pizza_toppings_advanced():
    """
    Advanced version with menu options and special deals.
    """
    toppings = []
    base_price = 10
    price_per_topping = 2.50
    
    print("\n=== PIZZA BUILDER (ADVANCED VERSION) ===")
    print("Enter pizza toppings one by one. Type 'quit' to finish.\n")
    
    while True:
        topping = input("Enter a topping (or 'quit' to finish): ").strip()
        
        if topping.lower() == 'quit':
            break
        
        if topping:
            if topping not in toppings:
                toppings.append(topping)
                print(f"Adding {topping} to your pizza.")
            else:
                print(f"{topping} is already on your pizza!")
        else:
            print("Please enter a valid topping.")
    
    # Calculate total price with discount
    number_of_toppings = len(toppings)
    subtotal = base_price + (number_of_toppings * price_per_topping)
    
    # Apply discount if more than 4 toppings
    discount = 0
    if number_of_toppings > 4:
        discount = subtotal * 0.1  # 10% discount
    
    total_price = subtotal - discount
    
    # Display summary
    print("\n=== PIZZA SUMMARY ===")
    print(f"Base price: ${base_price:.2f}")
    print(f"Number of toppings: {number_of_toppings}")
    
    if toppings:
        print("\nToppings:")
        for i, topping in enumerate(toppings, 1):
            print(f"  {i}. {topping}")
    else:
        print("\nNo toppings added.")
    
    print(f"\nPrice calculation:")
    print(f"  Base: ${base_price:.2f}")
    print(f"  Toppings: {number_of_toppings} × ${price_per_topping:.2f} = ${number_of_toppings * price_per_topping:.2f}")
    
    if discount > 0:
        print(f"  Discount (10%): -${discount:.2f}")
    
    print(f"\nTotal price: ${total_price:.2f}")


# Uncomment to run the advanced version
# add_pizza_toppings_advanced()

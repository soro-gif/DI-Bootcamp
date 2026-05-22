class Farm:
    def __init__(self, farm_name):
        """Initialize the Farm with a name and an empty animals dictionary."""
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        """
        Add animals to the farm.
        Can be called in two ways:
        1. add_animal('cow', 5) - adds 5 cows
        2. add_animal(cow=5, sheep=2, goat=12) - adds multiple animals at once
        """
        # If animal_type is provided, add it
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        
        # If kwargs are provided, add them
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_animal_types(self):
        """Return a sorted list of all animal types on the farm."""
        return sorted(self.animals.keys())

    def get_info(self):
        """
        Return a formatted string with farm info, animals, and counts.
        """
        info = f"{self.name}'s farm\n\n"
        
        # Add each animal with its count
        for animal_type in self.get_animal_types():
            info += f"{animal_type} : {self.animals[animal_type]}\n"
        
        # Add the signature phrase
        info += "\n    E-I-E-I-0!"
        
        return info

    def get_short_info(self):
        """
        Return a short sentence describing the farm and its animals.
        Example: "La ferme de McDonald possède des vaches, des chèvres et des moutons."
        """
        animal_types = self.get_animal_types()
        
        # Build the animal list with proper pluralization
        animal_list = []
        for animal in animal_types:
            count = self.animals[animal]
            # Add 's' if count > 1
            animal_name = animal if count == 1 else animal + "s"
            animal_list.append("des " + animal_name)
        
        # Join with commas and 'et' before the last item
        if len(animal_list) == 0:
            animals_str = ""
        elif len(animal_list) == 1:
            animals_str = animal_list[0]
        else:
            animals_str = ", ".join(animal_list[:-1]) + " et " + animal_list[-1]
        
        return f"La ferme de {self.name} possède {animals_str}."


# Test the code
if __name__ == "__main__":
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    
    print(macdonald.get_info())
    print("\n")
    print(macdonald.get_short_info())
    
    # Test the bonus feature with **kwargs
    print("\n--- Test with **kwargs ---")
    farm2 = Farm("Johnson")
    farm2.add_animal(cow=3, horse=2, pig=5)
    print(farm2.get_info())
    print("\n")
    print(farm2.get_short_info())

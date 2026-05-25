"""
Exercise 3: Dogs Domesticated
Create a PetDog class that inherits from Dog and adds training and tricks.

Key Python Topics:
- Inheritance
- super() function
- *args
- Random module
"""

import random


# Step 1: Define the Dog class (from Exercise 2)
class Dog:
    """A dog class with basic attributes and behaviors."""
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} barks."

    def run_speed(self):
        """Calculate running speed based on weight and age."""
        return self.weight / self.age * 10

    def fight(self, other_dog):
        """Determine which dog wins in a fight."""
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        if other_power > my_power:
            return f"{other_dog.name} won the fight!"
        return "It's a draw!"


# Step 2: Create the PetDog Class
class PetDog(Dog):
    """
    A Pet Dog class that inherits from Dog and adds training and tricks.
    """
    
    def __init__(self, name, age, weight):
        """
        Initialize a PetDog with name, age, weight, and a trained attribute.
        
        Args:
            name (str): The name of the dog
            age (int): The age of the dog
            weight (int): The weight of the dog
        """
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        """
        Train the dog by having it bark and setting trained to True.
        """
        print(self.bark())
        self.trained = True

    def play(self, *args):
        """
        Play with multiple dogs.
        
        Args:
            *args: Variable number of dog names (strings) or dog instances
        """
        # Extract dog names from arguments
        dog_names = []
        for arg in args:
            if isinstance(arg, PetDog) or isinstance(arg, Dog):
                dog_names.append(arg.name)
            else:
                dog_names.append(str(arg))
        
        # Add this dog to the list
        all_dogs = [self.name] + dog_names
        
        # Print the play message
        dogs_str = ", ".join(all_dogs)
        print(f"{dogs_str} all play together")

    def do_a_trick(self):
        """
        Perform a random trick if the dog is trained.
        
        Tricks:
        - does a barrel roll
        - stands on his back legs
        - shakes your hand
        - plays dead
        """
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            random_trick = random.choice(tricks)
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not trained yet!")



# Step 3: Test PetDog Methods


if __name__ == "__main__":
    
    print("EXERCISE 3: DOGS DOMESTICATED - PetDog Class")
  
    
    # Create PetDog instances
    print("\n1. Creating PetDog instances:")
    fido = PetDog("Fido", 2, 10)
    buddy = PetDog("Buddy", 3, 15)
    max_dog = PetDog("Max", 1, 8)
    
    print(f"   Created: {fido.name}, {buddy.name}, {max_dog.name}")
    
    # Test before training
    print("\n2. Testing do_a_trick() before training:")
    fido.do_a_trick()
    
    # Train the first dog
    print("\n3. Training Fido:")
    fido.train()
    print(f"   Fido is trained: {fido.trained}")
    
    # Do tricks after training
    print("\n4. Fido doing tricks (trained):")
    for i in range(3):
        fido.do_a_trick()
    
    # Play with multiple dogs
    print("\n5. Playing with multiple dogs:")
    fido.play(buddy, max_dog)
    
    # Play with dog names as strings
    print("\n6. Playing with dog names as strings:")
    buddy.play("Buddy", "Charlie", "Daisy")
    
    # Train more dogs
    print("\n7. Training more dogs:")
    buddy.train()
    max_dog.train()
    
    # Multiple dogs doing tricks
    print("\n8. Multiple trained dogs doing tricks:")
    fido.do_a_trick()
    buddy.do_a_trick()
    max_dog.do_a_trick()
    
    # Test inherited methods
    print("\n9. Testing inherited Dog methods:")
    print(f"   {fido.name}'s run speed: {fido.run_speed():.2f} km/h")
    print(f"   {buddy.name}'s run speed: {buddy.run_speed():.2f} km/h")
    
    print(f"\n   Fight result: {fido.fight(buddy)}")
    
    # Advanced test: play with mixed dog instances
    print("\n10. Advanced play test with dog instances:")
    fido.play(buddy, max_dog, "Sophie")
    
 
    print("End of Exercise 3 demonstration!")
   

import random


class Game:
    """Class to manage a single game of Rock-Paper-Scissors against the computer."""
    
    def get_user_item(self):
        """
        Ask the user to choose an item (rock/paper/scissors).
        Validates input and repeats until a valid choice is made.
        Returns the user's choice as a string.
        """
        valid_choices = ['r', 'p', 's']
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        
        while True:
            user_input = input("Select (r)ock, (p)aper or (s)cissors: ").lower().strip()
            
            if user_input in valid_choices:
                return choice_map[user_input]
            else:
                print("Invalid choice. Please enter 'r', 'p', or 's'.")
    
    def get_computer_item(self):
        """
        Randomly select rock, paper, or scissors for the computer.
        Returns the computer's choice as a string.
        """
        items = ['rock', 'paper', 'scissors']
        return random.choice(items)
    
    def get_game_result(self, user_item, computer_item):
        """
        Determine the result of the game by comparing user and computer items.
        
        Parameters:
        - user_item: the item chosen by the user (rock/paper/scissors)
        - computer_item: the item chosen by the computer (rock/paper/scissors)
        
        Returns:
        - 'win' if the user won
        - 'draw' if it's a tie
        - 'loss' if the user lost
        """
        if user_item == computer_item:
            return 'draw'
        
        # Check for winning conditions
        winning_conditions = {
            ('rock', 'scissors'): 'win',      # Rock beats scissors
            ('paper', 'rock'): 'win',         # Paper beats rock
            ('scissors', 'paper'): 'win'      # Scissors beats paper
        }
        
        if (user_item, computer_item) in winning_conditions:
            return 'win'
        else:
            return 'loss'
    
    def play(self):
        """
        Play one round of Rock-Paper-Scissors against the computer.
        
        This method:
        1. Gets the user's item choice
        2. Gets a random item for the computer
        3. Determines the result
        4. Displays the result message
        5. Returns the result as a string ('win', 'draw', or 'loss')
        """
        # Get user choice
        user_item = self.get_user_item()
        
        # Get computer choice
        computer_item = self.get_computer_item()
        
        # Determine result
        result = self.get_game_result(user_item, computer_item)
        
        # Display result
        result_message_map = {
            'win': "You won!",
            'draw': "It's a draw!",
            'loss': "You lost."
        }
        
        print(f"\nYou chose {user_item}. The computer chose {computer_item}. {result_message_map[result]}\n")
        
        return result

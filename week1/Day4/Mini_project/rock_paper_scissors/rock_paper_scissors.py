from game import Game
def get_user_menu_choice():
    """
    Display a simple menu and get the user's choice.
    Validates the input before returning.
    
    Returns:
    - 'play' if user chooses to play
    - 'scores' if user chooses to view scores
    - 'quit' if user chooses to quit
    """
    print("\n Menu")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    print("\n")
    
    valid_choices = ['g', 'x']
    
    while True:
        user_choice = input(" : ").lower().strip()
        
        if user_choice not in valid_choices:
            print("Invalid choice. Please enter 'g' or 'x'.")
            continue
        
        if user_choice == 'g':
            return 'play'
        elif user_choice == 'x':
            return 'quit'

def print_results(results):
    """
    Display the results of all games played.
    Takes a dictionary with keys 'win', 'loss', and 'draw'.
    
    Parameters:
    - results: a dictionary with format {'win': int, 'loss': int, 'draw': int}
    """
   
    print("Game Results :")
  
    print(f"You won   {results['win']} times")
    print(f"You lost  {results['loss']} times")
    print(f"You drew:  {results['draw']} times")  
    print("Thank you for playing !")

def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    
    Handles:
    1. Displaying the menu in a loop until the user quits
    2. Creating a new Game object and playing when requested
    3. Tracking all game results
    4. Displaying final results when the user quits
    """
    # Initialize results dictionary
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    # Main loop
    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice == 'play':
            # Create a new game and play
            game = Game()
            result = game.play()
            
            # Track the result
            results[result] += 1
        
        elif user_choice == 'quit':
            # Quit the game
            print_results(results)
            break


if __name__ == '__main__':
    main()

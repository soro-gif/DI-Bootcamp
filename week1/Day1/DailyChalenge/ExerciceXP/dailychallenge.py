
# Challenge 1 : List of Multiples

def generate_multiples():
    """
    Ask the user for a number and a length.
    Create and display a list of multiples of the number.
    """
    try:
        # Ask the user for a number
        number = int(input("Enter a number: "))
        
        # Ask the user for the desired length
        length = int(input("Enter the length of the list: "))
        
        # Create a list of multiples
        multiples = [number * i for i in range(1, length + 1)]
        
        # Display the final list
        print("List of multiples:", multiples)
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")



# Challenge 2 : Remove Consecutive Duplicate Letters


def remove_consecutive_duplicates():
    """
    Ask the user for a word and remove consecutive duplicate letters.
    """
    word = input("Enter a word: ")
    
    if not word:
        print("")
    else:
        # Use a list for efficient string building
        char_list = [word[0]]
        for letter in word[1:]:
            if letter != char_list[-1]:
                char_list.append(letter)
        print(''.join(char_list))


# Main Execution


if __name__ == "__main__":
    generate_multiples()
    print('\n' + '-'*20 + '\n')
    remove_consecutive_duplicates()

# 
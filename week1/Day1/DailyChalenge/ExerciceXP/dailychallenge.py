# =========================================================
# Challenge 1 : List of Multiples
# =========================================================

# Ask the user for a number
number = int(input("Enter a number: "))

# Ask the user for the desired length
length = int(input("Enter the length of the list: "))

# Create an empty list
multiples = []

# Loop to generate multiples
for i in range(1, length + 1):

    # Add multiples to the list
    multiples.append(number * i)

# Display the final list
print("List of multiples:", multiples)

#Challenge 2 : Remove Consecutive Duplicate Letters

word = input("Enter a word: ")
result = word[0]
for letter in word[1:]:
    if letter != result[-1]:
        result += letter
print(result)
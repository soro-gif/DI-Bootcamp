# Exercise 1
#Print the following output using one line of code:

print((" Hello World\n")*4)

# Exercise 2
#Write code that calculates the result of:

print((99 ** 3) * 8)

# Exercise 3
#Predict the output of the following code snippets:
#Comment what is your guess, then run the code and compare

5 < 3 # False
3 == 3 # True
3 == "3" # False
"3" > 3 # TypeError
"Hello" == "hello" # False

# Exercise 4
#Create a variable called computer_brand and assign it the value of your computer brand. Then print a sentence that says "I have a [computer_brand] computer".

computer_brand = "Lenovo"
print("I have a " + computer_brand + " computer")
# Exercise 5
name = "Soro"
age = 29
shoe_size = 43
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
print(info)

# Exercise 6
#Create two variables, a and b. Assign them any number values you want. Write code that checks if a is greater than b. If it is, print "Hello World".

a = 5
b = 3
if a > b:
    print("Hello World")

# Exercise 7
#Write code that asks the user for a number and determines if the number is even or odd. Print "The number is even" or "The number is odd" accordingly.

number = input("Enter a number: ")
if int(number) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
# Exercise 8
user_name = input("Enter your name: ")
if user_name == "Alice" or user_name == "Bob":
    print("Welcome " + user_name)
# Exercise 9
user_height = input("Enter your height in cm: ")
if int(user_height) >145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride.")
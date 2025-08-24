# Create a list of 5 fruits and print the third fruit.
fruits=["mango","banana","orange","apple","grape"]
print(fruits[2])

# Create a dictionary with keys: name, age. Print the value of age.
person={"name":"John","age":30}
print(person["age"])
# Define a tuple with three numbers. Try modifying it. What happens?
numbers=(1,2,3)
# numbers.append(6)

# Create a set from a list with duplicate values.
duplicates=[2,2,3,3,4,4]
duplicates=set(duplicates)  
print(duplicates)
# Challenge
# Create a program that:

# Takes 5 user inputs and stores them in a list
# Converts the list into a set and prints the unique values
user_inputs=[]
for i in range(5):
    value=input("Enter a value:")
    user_inputs.append(value)
unique_values=set(user_inputs)
print("The unique values are:",unique_values)

# Use a for loop to print numbers from 1 to 10.
for i in range(1,10):
    print(i)
# Use a while loop to print numbers until the user enters stop.
# Write a loop that prints even numbers from 1 to 20.
# Explain what break and continue do in your own words.
# Challenge
# Write a guessing game that asks the user to guess a secret number between 1 and 10.

# Give feedback (too high / too low)
# Use a while loop
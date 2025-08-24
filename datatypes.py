# Print the type of 42, 3.14, and 'hello'.
num=42
print(type(num))
print(type(3.14))
print(type("Hello"))

# Convert a string '100' to an integer.
str_num="100"
int_num=int(str_num)
print(int_num)
# Add an integer and a float together. What is the result?
sum=20+10.35
print(sum)
# What happens when you try to multiply a string by a number?
multiply="Jambo"*4
print(multiply)

# Asks the user to enter two numbers (as strings)
# Converts them to integers or floats
 # Prints their sum and type
num1=input("Enter first number:")
num2=input("Enter second number:")
 
num1=float(num1)
num2=float(num2)
sum= num1+num2
print("The sum is",sum)
print("The type is",type(sum))

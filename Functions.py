# Write a function greet(name) that prints “Hello, [name]”.
# def greet(name):
#      print("Hello",name)
# greet("Shamim")


# Create a function add(a, b) that returns the sum.
# def add(a,b):
#     return a+b
# print(add(3,9))
 

# Modify add() to print “even” or “odd” based on the result.
def add(a,b):
    sum=a+b
    if sum%2==0:
        print("even")
    else:
        print("odd")
    return sum 
print(add(21,9)) 


# Call a function from within another function.
# Challenge
# Write a calculator function:

# Takes two numbers and an operation (+, -, *, /)
# Returns the result
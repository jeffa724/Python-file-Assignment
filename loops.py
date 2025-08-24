# Use a for loop to print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)
# Use a while loop to print numbers until the user enters stop.
# while True:
#     user=input(":")
#     if user.lower()=="stop":
#         break
#     print("user")
    

# Write a loop that prints even numbers from 1 to 20.
for i in range(1,21):
    if i%2==0:
        print(i)
# Explain what break and continue do in your own words.
# break stops the loop entirely when a certain condition is met.
# continue skips the current iteration and moves to the next one when a certain condition is met.
# Challenge
# Write a guessing game that asks the user to guess a secret number between 1 and 10.

# Give feedback (too high / too low)
# Use a while loop
secret_number=7
while True:
    guess=int(input("Guess the secret number between 1 and 10:"))
    if guess<secret_number:
        print("Too low!")
    elif guess>secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break

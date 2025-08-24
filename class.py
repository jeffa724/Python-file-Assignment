# # Define a class named Student with the following attributes:
# # name
# # age
# # grade
# # Create a method display_info() that prints the student's details.
# # Create three student objects and call the method for each to display their details.
# class Student:

#     def __init__(self, name, age, grade):
#          self.name = name
#          self.age = age
#          self.grade = grade

        
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        
# s1 = Student("John", 20, "A")
# s2 = Student("Grace", 22, "B")
# s3 = Student("Tina", 19, "A+")

# s1.display_info()
# s2.display_info()
# s3.display_info()

# Instance vs Class Methods
# Define a class named BankAccount with:
# account_number
# balance
# Add methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Add a class variable to store the bank name and a class method to display the bank name.
# Create two account objects and perform deposits and withdrawals.
class BankAccount:
    bank_name = "Global Bank"  # Class variable

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    @classmethod
    def display_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")

# Create account objects
account1 = BankAccount("123456", 1000)
account2 = BankAccount("654321", 500)
# Perform operations
account1.deposit(200)
account1.withdraw(150)
account1.display_balance()
account2.deposit(300)
account2.withdraw(800)
account2.display_balance()

BankAccount.display_bank_name()
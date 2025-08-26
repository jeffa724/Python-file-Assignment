# # Define a class named Student with the following attributes:
# # name
# # age
# # grade
# # Create a method display_info() that prints the student's details.
# # Create three student objects and call the method for each to display their details.
class Student:

    def __init__(self, name, age, grade):
         self.name = name
         self.age = age
         self.grade = grade

        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        
s1 = Student("John", 20, "A")
s2 = Student("Grace", 22, "B")
s3 = Student("Tina", 19, "A+")

s1.display_info()
s2.display_info()
s3.display_info()

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
    

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance =self.balance + amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance =self.balance -amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
        
    @classmethod
    def bank_name(cls):
        return "Global Bank"

   

# Create account objects
account1 = BankAccount("123456", 1000)

# Perform operations
account1.deposit(200)
account1.withdraw(150)
account1.display_balance()


# Create a class Car with:
# Private attributes: __make, __model, __year, __speed
# Methods to:
# Get and set make, model, and year.
# Increase and decrease speed.
# Display all car details.
# Create a Car object, update its attributes, and demonstrate encapsulation.

class Car:
    def __innit___(self,make,model,year,speed):
        self.make=make
        self.model=model
        self.year=year
        self.speed=speed
        
    def get_make(self):
        return self.make
    
    def set_make(self,make):
        self.make=make 
        # model
    def get_model(self):
        return self.model
    
    def set_model(self,model):
        self.model=model
        
        # year
        
    def get_year(self):
        return self.year
    
    def set_year(self,year):
        self.year=year
        
    # speed
    def increse_speed(self,speed):
        if speed>0:
            self.speed=self.speed+speed
        else:
            print("speed not increased")
        
        # decrease speed
        def decrease_speed(self,speed):
            if speed>0:
                self.speed=self.speed-speed
            else:
                print("speed not decreased")
    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Speed: {self.speed} km/h")   
        
                
    
                
                
        
    (one, two):
        """
        Purpose: one
        """
        
    # end def
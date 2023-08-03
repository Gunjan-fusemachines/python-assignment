# BankAccount and Customer classes in Python to represent a simple banking system
class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"BankAccount with account number {self.account_number} is being destroyed.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(self.generate_account_number(), 0, "Savings")

    def __del__(self):
        print(f"Customer {self.name} with account number {self.bank_account.account_number} is being destroyed.")

    def generate_account_number(self):
        # In a real banking system, you would generate a unique account number here.
        # For simplicity, we use a static counter for demonstration purposes.
        Customer.account_counter = getattr(Customer, "account_counter", 1000) + 1
        return f"ACC{Customer.account_counter}"


# Create a customer and bank account objects
customer1 = Customer("John Doe", 30, "123 Main St")
customer2 = Customer("Jane Smith", 25, "456 Park Ave")

# Access customer details
print(f"Customer 1: {customer1.name}, {customer1.age} years old, Address: {customer1.address}")
print(f"Customer 2: {customer2.name}, {customer2.age} years old, Address: {customer2.address}")

# Access bank account details for each customer
print(f"Bank Account for Customer 1: Account Number: {customer1.bank_account.account_number}, Balance: {customer1.bank_account.balance}, Type: {customer1.bank_account.account_type}")
print(f"Bank Account for Customer 2: Account Number: {customer2.bank_account.account_number}, Balance: {customer2.bank_account.balance}, Type: {customer2.bank_account.account_type}")

# The objects will be destroyed when the program ends

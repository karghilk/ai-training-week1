
# ==========================================
# WEEK 1 - DAY 1
# TASK 1: BANK ACCOUNT CLASS
# ==========================================

# 1. Create a custom exception

class InsufficientFundsError(Exception):
    pass


# 2. Create Account class

class Account:

    # Constructor
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Deposit method
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    # Withdraw method
    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        self.balance -= amount

        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

    # Show method
    def show(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: {self.balance}")


# 3. Create an object

account1 = Account("Arun", 1000)


# 4. Perform transactions using exception handling

try:
    account1.deposit(500)

    account1.withdraw(2000)

except InsufficientFundsError as e:
    print("Error:", e)

finally:
    print("Transaction finished")

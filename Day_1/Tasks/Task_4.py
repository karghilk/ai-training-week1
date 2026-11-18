
# ==========================================
# WEEK 1 - DAY 1
# TASK 2: INHERITANCE AND OVERRIDING
# ==========================================

# 1. Custom exception

class InsufficientFundsError(Exception):
    pass


# 2. Parent class

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

    def show(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


# 3. Child class

class SavingsAccount(Account):

    def __init__(self, owner, balance=0, min_balance=500):

        # Reuse parent constructor
        super().__init__(owner, balance)

        # Extra attribute
        self.min_balance = min_balance

    # Override withdraw method
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self.balance - amount < self.min_balance:

            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount

        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")


# 4. Create Priya's savings account

priya = SavingsAccount("Priya", 1500)


# 5. Test withdrawals

for amount in [1200, 800]:

    try:
        priya.withdraw(amount)

    except InsufficientFundsError as e:
        print("Error:", e)


# 6. Check inheritance

print(isinstance(priya, Account))

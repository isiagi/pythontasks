class BankAccount:
    # A class-level variable representing bank users
    bank_users = [{"acc_no": 1, "acc_balance": 100}, {"acc_no": 2, "acc_balance": 0}]

    def __init__(self, account_number, balance=0):
        # Initialize a bank account with an account number and an optional initial balance
        self.account_number = account_number
        self.balance = balance

    def find_user(self):
        # Find a user in the bank_users list based on the account number
        for user in self.bank_users:
            if user["acc_no"] == self.account_number:
                return user
        return None

    def check_user(self):
        # Check if the user with the specified account number exists
        user = self.find_user()
        if user is None:
            print(f"{self.account_number} account number is not registered")
            return False
        return True

    def deposit(self, amount, name):
        # Deposit money into the account if the user exists
        if self.check_user():
            user = self.find_user()
            user["acc_balance"] += amount
            print(f'{name} deposited {amount} and new balance is {user["acc_balance"]}')

    def withdrawal(self, amount, name):
        # Withdraw money from the account if the user exists and has sufficient balance
        if self.check_user():
            user = self.find_user()
            if user["acc_balance"] >= amount:
                user["acc_balance"] -= amount
                print(
                    f'{name} withdrew {amount} and new balance is {user["acc_balance"]}'
                )
            else:
                print(f"Insufficient balance for {name}")

    def account_balance(self, name):
        # Check and print the account balance for the user if they exist
        if self.check_user():
            user = self.find_user()
            print(f'{name} Account balance is {user["acc_balance"]}')


# Create two bank account instances
tom_account = BankAccount(1)
sarah_account = BankAccount(2)

# Perform deposit and withdrawal operations on the accounts
sarah_account.account_balance("Sarah")
tom_account.deposit(4000, "Tom")
sarah_account.withdrawal(40, "Sarah")

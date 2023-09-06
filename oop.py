import operator


class Bank_Account:
    # A class-level variable representing bank users
    bank_users = [{"acc_no": 1, "acc_balance": 100}, {"acc_no": 2, "acc_balance": 0}]

    def __init__(self, account_number, balance=0):
        # Constructor initializes the account with an account number and balance
        self.account_number = account_number
        self.__balance = balance  # Double underscore indicates private attribute

    def check_user(self):
        # Check if the user's account number is registered
        user_num = operator.itemgetter("acc_no")
        users = map(user_num, self.bank_users)

        user_acc_num = self.account_number

        if user_acc_num not in users:
            print(f"Acount number {user_acc_num} is not registered")
            return

    def deposit(self, amount, name):
        # Deposit money into the account
        self.check_user()

        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                item["acc_balance"] += int(amount)
                print(
                    f'{name} deposited {amount} and new balance is {item.get("acc_balance")}'
                )
                return

    def withdrawal(self, amount, name):
        # Withdraw money from the account
        self.check_user()
        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                item["acc_balance"] -= int(amount)
                print(
                    f'{name} withdrew {amount} and new balance is {item.get("acc_balance")}'
                )
                return

    def account_balance(self, name):
        # Check and print the account balance
        self.check_user()
        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                print(f'{name} Account balance is {item["acc_balance"]}')
                return


# Create two bank account instances
tom_account = Bank_Account(1)
sarah_account = Bank_Account(5)

# Perform deposit and withdrawal operations on the accounts
sarah_account.account_balance("Sarah")
tom_account.deposit(4000, "Tom")
sarah_account.withdrawal(40, "Sarah")

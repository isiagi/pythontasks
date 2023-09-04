# Create a bankaccount class with attributes: account number, balance.
# implement methods for deposit, withdrawal and displaying account balance.
# instantiate two accounts objects and perform transaction.

# Let users choose if they want to deposit, withdraw or display balance.

# Integrate private variables


class Bank_Account:
    bank_users = [{"acc_no": 1, "acc_balance": 100}, {"acc_no": 2, "acc_balance": 0}]

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                item["acc_balance"] += int(amount)
                print(
                    f'you deposited {amount} and new balane {item.get("acc_balance")}'
                )

                break
            else:
                print("Account Number Not Found")
                break

    def withdrawal(self, amount):
        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                item["acc_balance"] -= int(amount)
                print(f'you withdraw {amount} and new balane {item.get("acc_balance")}')

                break
            else:
                print("Account Number Not Found")
                break

    def account_balance(self):
        for item in self.bank_users:
            if item["acc_no"] == self.account_number:
                print(item["acc_balance"])
                break
            else:
                print("Account Number Not Found")
                break


save_money = Bank_Account(1)

# print(save_money.__balance)

save_money.account_balance()

save_money.deposit(4000)
save_money.withdrawal(40)

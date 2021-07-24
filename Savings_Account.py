class SavingsAccount:
    annual_Inter_rate = 5

    def balance(self, balance):
        self.saving_balance = balance

    def Monthly_interest(self):
        self.saving_balance += self.saving_balance *SavingsAccount.annual_Inter_rate /1200

    @staticmethod
    def modifyInterestRate(annual_Inter_rate):
        SavingsAccount.annual_Inter_rate = annual_Inter_rate
     


saver1 = SavingsAccount()
saver2 = SavingsAccount()
saver1.balance(2000)
saver2.balance(3000)

saver1.Monthly_interest()
saver2.Monthly_interest()
print(f'\nBalance of Saver1: Rs.{saver1.saving_balance}\nBalance of Saver2: Rs.{saver2.saving_balance}')
saver1.modifyInterestRate(7)
saver1.Monthly_interest()
saver2.Monthly_interest()
print(f'\nBalance of Saver1: Rs.{saver1.saving_balance}\nBalance of Saver2: Rs.{saver2.saving_balance}')
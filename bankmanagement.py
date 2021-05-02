import sys
class Customer:
    """Bank management system"""
    bankname = "Durgesh Bank"
    def __init__(self, name, balance= 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
            sys.exit()
        self.balance = self.balance - amount
        print("balance after witdrawel ", self.balance)

print("Welcome to ",Customer.bankname)
name = input("enter your name")
c = Customer(name)
while True:
    print('d- for deposit /n w - withdrawal /n e - exit')
    choice = input("enter your choice")
    if choice == 'd' or choice == 'D' :
        amount = int(input("enter the amount to deposit"))
        c.deposit(amount)

    elif choice == 'w' or choice == 'W' :
        amount = int(input("enter the amount to withdraw"))
        c.withdraw(amount)
    elif choice == 'e' or choice == 'E' :
        print("thanx for using our service")
        sys.exit()
    else :
        print("wrong choice enter again correct choice")

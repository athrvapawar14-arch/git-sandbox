""" 
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()

print(a.count)
print(b.count)
print(Counter.count)

Oh. this was a tricky one. 
but it should print 3. i think. 
first of all the count is class variable. And whenever a constructor is made. 
that is an object is initialized, the count increases. since we have 3 object, we get 3.
so all three should print 3. 

"""

class BankAccount:

    
    def __init__(self, name, balance):  # Constructor

        # Instance Variables
        self.name = name
        self.balance = balance


        # Instance Methods
    def deposit(self, amount):  
        # the method call must have an if block to check if deposited money is not negative. like at the input level itself.
        if amount <= 0: 
            print("Invalid entry. Try again!!")
        
        else:
            self.balance = self.balance + amount
            print(f"DEPOSITED {amount} TO ACCOUNT")
            print(f"Your new bank balance is : {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid entry. Try Again!!!")

        else:

            if self.balance >= amount :
                self.balance = self.balance - amount
                print(f"Withdrawn amount {amount}")
                print(f"Your new bank balance is {self.balance}")

            else:
                print("Insufficient funds")

    def show_balance(self):
        return {self.balance}


    def transfer( self, acc, amount):

        if amount <= 0:
            print("Invalid Entry. Try again!!!")


        else:

            if self.balance >= amount :
                self.balance = self.balance - amount

                acc.deposit(amount)
                print(f"Deposited amount {amount} to {acc.name}")

            else:
                print("Insufficient funds.")




a = BankAccount("Athrva", 5000)
b = BankAccount("Alex", 1000)

a.withdraw(300)
a.transfer(b, 1000)

print(a.show_balance())   # 3700
print(b.show_balance())   # 2000
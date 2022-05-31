class Account:
    def __init__(self, name, number, amount):
        self.name = name
        self.number = number
        self.amount = amount

    def accountInfo (self):
        print("Name: ", self.name)
        print("Number: ", self.number)
        print("amount: ", self.amount)
        

account = Account("Omer Demirel", "12345", "10000")       

account.accountInfo()

class BankAccount:
    def __init__(self,name,num,type,balance):
        self.name = name
        self.account_num = num
        self.account_type = type
        self.balance = balance
    def display(self):
        print(self.name)
        print(self.account_num)
        print(self.account_type)
        print(self.balance)
    def deposit(self,deposit):
        self.balance+=deposit
        print(f"Amount after deposit: ${self.balance}")
    def withdraw(self,withdraw):
        print(self.balance)
        if (withdraw > self.balance):
            print("Insufficient balance")
            self.balance -= withdraw
account = BankAccount("Afnan","5247612623","Savings",100000)
account.display()
account.deposit(500)
account.withdraw(300)
account.display()
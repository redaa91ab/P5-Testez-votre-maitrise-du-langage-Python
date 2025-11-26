class BankAccount:
    """ class that represent a Bank Account """
    def __init__(self, account_holder: str, balance: float):
        """
        Args:
           `account_holder` : le nom du titulaire du compte (string)
            `balance` : le solde du compte (float)
        """

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """ Add value amount to the balance """
        if amount > 0 : 
            self.balance += amount
            print(f"\n{amount} has been added to the balance.")
            print(f"New balance : {self.balance}")
        else : 
            print("Please enter a valid amount")

    def withdraw(self, amount):
        """
        If the amount is less than the balance :
        Remove the amount value from the balance
        """
        if amount > self.balance :
            print("\nYour balance is too low for this request.")
        else : 
            self.balance -= amount
            print(f"\nWithdraw successfully done. See you soon !")
            print(f"New balance : {self.balance}")

    def display_balance(self):
        """ Display the balance """
        print(f"\nWelcome {self.account_holder} ! ")
        print(f"\nBalance : {self.balance}")
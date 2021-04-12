def create_spend_chart(categories):
    return None


class Category:
    """This are categories included in the budget"""
    
    def __init__(self, name):
        """Initialize the name"""
        self.name = name 
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:=^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total = total + item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        """Deposit is the amount that is initially put in a place like in an account"""

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Withdraw is the amount removed from the deposited money"""

        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def check_balance(self):
        """Check Balance is the balance gotten from deposit minus withdraw"""

        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash

    def transfer(self, amount, category):
        """Transfer is the amount move from one place to another for other purpose"""

        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):

        if(self.check_balance() >= amount):
            return True
        return False


    
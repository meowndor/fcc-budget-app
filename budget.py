class Category:
    def __init__(self, label=None):
        if isinstance(label, str) != True:
            self.label = str(label)
        else:
            self.label = label

        self.ledger = []

    def total_funds(self):
        funds = 0
        for i in self.ledger:
            for key, value in i.items():
                # print(key, value)
                if key == "amount":
                    funds += value
        return funds

    def check_funds(self, amount=None):
        if amount <= self.total_funds():
            return True
        else:
            return False

    def get_balance(self):
        return self.total_funds()

    def deposit(self, amount=None, description=""):
        return self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, expense=None, description=""):
        if self.check_funds(expense) == True:
            self.ledger.append(
                {"amount": -1*expense, "description": description})
            return True
        else:
            return False

    def transfer(self, amount=None, destination=None):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {destination.label}")
            destination.deposit(amount, f"Transfer from {self.label}")
            return True
        else:
            return False

    def __str__(self):
        title = self.label.center(30, "*")+"\n"
        details = ""
        balance = 0
        for i in self.ledger:
            if i["description"] == None or i["amount"] == None:
                pass

            # TODO: fix the description slicing depends on the length of amount number
            elif len(i["description"]) > 23:
                details += i["description"][:23] + \
                    "{0:.2f}".format(i["amount"]).rjust(
                        30-len(i["description"][:23])) + "\n"
            else:
                details += i["description"] + \
                    "{0:.2f}".format(i["amount"]).rjust(
                        30-len(i["description"])) + "\n"
            balance += i["amount"]

        total = "Total: {0:.2f}".format(balance)
        # values = []
        # description = []
        # for i in self.ledger:
        #     for key, value in i.items():
        #         if key == "amount":
        #             values.append(value)
        #         elif key == "description":
        #             description.append(value)
        return title+details+total
        # def create_spend_chart(categories):

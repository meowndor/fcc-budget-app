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
        return title+details+total


def create_spend_chart(category):
    categories = [item.label for item in category]
    # total expense each category
    each_category_x = []
    category_x_total_percent = []
    for each in category:
        each_category_x.append(sum([-1*i["amount"]
                                    for i in each.ledger if i["amount"] < 0]))
    for i in range(len(each_category_x)):
        category_x_total_percent.append(
            (each_category_x[i]/sum(each_category_x))*100)

    def tick(percentage):
        o = ""
        for i in [round(rounded) for rounded in category_x_total_percent]:
            if i >= percentage:
                o += ("o".center(3))
            else:
                o += "   "
        return o
    line = []
    for percentage in range(100, -10, -10):
        line.append(str(percentage) + "|" + tick(percentage) + " " + "\n")
    print_line = ""
    for i in line:
        print_line += str(i).rjust(15)
    separator = "    " + "-"*3*len(categories) + "-"+"\n"
    padded = []
    for item in list(map(str, categories)):
        padded.append(item.ljust(
            len(max(list(map(str, categories)), key=len)), " "))

    regroup = ["".join(map(str, [item[i].center(3) for item in padded]))
               for i in range(len(max(padded, key=len)))]
    label = ""
    for i in regroup:
        if i == regroup[-1]:
            label += i.rjust(13) + " "
        else:
            label += i.rjust(13) + " " + "\n"

    title = "Percentage spent by category" + "\n"
    return title + print_line + separator + label
    # return line

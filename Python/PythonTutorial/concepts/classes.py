class factory:
    def __init__(self, name, owner, product):
        self.name = name
        self.owner = owner
        self.product = product
    def makeProfit(self):
        print("True")


cocaCola = factory("Can Factory", "John Doe", "Cans")
cocaCola.makeProfit()
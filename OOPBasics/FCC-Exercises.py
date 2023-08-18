import csv

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount

    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to receive arguments - assertions can run our own personal error messages
        assert price >= 0, f"Price {price} is not equal or greater than 0!"

        assert quantity >= 0, f"Quantity is not equal or greater than 0!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    @classmethod # aparently this turns instantiate_from_csv into a class method...
    def instantiate_from_csv(cls):# cls -> the class reference (Item) is passed as a method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})" # good practice to display exactly as we have created
# By using this best practice, we can take the terminal printed message and copy paste it elsewhere

Item.instantiate_from_csv()







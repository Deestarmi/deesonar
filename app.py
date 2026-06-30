def calculate_discount(price, discount_percent):
    final_price = price - (price * discount_percent / 100)
    return final_price

def unused_function():
    x = 10
    return x

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def total(self):
        total = 0
        for i in self.items:
            total = total + i["price"]
        return total
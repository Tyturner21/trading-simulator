import time

class Order:
    def __init__(self, bot_name, side, qty, price):
        self.bot_name = bot_name
        self.side = side.upper()  # "BUY" or "SELL"
        self.qty = qty
        self.price = price

    def __repr__(self):
        return f"{self.bot_name}: {self.side} {self.qty}@{round(self.price, 2)}"


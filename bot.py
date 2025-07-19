from order import Order
import random

class TrendBot:
    def __init__(self, name):
        self.name = name

    def decide_order(self, tick, price):
        # Wider and random offset: +3% to -3%
        direction = 1 if random.random() < 0.5 else -1
        offset = random.uniform(0.015, 0.035)
        order_price = round(price * (1 + direction * offset), 2)
        qty = random.randint(1, 3)
        side = "BUY" if direction == 1 else "SELL"
        return [Order(self.name, side, qty, order_price)]

class MarketMakerBot:
    def __init__(self, name):
        self.name = name

    def decide_order(self, tick, price):
        spread = random.uniform(2.0, 4.0)  # wider spread
        qty = random.randint(1, 3)
        buy_price = round(price - spread / 2, 2)
        sell_price = round(price + spread / 2, 2)
        return [
            Order(self.name, "BUY", qty, buy_price),
            Order(self.name, "SELL", qty, sell_price),
        ]

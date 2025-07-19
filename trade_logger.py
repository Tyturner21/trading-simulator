# trade_logger.py

class TradeLogger:
    def __init__(self):
        self.trades = []

    def log_trade(self, qty, price):
        self.trades.append((qty, price))
        print(f"TRADE: {qty} @ {price}")

    def get_trade_history(self):
        return self.trades

    def print_summary(self):
        print("\nTrade History:")
        for qty, price in self.trades:
            print(f"{qty} @ {price}")

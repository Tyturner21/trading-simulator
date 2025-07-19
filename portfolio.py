class Portfolio:
    def __init__(self):
        self.cash = {}
        self.holdings = {}
        self.pnl_history = {}

    def add_bot(self, name, initial_cash):
        self.cash[name] = initial_cash
        self.holdings[name] = 0
        self.pnl_history[name] = []

    def update_after_trade(self, bot_name, side, qty, price):
        if side.lower() == 'buy':
            self.cash[bot_name] -= qty * price
            self.holdings[bot_name] += qty
        elif side.lower() == 'sell':
            self.cash[bot_name] += qty * price
            self.holdings[bot_name] -= qty

    def record_pnl(self, current_price):
        for name in self.cash:
            value = self.cash[name] + self.holdings[name] * current_price
            self.pnl_history[name].append(value)

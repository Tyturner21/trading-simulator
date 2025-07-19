import numpy as np
import matplotlib.pyplot as plt
from order import Order
from order_book import match_orders
from portfolio import Portfolio
from bot import TrendBot, MarketMakerBot
from trade_logger import TradeLogger

# Initialize
price = 100
ticks = 10
price_history = [price]

bots = [TrendBot("TrendBot"), MarketMakerBot("MakerBot")]

portfolio = Portfolio()
portfolio.add_bot("TrendBot", 100000)
portfolio.add_bot("MakerBot", 100000)

logger = TradeLogger()

# Simulation loop
for tick in range(1, ticks + 1):
    print(f"\n=== TICK {tick} ===")
    price += np.random.normal(0, 2)
    price_history.append(price)

    all_orders = []
    for bot in bots:
        orders = bot.decide_order(tick, price)
        all_orders.extend(orders)
        for order in orders:
            print(f"{bot.name} Order: {order}")

    buy_orders = [o for o in all_orders if o.side == "BUY"]
    sell_orders = [o for o in all_orders if o.side == "SELL"]
    trades = match_orders(buy_orders, sell_orders)

    for bot_name, side, qty, trade_price in trades:
        portfolio.update_after_trade(bot_name, side, qty, trade_price)
        logger.log_trade(qty, trade_price)

    portfolio.record_pnl(price)

logger.print_summary()

# Plot
fig, ax1 = plt.subplots()

base_value = 100000
for name, pnl in portfolio.pnl_history.items():
    delta_pnl = [v - base_value for v in pnl]
    ax1.plot(delta_pnl, label=name)

ax1.set_ylabel("Portfolio ΔValue")
ax1.set_xlabel("Tick")

ax2 = ax1.twinx()
ax2.plot(price_history[1:], label="Price", linestyle="--", color="green")
ax2.set_ylabel("Price")

plt.title("Bot P&L Change and Market Price")
fig.legend(loc="upper left")
plt.grid(True)
plt.show()

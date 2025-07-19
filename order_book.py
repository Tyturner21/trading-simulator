import heapq
from order import Order

# order_book.py

def match_orders(buy_orders, sell_orders):
    buy_orders = sorted(buy_orders, key=lambda o: -o.price)
    sell_orders = sorted(sell_orders, key=lambda o: o.price)

    trades = []
    i = j = 0

    while i < len(buy_orders) and j < len(sell_orders):
        buy = buy_orders[i]
        sell = sell_orders[j]

        if buy.price >= sell.price:
            traded_qty = min(buy.qty, sell.qty)
            trade_price = round((buy.price + sell.price) / 2, 2)

            trades.append((buy.bot_name, "buy", traded_qty, trade_price))
            trades.append((sell.bot_name, "sell", traded_qty, trade_price))

            buy.qty -= traded_qty
            sell.qty -= traded_qty

            if buy.qty == 0:
                i += 1
            if sell.qty == 0:
                j += 1
        else:
            break

    return trades

import sys

def first_solution(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_profit = max(prices[j] - prices[i], max_profit)
    return max_profit


def second_solution(prices):
    # handle empty list
    if len(prices) == 0:
        return 0

    # initial buying and selling prices
    buy_stack, sell_stack = [(0, prices[0])], [(None, 0)]
    max_profit = sell_stack[-1][1] - buy_stack[-1][1]

    for idx, price in enumerate(prices):
        # find the best buying and selling prices
        if buy_stack[-1][1] > price:
            buy_stack.append((idx, price))
        if sell_stack[-1][1] < price:
            sell_stack.append((idx, price))

        # check profitability and time sequence
        if sell_stack[-1][1] - buy_stack[-1][1] > max_profit:
            sell_time = sell_stack[-1][0]
            buy_time = buy_stack[-1][0]

            if sell_time > buy_time and sell_time is not None:
                max_profit = sell_stack[-1][1] - buy_stack[-1][1]
            else:
                sell_stack.pop()
    return max_profit


def third_solution(prices):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


if __name__ == "__main__":
    input1 = [4,0,1,0,0,0,6,1,4]
    print(third_solution(input1))

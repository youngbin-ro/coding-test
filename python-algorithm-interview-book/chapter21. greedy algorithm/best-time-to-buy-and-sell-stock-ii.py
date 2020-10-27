from typing import List


def first_solution(prices: List[int]) -> int:
    profit = 0
    for idx in range(len(prices) - 1):
        profit += max(prices[idx + 1] - prices[idx], 0)
    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(first_solution(prices))

    prices = [1, 2, 3, 4, 5]
    print(first_solution(prices))

    prices = [7, 6, 4, 3, 1]
    print(first_solution(prices))

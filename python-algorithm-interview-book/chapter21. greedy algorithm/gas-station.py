from typing import List


def first_solution(gas: List[int], cost: List[int]) -> int:
    # get candidates to be start station
    candidates = [idx for idx, (g, c) in enumerate(zip(gas, cost)) if g >= c]

    # iterate over candidates
    for start in candidates:
        flag = True
        tank = 0

        # travel clockwise
        for station in range(start, len(gas) + start):

            # adjust index
            if station >= len(gas):
                station -= len(gas)

            # check possibility
            tank += gas[station] - cost[station]
            if tank < 0:
                flag = False
                break

        # return if satisfied
        if flag:
            return start

    return -1


def second_solution(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for station in range(len(gas)):
        if gas[station] + fuel < cost[station]:
            start = station + 1
            fuel = 0
        else:
            fuel += gas[station] - cost[station]
    return start


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(second_solution(gas, cost))
    print()

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(second_solution(gas, cost))

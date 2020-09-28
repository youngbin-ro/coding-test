import collections


def first_solution(grid) -> int:
    if not grid:
        return 0

    height, width = len(grid), len(grid[0])
    count, searched = 0, []
    for i in range(height):
        for j in range(width):
            if [i, j] in searched:
                continue
            elif grid[i][j] == "0":
                searched.append([i, j])
                continue

            searched.append([i, j])
            deque = collections.deque()
            deque.append([i, j])
            while deque:
                node = deque.popleft()
                children = [[node[0] - 1, node[1]],
                            [node[0], node[1] + 1],
                            [node[0] + 1, node[1]],
                            [node[0], node[1] - 1]]

                for child in children:
                    if height <= child[0] or width <= child[1]\
                            or child[0] < 0 or child[1] < 0 or child in searched:
                        continue
                    searched.append(child)
                    if grid[child[0]][child[1]] == "1":
                        deque.append(child)
            count += 1
    return count


def second_solution(grid) -> int:
    if not grid:
        return 0

    height, width = len(grid), len(grid[0])
    count, searched, flag = 0, [], False
    stack, queue = [], collections.deque()
    stack.append([0, 0])

    while stack:
        node = stack.pop()
        if grid[node[0]][node[1]] == "1":
            flag = True
        searched.append(node)
        children = [
            [node[0] - 1, node[1]],
            [node[0], node[1] + 1],
            [node[0] + 1, node[1]],
            [node[0], node[1] - 1]
        ]

        for child in children:
            if height <= child[0]\
                    or width <= child[1] \
                    or child[0] < 0\
                    or child[1] < 0\
                    or child in searched:
                continue
            if grid[child[0]][child[1]] == "1" and child not in stack:
                stack.append(child)
                flag = True
            elif grid[child[0]][child[1]] == "0" and child not in queue:
                queue.append(child)

        if not stack:
            if flag:
                count += 1
                flag = False
            if not queue:
                break
            stack.append(queue.popleft())
    return count


def third_solution(grid) -> int:
    def dfs(i, j):
        if i < 0 or len(grid) <= i or \
                j < 0 or len(grid[0]) <= j or \
                grid[i][j] == "0":
            return
        grid[i][j] = "0"
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j + 1)

    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1
    return count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(third_solution(grid1))

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(third_solution(grid2))

    grid3 = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    print(third_solution(grid3))

    grid4 = [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"]
    ]
    print(third_solution(grid4))

    grid5 = [["1"]]
    print(third_solution(grid5))

    grid6 = [
        ["0", "1", "0"],
        ["1", "0", "1"],
        ["0", "1", "0"]
    ]
    print(third_solution(grid6))

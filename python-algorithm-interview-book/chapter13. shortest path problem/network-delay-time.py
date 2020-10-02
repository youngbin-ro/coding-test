import collections, heapq


# incorrect
def first_solution(times: list, N: int, K: int) -> int:
    delays = [[0] * (N + 1) for _ in range(N + 1)]
    graph = collections.defaultdict(list)
    for time in times:
        delays[time[0]][time[1]] = time[2]
        graph[time[0]].append(time[1])
    time = [0] * (N + 1)
    searched = set()

    def bfs(start):
        searched.add(start)
        for node in graph[start]:
            if node in searched and time[start] >= time[node]:
                continue
            updated = time[start] + delays[start][node]
            time[node] = updated if time[node] == 0 else min(time[node], updated)
            bfs(node)

    bfs(K)
    return -1 if len(searched) != N else max(time)


def second_solution(times: list, N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    Q = [(0, K)]
    dist = collections.defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    if len(dist) == N:
        return max(dist.values())
    return -1


if __name__ == "__main__":
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N1, K1 = 4, 2
    print(second_solution(times1, N1, K1))

    times2 = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    N2, K2 = 3, 1
    print(second_solution(times2, N2, K2))

    times3 = [[1, 2, 1], [2, 1, 3]]
    N3, K3 = 2, 2
    print(second_solution(times3, N3, K3))

    times4 = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
    N4, K4 = 3, 2
    print(second_solution(times4, N4, K4))

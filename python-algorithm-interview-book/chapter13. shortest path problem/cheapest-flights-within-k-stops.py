import collections, heapq


# incorrect
def first_solution(n: int, flights: list, src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, -1)]
    dist = collections.defaultdict(int)
    prev = collections.defaultdict(int)

    def n_stops(node):
        count = -1
        while node != -1:
            node = prev[node]
            count += 1
        return count

    while Q:
        time, node, prev_node = heapq.heappop(Q)
        if node not in dist:
            if n_stops(prev_node) >= K and node != dst:
                continue
            dist[node] = time
            prev[node] = prev_node

            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v, node))

    if dst in dist:
        return dist[dst]
    return -1


def second_solution(n: int, flights: list, src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, K)]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


if __name__ == "__main__":
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    n, src, dst, k = 3, 0, 2, 1
    print(second_solution(n, edges, src, dst, k))    # answer: 200

    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    n, src, dst, k = 3, 0, 2, 0
    print(second_solution(n, edges, src, dst, k))    # answer: 500

    edges = [[1, 2, 10], [2, 0, 7], [1, 3, 8],
             [4, 0, 10], [3, 4, 2], [4, 2, 10],
             [0, 3, 3], [3, 1, 6], [2, 4, 5]]
    n, src, dst, k = 5, 0, 4, 1
    print(second_solution(n, edges, src, dst, k))

    edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],
             [1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],
             [8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    n, src, dst, k = 10, 6, 0, 7
    print(second_solution(n, edges, src, dst, k))

    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    n, src, dst, k = 4, 0, 3, 1
    print(second_solution(n, edges, src, dst, k))

    edges = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    n, src, dst, k = 5, 0, 2, 2
    print(second_solution(n, edges, src, dst, k))

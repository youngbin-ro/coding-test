import collections, itertools


def first_solution(tickets: list) -> list:
    graph = collections.defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    paths = []

    def dfs(start, path, edges):
        if not edges:
            paths.append(path[:])
            return

        for node in sorted(graph[start]):
            if [start, node] not in edges:
                continue
            path.append(node)
            edges.remove([start, node])
            dfs(node, path, edges)
            if paths:
                break
            edges.append([start, node])
            path.pop()

    dfs('JFK', ['JFK'], tickets)
    return paths[0]


def second_solution(tickets: list) -> list:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]


if __name__ == "__main__":
    input1 = [["MUC", "LHR"],
              ["JFK", "MUC"],
              ["SFO", "SJC"],
              ["LHR", "SFO"]]
    print(second_solution(input1))
    print()

    input2 = [["JFK", "SFO"],
              ["JFK", "ATL"],
              ["SFO", "ATL"],
              ["ATL", "JFK"],
              ["ATL", "SFO"]]
    print(second_solution(input2))
    print()

    input3 = [["JFK", "KUL"],
              ["JFK", "NRT"],
              ["NRT", "JFK"]]
    print(second_solution(input3))
    print()

    input4 = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
    print(second_solution(input4))

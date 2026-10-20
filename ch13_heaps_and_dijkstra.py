import heapq

def k_smallest(items: list[int], k: int) -> list[int]:
    copy = items.copy()
    heapq.heapify(copy)
    result: list[int] = []
    while copy and len(result) < k:
        result.append(heapq.heappop(copy))
    return result

def dijkstra_shortest_path(graph: dict[str, list[tuple[str, int]]], start: str, goal: str) -> tuple[int, list[str]] | None:
    dist = {start: 0}
    parent = {start: None}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        for neighbour, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbour, float("inf")):
                dist[neighbour] = new_dist
                parent[neighbour] = node
                heapq.heappush(heap, (new_dist, neighbour))

    if goal not in parent:
        return None

    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]

    path.reverse()
    return dist[goal], path

## Tests for k_smallest

numbers = [5, 1, 8, 3, 9, 2]
print(k_smallest(numbers, 3))  # [1, 2, 3]
print(k_smallest(numbers, 1))  # [1]
print(k_smallest(numbers, 0))  # []
print(k_smallest(numbers, 10))  # [1, 2, 3, 5, 8, 9]
print(numbers)  # [5, 1, 8, 3, 9, 2]
print(k_smallest([5, 1, 1, 3], 2))  # [1, 1]
print(k_smallest([], 3))  # []

## Tests for dijkstra_shortest_path
roads = {
    "A": [("B", 1), ("E", 10)],
    "B": [("A", 1), ("C", 1)],
    "C": [("B", 1), ("D", 1)],
    "D": [("C", 1), ("F", 1)],
    "E": [("A", 10), ("F", 1)],
    "F": [("D", 1), ("E", 1)],
    "G": [],
}

print(dijkstra_shortest_path(roads, "A", "F"))  # (4, ['A', 'B', 'C', 'D', 'F'])
print(dijkstra_shortest_path(roads, "A", "E"))  # (5, ['A', 'B', 'C', 'D', 'F', 'E'])
print(dijkstra_shortest_path(roads, "F", "A"))  # (4, ['F', 'D', 'C', 'B', 'A'])
print(dijkstra_shortest_path(roads, "A", "A"))  # (0, ['A'])
print(dijkstra_shortest_path(roads, "A", "G"))  # None
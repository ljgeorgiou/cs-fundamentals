from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph: dict[str, list[str]] = {}

    def add_node(self, a: str) -> None:
        if a not in self.graph:
            self.graph[a] = []

    def add_edge(self, a: str, b: str) -> None:
        self.add_node(a)
        self.add_node(b)
        self.graph[a].append(b)
        self.graph[b].append(a)

    def add_directed_edge(self, a: str, b: str) -> None:
        self.add_node(a)
        self.add_node(b)
        self.graph[a].append(b)

    def neighbours(self, a: str) -> list[str]:
        return self.graph[a]

    def bfs(self, start: str) -> list[str]:
        result: list[str] = []
        worklist: deque[str] = deque([start])
        already_seen: set[str] = {start}
        while worklist:
            node = worklist.popleft()
            result.append(node)
            for neighbour in self.neighbours(node):
                if neighbour not in already_seen:
                    worklist.append(neighbour)
                    already_seen.add(neighbour)
        return result

    def dfs(self, node: str, already_seen: set[str] | None = None, order: list[str] | None = None) -> list[str]:
        if already_seen is None:
            already_seen = set()
        if order is None:
            order = []
        already_seen.add(node)
        order.append(node)
        for neighbour in self.neighbours(node):
            if neighbour not in already_seen:
                self.dfs(neighbour, already_seen, order)
        return order

    def shortest_path(self, start: str, goal: str) -> list[str] | None:
        parent: dict[str, str | None] = {start: None}
        queue: deque[str] = deque([start])
        while queue:
            node = queue.popleft()
            if node == goal:
                break
            for neighbour in self.neighbours(node):
                if neighbour not in parent:
                    parent[neighbour] = node
                    queue.append(neighbour)

        if goal not in parent:
            return None

        path: list[str] = []
        current_node = goal
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]

        path.reverse()
        return path

    def is_connected(self, a: str, b: str) -> bool:
        path = self.shortest_path(a, b)
        return path is not None

    def has_cycle(self, node: str, already_seen: set[str] | None = None, parent: str | None = None) -> bool:
        # Only works on undirected graphs (built with add_edge).
        if already_seen is None:
            already_seen = set()
        already_seen.add(node)
        for neighbour in self.neighbours(node):
            if neighbour not in already_seen:
                if self.has_cycle(neighbour, already_seen, node):
                    return True
            elif neighbour != parent:
                return True
        return False

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")
g.add_edge("F", "G")
g.add_edge("G", "E")
g.add_node("H")

print(g.bfs("A"))  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(g.bfs("H"))  # ['H']
print(g.dfs("A"))  # ['A', 'B', 'D', 'C', 'E', 'F', 'G']
print(g.dfs("G"))  # ['G', 'F', 'E', 'D', 'B', 'A', 'C']
print(g.shortest_path("A", "G"))  # ['A', 'B', 'D', 'E', 'G']
print(g.shortest_path("A", "A"))  # ['A']
print(g.shortest_path("A", "H"))  # None
print(g.is_connected("A", "G"))  # True
print(g.is_connected("A", "H"))  # False
print(g.has_cycle("A"))  # True
print(g.has_cycle("H"))  # False

d = Graph()
d.add_directed_edge("A", "B")
d.add_directed_edge("B", "C")
d.add_directed_edge("C", "D")

print(d.bfs("A"))  # ['A', 'B', 'C', 'D']
print(d.bfs("C"))  # ['C', 'D']
print(d.dfs("D"))  # ['D']
print(d.shortest_path("A", "D"))  # ['A', 'B', 'C', 'D']
print(d.shortest_path("D", "A"))  # None

t = Graph()
t.add_edge("A", "B")
t.add_edge("A", "C")
t.add_edge("B", "D")
t.add_edge("B", "E")

print(t.has_cycle("A"))  # False
print(t.has_cycle("D"))  # False
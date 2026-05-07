from collections import deque
import heapq


class SearchAlgorithms:

    def __init__(self, environment):
        self.env = environment
        self.grid = environment.grid
        self.size = environment.size

    def is_valid(self, x, y):

        if 0 <= x < self.size and 0 <= y < self.size:
            return self.grid[x, y] != self.env.BLOCKED

        return False

    def get_neighbors(self, node):

        x, y = node
        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        res = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                res.append((nx, ny))

        return res

    def heuristic(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def risk(self, node):
        return 5 if node in self.env.hazards else 0

    def bfs(self, start, goal):

        q = deque([(start, [start])])
        visited = set()
        expanded = 0

        while q:

            node, path = q.popleft()

            if node in visited:
                continue

            visited.add(node)
            expanded += 1

            if node == goal:
                return {
                    "path": path,
                    "cost": len(path),
                    "risk": sum(self.risk(p) for p in path),
                    "nodes_expanded": expanded
                }

            for n in self.get_neighbors(node):
                q.append((n, path + [n]))

        return None

    def a_star(self, start, goal):

        pq = [(0, start, [start], 0)]
        visited = set()
        expanded = 0

        while pq:

            f, node, path, g = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            expanded += 1

            if node == goal:
                return {
                    "path": path,
                    "cost": g,
                    "risk": sum(self.risk(p) for p in path),
                    "nodes_expanded": expanded
                }

            for n in self.get_neighbors(node):

                ng = g + 1 + self.risk(n)
                h = self.heuristic(n, goal)
                heapq.heappush(pq, (ng + h, n, path + [n], ng))

        return None
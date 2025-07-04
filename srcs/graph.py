import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, w):
        self.edges.setdefault(u, []).append((v, w))

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.edges}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            for v, w in self.edges.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return dist

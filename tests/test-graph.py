from src.graph import Graph

def test_dijkstra():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('A', 'C', 4)

    dist = g.dijkstra('A')
    assert dist['C'] == 3

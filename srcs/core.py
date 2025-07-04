import sys
import os
sys.path.append(os.path.dirname(__file__))

import argparse
from graph import Graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str, default='dijkstra')
    parser.add_argument('--source', type=str)
    parser.add_argument('--target', type=str)
    args = parser.parse_args()

    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('C', 'D', 1)

    if args.algo == 'dijkstra':
        dist = g.dijkstra(args.source)
        print(f"从 {args.source} 到 {args.target} 的最短路径长度为：{dist[args.target]}")
    else:
        print("暂不支持该算法")

if __name__ == '__main__':
    main()

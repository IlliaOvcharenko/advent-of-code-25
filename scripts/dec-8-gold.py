import sys
sys.setrecursionlimit(1500)

import random
import math
import operator

from collections import Counter
from functools import reduce
from itertools import combinations

from tqdm.cli import tqdm


def main():
    # fn = "inputs/aoc-25-dec-8-test.txt"
    fn = "inputs/aoc-25-dec-8.txt"


    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]


    points = []
    for l in lines:
        points.append(tuple(map(int, l.split(","))))

    num_points = len(points)

    dist_done = [[False] * num_points for _ in range(num_points)]

    calc_dist = lambda p1, p2: \
        math.sqrt(sum([ (f-s) ** 2 for f, s in zip(p1, p2)]))



    dist_list = []
    for i in range(num_points):
        for j in range(num_points):
            if (i != j) and not dist_done[i][j]:
                dist = calc_dist(points[i], points[j])
                dist_done[i][j] = True
                dist_done[j][i] = True

                dist_list.append((dist, i, j))

    dist_list = list(sorted(dist_list, key=lambda x: x[0]))


    graph_matrix = [[False] * num_points for _ in range(num_points)]

    for _, p1, p2 in tqdm(dist_list):
        graph_matrix[p1][p2] = True
        graph_matrix[p2][p1] = True


        visited = [False] * num_points
        def dfs(n_from):

            if visited[n_from]:
                return False
            visited[n_from] = True


            node_edges = [
                e for e, s in enumerate(graph_matrix[n_from])
                if s
            ]

            for e in node_edges:
                dfs(e)

        dfs(random.choice(range(num_points)))

        if all(visited):
            print(f"point 1 {p1} {points[p1]}")
            print(f"point 2 {p2} {points[p2]}")
            print(points[p1][0] * points[p2][0])
            break


    # Backward Edition, too slow, there are much more edges to remove.
    # graph_matrix = [[True] * num_points for _ in range(num_points)]
    # while True:
    #     # edge to remove
    #     _, p1, p2 = dist_list.pop(-1)
    #     print(f"remove edge {p1} - {p2}")

    #     graph_matrix[p1][p2] = False
    #     graph_matrix[p2][p1] = False

    #     visited = [False] * num_points

    #     def is_connected(n_from, n_to):
    #         if visited[n_from]:
    #             return False
    #         visited[n_from] = True

    #         if n_from == n_to:
    #             return True

    #         node_edges = [
    #             e for e, s in enumerate(graph_matrix[n_from])
    #             if s
    #         ]

    #         return any([is_connected(e, n_to) for e in node_edges])

    #     if not is_connected(p1, p2):
    #         print(f"point 1 {p1} {points[p1]}")
    #         print(f"point 2 {p2} {points[p2]}")
    #         print(points[p1][0] * points[p2][0])
    #         break


if __name__ == "__main__":
    main()

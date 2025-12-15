import math
import operator

from collections import Counter
from functools import reduce


def main():
    fn = "inputs/aoc-25-dec-8-test.txt"
    string_count = 10

    # fn = "inputs/aoc-25-dec-8.txt"
    # string_count = 1000


    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]


    points = []
    for l in lines:
        points.append(tuple(map(int, l.split(","))))

    num_points = len(points)

    dist_matrix = [[math.inf] * num_points for _ in range(num_points)]

    calc_dist = lambda p1, p2: \
        math.sqrt(sum([ (f-s) ** 2 for f, s in zip(p1, p2)]))



    dist_list = []
    for i in range(num_points):
        for j in range(num_points):
            if (i != j) and math.isinf(dist_matrix[i][j]):
                dist = calc_dist(points[i], points[j])
                # print(dist)
                dist_matrix[i][j] = dist
                dist_matrix[j][i] = dist

                dist_list.append((dist, i, j))

    dist_list = list(sorted(dist_list, key=lambda x: x[0]))

    # print(points)
    # print()
    # print(dist_matrix)
    # print()
    # print(dist_list)

    # circuits = list(range(num_points))
    # while string_count > 0:
    #     d, i, j = dist_list.pop(0)

    graph_edges = []
    graph_edges += [(i, j) for _, i, j in dist_list[:string_count]]
    graph_edges += [(j, i) for _, i, j in dist_list[:string_count]]
    visited = [-1] * num_points

    def dfs(n, visited_from):
        if visited[n] != -1:
            return

        visited[n] = visited_from

        node_edges = [e for e in graph_edges if e[0] == n]

        for e in node_edges:
            dfs(e[1], visited_from)

    for n in range(num_points):
        dfs(n, n)

    three_largest = Counter(visited).most_common(3)
    print(reduce(operator.mul, [i[1] for i in three_largest], 1))



if __name__ == "__main__":
    main()

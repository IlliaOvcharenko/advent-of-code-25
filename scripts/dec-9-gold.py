# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

from itertools import combinations

import numpy as np

def main():
    # fn = "inputs/aoc-25-dec-9-test.txt"
    fn = "inputs/aoc-25-dec-9.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]


    points = [tuple(map(int, l.split(","))) for l in lines]

    # print(points)



    # Remap points (coordinate compression, notices it on a reddit post)
    x_remap = list(sorted([p[0] for p in points]))
    y_remap = list(sorted([p[1] for p in points]))

    points_remap = [
        (x_remap.index(p[0]), y_remap.index(p[1]))
        for p in points
    ]


    # Substract min
    min_x = min([p[0] for p in points_remap])
    min_y = min([p[1] for p in points_remap])
    # print(min_x, min_y)

    points_remap = [(p[0] - min_x + 1, p[1] - min_y + 1) 
                    for p in points_remap]

    max_x = max([p[0] for p in points_remap]) + 1
    max_y = max([p[1] for p in points_remap]) + 1
    print(max_x, max_y)
    # exit(0)


    # mapping = [[False] * (max_x+1) for _ in range(max_y+1)]
    mapping = np.full((max_y+1, max_x+1), False)
    # Define borders
    for p1, p2 in zip(points_remap, (points_remap[1:] + [points_remap[0]])):
        # print(p1)
        # print(p2)
        mapping[p1[1], p1[0]] = True
        mapping[p2[1], p2[0]] = True

        if p1[1] == p2[1]:
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
                mapping[p1[1], i] = True
        elif p1[0] == p2[0]:
            for i in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
                mapping[i, p1[0]] = True

    blank_mapping = np.full_like(mapping, False)

    # queue = [(points_remap[0][1]+1, points_remap[0][0]+1), ]

    queue = [(0, 0), ]
    # print(queue)

    while queue:
        # print(len(queue))
        i, j  = queue.pop(0)

        if not (0 <= i <= max_y):
            continue
        if not (0 <= j <= max_x):
            continue

        if blank_mapping[i, j]:
            continue

        if mapping[i, j]:
            continue

        blank_mapping[i, j] = True

        # for ii in range(i-1, i+2):
        #     for jj in range(j-1, j+2):
        #         queue.append((ii, jj))
        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                # print(ii, jj)
                # if not (ii == jj):
                queue.append((ii, jj))
        # exit(0)

    # for i in range(max_y):
    #     for j in range(max_j):


    # def walk_around(i, j):
    #     if not (0 <= i <= max_y):
    #         return
    #     if not (0 <= j <= max_x):
    #         return

    #     if blank_mapping[i, j]:
    #         return

    #     if mapping[i, j]:
    #         return

    #     blank_mapping[i, j] = True

    #     for ii in range(i-1, i+2):
    #         for jj in range(j-1, j+2):
    #             walk_around(ii, jj)

    # walk_around(0, 0)


    # # Print mapping
    # for row in mapping:
    #     print("".join(map(lambda x: "x" if x else ".", row.tolist())))
    #     # exit(0)
    # print()

    # # Print mapping
    # for row in blank_mapping:
    #     print("".join(map(lambda x: "x" if x else ".", row.tolist())))
    #     # exit(0)
    # print()

    mapping = mapping | ~blank_mapping
    # # mapping = mapping | blank_mapping

    # for row in mapping:
    #     print("".join(map(lambda x: "x" if x else ".", row.tolist())))
    #     # exit(0)
    # print()
    # exit(0)

    area_list = []
    for i, j in combinations(range(len(points)), 2):
        area = (abs(points[i][0] - points[j][0]) + 1) \
             * (abs(points[i][1] - points[j][1]) + 1)
        area_list.append((area, i, j))

    area_list = list(sorted(area_list, key=lambda x: x[0], reverse=True))

    for a, i, j in area_list:
        min_x = min(points_remap[i][0], points_remap[j][0])
        max_x = max(points_remap[i][0], points_remap[j][0])
        min_y = min(points_remap[i][1], points_remap[j][1])
        max_y = max(points_remap[i][1], points_remap[j][1])

        # print(a)
        if mapping[min_y: max_y+1, min_x: max_x+1].all():
            print(a, points[i], points[j])
            break
        # exit(0)


    # max_area = 0
    # for i, j in combinations(range(len(points)), 2):
    #     def check_if_rect_is_valid(i, j):
    #         min_x = min(points[i][0], points[j][0])
    #         max_x = max(points[i][0], points[j][0])
    #         min_y = min(points[i][1], points[j][1])
    #         max_y = max(points[i][1], points[j][1])
    #         border_points = []

    #         for p in range(len(points)):
    #             if (p == i) or (p == j):
    #                 continue

    #             if (
    #                 (min_x == points[p][0]) or \
    #                 (points[p][0] == max_x)
    #             ) and (
    #                 min_y <= points[p][1] <= max_y
    #             ):
    #                 border_points.append(p)

    #             if (
    #                 (min_y == points[p][1]) or \
    #                 (points[p][1] == max_y)
    #             ) and (
    #                 min_x+1 <= points[p][0] <= max_x
    #             ):
    #                 border_points.append(p)

    #             if (min_x+1 <= points[p][0] <= max_x-1) and \
    #                (min_y+1 <= points[p][1] <= max_y-1):
    #                 return False

    #         print(points[i])
    #         print(points[j])
    #         print(f"border points: {[points[p] for p in border_points]}")

    #         # for bp1 in border_points:
    #         #     for bp2 in border_points:
    #         border_points.append(i)
    #         border_points.append(j)
    #         border_points = list(sorted(border_points))
    #         print(f"border points: {[points[p] for p in border_points]}")
    #         for bp1, bp2 in zip(
    #             border_points, (border_points[1:] + [border_points[0]])
    #         ):
    #             # if bp1 == bp2:
    #             #     continue

    #             if (points[bp1][0] == points[bp2][0]) and \
    #                (points[bp1][0] != min_x and points[bp1][0] != max_x):
    #                 print(f"reject because cross x")
    #                 return False

    #             if (points[bp1][1] == points[bp2][1]) and \
    #                (points[bp1][1] != min_y and points[bp1][1] != max_y):
    #                 print(points[bp1])
    #                 print(points[bp2])
    #                 print(min_y, max_y)
    #                 print(f"reject because cross y")
    #                 return False

    #         # print()
    #         return True

    #     if check_if_rect_is_valid(i, j):
    #         area = (abs(points[i][0] - points[j][0]) + 1) \
    #              * (abs(points[i][1] - points[j][1]) + 1)

    #         print("area valid")
    #         # print(points[i])
    #         # print(points[j])
    #         print(area)
    #         print()

    #         if area > max_area:
    #             max_area = area
    #     else:
    #         area = (abs(points[i][0] - points[j][0]) + 1) \
    #              * (abs(points[i][1] - points[j][1]) + 1)

    #         print("area not valid")
    #     #     print(points[i])
    #     #     print(points[j])
    #         print(area)
    #         print()


    # print(max_area)



if __name__ == "__main__":
    main()

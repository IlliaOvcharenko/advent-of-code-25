from itertools import combinations
def main():
    fn = "inputs/aoc-25-dec-9.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]


    points = [tuple(map(int, l.split(","))) for l in lines]
    print(points)

    max_area = 0
    for i, j in combinations(range(len(points)), 2):
        area = (abs(points[i][0] - points[j][0]) + 1) \
             * (abs(points[i][1] - points[j][1]) + 1)
        # print(points[i])
        # print(points[j])
        # print(area)
        # print()

        if area > max_area:
            max_area = area
    print(max_area)



if __name__ == "__main__":
    main()

def main():
    fn = "inputs/aoc-25-dec-5.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    ranges = []
    requests = []

    blank_line_idx = lines.index("")

    for i in range(blank_line_idx):
        ranges.append(list(map(int, lines[i].split("-"))))


    to_use = [True] * len(ranges)
    ranges = list(sorted(ranges, key=lambda x: x[0]))
    # print(ranges)

    for idx1, idx2 in zip(range(0, len(ranges)-1), range(1, len(ranges))):
        # print(idx1, idx2)

        f1, t1 = ranges[idx1]
        f2, t2 = ranges[idx2]

        if t1 >= f2:
            new_f = min(f1, f2)
            new_t = max(t1, t2)

            ranges[idx2] = [new_f, new_t]
            to_use[idx1] = False


    # print(ranges)
    # print(to_use)

    ranges = [r for r_idx, r in enumerate(ranges) if to_use[r_idx]]

    # print(ranges)

    all_fresh = sum([t-f+1 for f, t in ranges])
    print(all_fresh)


if __name__ == "__main__":
    main()

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

    for i in range(blank_line_idx+1, len(lines)):
        requests.append(int(lines[i]))

    fresh_count = 0
    for req in requests:
        for f, t in ranges:
            if f <= req <= t:
                fresh_count += 1
                break


    # print(ranges)
    # print()
    # print(requests)
    # print()
    print(fresh_count)


if __name__ == "__main__":
    main()

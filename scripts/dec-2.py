def main():
    fn = "inputs/aoc-25-dec-2.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    ranges = lines[0].split(",")

    num_sum = 0
    for r in ranges:
        r_from, r_to = list(map(int, r.split("-")))
        # print(r_from)
        # print(r_to)
        # print()

        for num in range(r_from, r_to+1):
            num_str = str(num)
            num_len = len(num_str)

            if num_len % 2 == 0:
                if num_str[:num_len//2] == num_str[num_len//2:]:
                    # print(f"found: {num}")
                    num_sum += num
    print(num_sum)


if __name__ == "__main__":
    main()

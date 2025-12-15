def main():
    fn = "inputs/aoc-25-dec-2.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    ranges = lines[0].split(",")

    num_sum = 0
    used_nums = set()
    for r in ranges:
        r_from, r_to = list(map(int, r.split("-")))

        # print(r_from)
        # print(r_to)
        # print()

        for num in range(r_from, r_to+1):
            num_str = str(num)
            num_len = len(num_str)

            for patter_len in range(1, num_len // 2 + 1):
                suggested_num_str = num_str[:patter_len] \
                                  * (num_len // patter_len)
                if num_str == suggested_num_str:
                    # print(f"found: {num}")
                    if num not in used_nums:
                        used_nums.add(num)
                        num_sum += num

    print(num_sum)


if __name__ == "__main__":
    main()

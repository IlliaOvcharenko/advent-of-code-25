def main():
    fn = "inputs/aoc-25-dec-3.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    total_joltage = 0
    for bat_bank in lines:
        digits = [int(ch) for ch in bat_bank]
        first = max(digits[:-1])
        first_index = digits.index(first)

        second = max(digits[first_index+1:])
        joltage = first * 10 + second
        total_joltage += joltage
        # print(joltage)

    # print()
    print(total_joltage)


if __name__ == "__main__":
    main()

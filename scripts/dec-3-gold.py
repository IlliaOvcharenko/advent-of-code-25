def main():
    fn = "inputs/aoc-25-dec-3.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    total_joltage = 0
    for bat_bank in lines:
        digits = [int(ch) for ch in bat_bank]


        selected = [0, ]
        for i in range(12-1, 0-1, -1):
            if i != 0:
                digit = max(digits[selected[-1]:-i])
            else:
                digit = max(digits[selected[-1]:])

            digit_index = digits[selected[-1]:].index(digit) + selected[-1]
            selected.append(digit_index + 1)

        selected = selected[1:]
        selected_digit = [digits[idx - 1] for idx in selected]
        joltage = int("".join(map(str, selected_digit)))


        total_joltage += joltage
        # print(joltage)

    # print()
    print(total_joltage)


if __name__ == "__main__":
    main()

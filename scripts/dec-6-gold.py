import operator

from functools import reduce
def main():
    fn = "inputs/aoc-25-dec-6.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    # Parse operators and spaces
    problems = []
    for ch_idx, ch in enumerate(lines[-1]):
        if ch in ["+", "*"]:
            if problems:
                problems[-1]["digit_len"] -= 1
                problems[-1]["digit_start_idx"] -= 1

            problems.append({
                "op": ch,
                "digit_len": 1,
                "digit_start_idx": ch_idx,
                "numbers": []
            })
        else:
            problems[-1]["digit_len"] += 1
            problems[-1]["digit_start_idx"] = ch_idx

    # import json
    # print(json.dumps(problems, indent=2))

    # Parse numbers
    for p_idx in range(len(problems)):
        p = problems[p_idx]
        for digit_idx in range(
            p["digit_start_idx"],
            p["digit_start_idx"] - p["digit_len"],
            -1
        ):
            digits = [l[digit_idx] for l in lines[:-1] if l[digit_idx] != " "]
            num = int("".join(digits))
            p["numbers"].append(num)

    # import json
    # print(json.dumps(problems, indent=2))

    grand_total = 0
    for p in problems:
        if p["op"] == "*":
            grand_total += reduce(operator.mul, p["numbers"], 1)
        if p["op"] == "+":
            grand_total += reduce(operator.add, p["numbers"], 0)
    print(grand_total)



if __name__ == "__main__":
    main()

import operator

from functools import reduce
def main():
    fn = "inputs/aoc-25-dec-6.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    operators = [op for op in lines[-1].split(" ") if op != ""]
    num_of_problems = len(operators)
    num_per_problem = len(lines) - 1

    numbers = [[] for _ in range(num_of_problems)]
    for l in lines[:-1]:

        for n_idx, n in enumerate([int(i) for i in l.split(" ") if i != ""]):
            numbers[n_idx].append(n)


    # print(numbers)
    # print(operators)

    grand_total = 0
    for nums, op in zip(numbers, operators):
        if op == "*":
            grand_total += reduce(operator.mul, nums, 1)
        if op == "+":
            grand_total += reduce(operator.add, nums, 0)
    print(grand_total)



if __name__ == "__main__":
    main()

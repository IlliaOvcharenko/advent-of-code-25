from itertools import combinations

def main():
    fn = "inputs/aoc-25-dec-10.txt"
    fn = "inputs/aoc-25-dec-10-test.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    sum_of_presses = 0

    for machine in lines:
        blocks = machine.split(" ")
        _ = blocks.pop(0)
        state = blocks.pop(-1)
        state = state.replace("{", "").replace("}", "")
        state = [int(ch) for ch in state.split(",")]

        btns = [b.replace("(", "").replace(")", "")  for b in blocks]
        btns = [list(map(int, b.split(",")))  for b in btns]
        # print(state)
        # print(btns)


        seq_len = 0
        is_found = False

        while True:
            seq_len += 1

            for selected_btns in combinations(range(len(btns)), seq_len):
                # print(items)
                state_to_check = [0, ] * len(state)
                for btn in [btns[b] for b in selected_btns]:
                    for item in btn:
                        state_to_check[item] += 1
                if state_to_check == state:
                    print([btns[b] for b in selected_btns])
                    is_found = True
                    sum_of_presses += seq_len

                if is_found:
                    break

            if is_found:
                break

    print(sum_of_presses)


if __name__ == "__main__":
    main()

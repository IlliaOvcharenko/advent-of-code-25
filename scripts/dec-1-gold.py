def main():
    fn = "inputs/aoc-25-dec-1.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    zero_counter = 0
    prev_state = -1
    cur_state = 50
    for l in lines:
        d = l[0]
        rot = int(l[1:])

        zero_counter = zero_counter + (rot // 100)
        rot %= 100

        if d == "L":
            rot = 100 - rot
        elif d == "R":
            pass

        prev_state = cur_state

        cur_state += rot

        if d == "L":
            zero_counter += 1 - (cur_state // 100)
        elif d == "R":
            zero_counter += (cur_state // 100)

        cur_state %= 100


        if d == "L" and prev_state == 0:
            zero_counter -= 1
        if d == "L" and cur_state == 0:
            zero_counter += 1

        # print(f"line: {l}, state: {cur_state}, zeros: {zero_counter}")
    print(zero_counter)



if __name__ == "__main__":
    main()

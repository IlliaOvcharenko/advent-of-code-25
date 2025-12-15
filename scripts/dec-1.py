
def main():
    fn = "inputs/aoc-25-dec-1.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    zero_counter = 0
    cur_state = 50
    for l in lines:
        d = l[0]
        rot = int(l[1:])

        rot %= 100

        if d == "L":
            rot = 100 - rot

        cur_state += rot
        cur_state %= 100
        if cur_state == 0:
            zero_counter += 1
    print(zero_counter)



if __name__ == "__main__":
    main()

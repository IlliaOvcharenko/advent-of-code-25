def check_paper_roll(i, j, adj):
    neighbour_count = 0
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if ii == i and jj == j:
                continue
            if ii < 0 or jj < 0:
                continue
            if ii >= len(adj) or jj >= len(adj[i]):
                continue

            if adj[ii][jj] == "@":
                neighbour_count += 1
    return neighbour_count < 4


def main():
    fn = "inputs/aoc-25-dec-4.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    adj = []
    for line in lines:
        row = list(line)
        adj.append(row)

    accessed_paper_roll_count = 0
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j] == "@":
                accessed_paper_roll_count += check_paper_roll(i, j, adj)

    print(accessed_paper_roll_count)

if __name__ == "__main__":
    main()

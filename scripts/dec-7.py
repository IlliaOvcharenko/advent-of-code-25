def main():
    fn = "inputs/aoc-25-dec-7.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    tachyon_manifold = [list(l) for l in lines]
    tachyon_manifold_shape = (
        len(tachyon_manifold),
        len(tachyon_manifold[0]),
    )
    visited = [[False] * len(l) for l in lines]
    init = (0, tachyon_manifold[0].index("S"))
    queue = [init, ]

    num_of_splits = 0

    # Bfs?
    while queue:
        i, j = queue.pop(0)
        # print(i, j)

        if not (0 <= i < tachyon_manifold_shape[0]):
            continue
        if not (0 <= j < tachyon_manifold_shape[1]):
            continue

        if visited[i][j]:
            continue
        else:
            visited[i][j] = True

        if tachyon_manifold[i][j] in [".", "S"]:
            queue.append((i+1, j))
        elif tachyon_manifold[i][j] == "^":
            queue.append((i, j-1))
            queue.append((i, j+1))
            num_of_splits += 1 

    print(num_of_splits)


if __name__ == "__main__":
    main()

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

    timeline_count = [[0, ] * len(l) for l in lines]
    timeline_count[init[0]][init[1]] = 1

    def is_move_possible(i, j):
        return (0 <= i < tachyon_manifold_shape[0]) and \
               (0 <= j < tachyon_manifold_shape[1])

    # Bfs?
    while queue:
        i, j = queue.pop(0)

        if visited[i][j]:
            continue
        else:
            visited[i][j] = True

        if tachyon_manifold[i][j] in [".", "S"]:
            if is_move_possible(i+1, j):
                queue.append((i+1, j))
                timeline_count[i+1][j] += timeline_count[i][j]
        elif tachyon_manifold[i][j] == "^":
            if is_move_possible(i+1, j-1):
                queue.append((i+1, j-1))
                timeline_count[i+1][j-1] += timeline_count[i][j]
            if is_move_possible(i+1, j+1):
                queue.append((i+1, j+1))
                timeline_count[i+1][j+1] += timeline_count[i][j]

    # for i in range(tachyon_manifold_shape[0]):
    #     print(" ".join([str(tc).zfill(2) for tc in timeline_count[i]]))

    print(sum(timeline_count[-1]))


if __name__ == "__main__":
    main()

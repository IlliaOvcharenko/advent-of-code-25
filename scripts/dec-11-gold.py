def main():
    fn = "inputs/aoc-25-dec-11.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    adj = {"out": set(), "fcc": set(), "svr": set(), "dac": set()}

    all_nodes = set()
    for l in lines:
        node, neighbours = l.split(":")
        node = node.strip()
        neighbours = [n.strip() for n in neighbours.strip().split(" ")]

        adj[node] = set(neighbours)
        all_nodes.add(node)
        all_nodes.update(set(neighbours))

    def cout_ways_out(node_from, node_to) -> int:
        num_of_pathes = {n: -1 for n in all_nodes}
        # print(num_of_pathes)
        def dfs(node) -> int:

            if node == node_to:
                return 1

            if num_of_pathes[node] == -1:
                num_of_pathes[node] = sum([
                    dfs(neighbour) for neighbour in adj[node]
                ])
            return num_of_pathes[node]
        return dfs(node_from)

    total_ways_out = 0

    # svr - fft - dac - out
    ways_svr_to_fft = cout_ways_out("svr", "fft")
    ways_fft_to_dac = cout_ways_out("fft", "dac")
    ways_dac_out = cout_ways_out("dac", "out")
    total_ways_out += (ways_svr_to_fft * ways_fft_to_dac * ways_dac_out)

    # svr - dac - fft - out
    ways_svr_to_dac = cout_ways_out("svr", "dac")
    ways_dac_to_fft = cout_ways_out("dac", "fft")
    ways_fft_out = cout_ways_out("fft", "out")
    total_ways_out += (ways_svr_to_dac * ways_dac_to_fft * ways_fft_out)
    print(total_ways_out)


if __name__ == "__main__":
    main()

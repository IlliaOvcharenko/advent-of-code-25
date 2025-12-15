def main():
    fn = "inputs/aoc-25-dec-11.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    adj = {}

    for l in lines:
        node, neighbours = l.split(":")
        node = node.strip()
        neighbours = [n.strip() for n in neighbours.strip().split(" ")]

        adj[node] = set(neighbours)

    num_of_pathes = {n: -1 for n in adj.keys()}
    def ask_for_num_of_pathes(node) -> int:

        if node == "out":
            return 1

        if num_of_pathes[node] == -1:
            num_of_pathes[node] = sum([
                ask_for_num_of_pathes(neighbour) 
                for neighbour in adj[node]
            ])
        return num_of_pathes[node]

    total_ways_out = ask_for_num_of_pathes("you")
    print(total_ways_out)






if __name__ == "__main__":
    main()

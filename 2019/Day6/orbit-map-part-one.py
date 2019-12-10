def parse_orbit_tree(lines):
    node_dict = {}
    for line in lines:
        parsed = line.strip().split(")")
        node_dict[parsed[1]] = parsed[0]
    return node_dict


def read_file():
    f = open("input.txt", "r")
    if f.mode == 'r':
        node_tree = parse_orbit_tree(f.readlines())
        return node_tree


def count_orbits(node_tree):
    count = 0
    for node in node_tree.keys():
        curr_node = node
        while curr_node in node_tree.keys():
            count += 1
            curr_node = node_tree[curr_node]
    return count


def get_route_to_root(node_tree, start):
    route = [start]
    node = start
    while node in node_tree.keys():
        route.append(node_tree[node])
        node = node_tree[node]
    return route


def find_route_to_san(node_tree, start, target):
    return len(set(get_route_to_root(node_tree, start)) ^ set(get_route_to_root(node_tree, target)) ^ {start, target})


def main():
    node_tree = read_file()
    print(count_orbits(node_tree))
    print(find_route_to_san(node_tree, 'YOU', 'SAN'))


if __name__ == "__main__":
    main()

from collections import defaultdict


def read_input(file_name):
    with open(file_name, 'r') as f:
        rules = [line for line in f]
        return rules


def parse_input(rules):
    graph = defaultdict(list)
    for rule in rules:
        node, edges = rule.split('contain')
        node_words = node.split()
        node_type = node_words[0] + node_words[1]
        graph[node_type] = []
        for edge in edges.strip().split(','):
            edge = edge.strip()
            if edge == 'no other bags.':
                continue
            words = edge.split(' ')
            count = int(words[0])
            name = words[1] + words[2]
            graph[node_type].append((count, name))

    return graph


def reverse_graph(graph):
    new_graph = defaultdict(list)
    for node, edges in graph.items():
        for edge in edges:
            count, name = edge
            new_graph[name].append((count, node))
    return new_graph


def dfs(graph, node, visited):
    if node in visited:
        return 0

    count = 1
    visited.add(node)

    for edge in graph[node]:
        _, name = edge
        count += dfs(graph, name, visited)

    return count


def dfs_2(graph, node):
    # Guaranteed to be tree
    tally = 0
    for edge in graph[node]:
        bags, name = edge
        to_add = bags + bags * dfs_2(graph, name)
        print('node {} edge {} to_add {}'.format(node,name,to_add))
        tally = tally + to_add

    return tally


if __name__ == '__main__':
    # rules = read_input('data/day7_test2.txt')
    # rules = read_input('data/day7_test.txt')
    rules = read_input('data/day7.txt')
    parsed_graph = parse_input(rules)
    reversed_graph = reverse_graph(parsed_graph)

    my_visited = set()
    val = dfs(reversed_graph, 'shinygold', my_visited)
    print(val - 1)
    val = dfs_2(parsed_graph, 'shinygold')
    print(val)

from random import sample

def find_cycle(graph, start_node):
    # Find cycle in the graph starting with start_node
    cycle = [start_node]
    node = start_node
    while True:
        sinks = graph[node]
        next_node = sample(sinks, 1)[0]
        if len(sinks) > 1:
            graph[node] = sinks - set([next_node])
        else:
            del(graph[node])
        cycle.append(next_node)
        node = next_node
        if node == start_node:
            break

    return cycle, graph

def node_degrees(graph):
    # Calculate indegree and outdegree of all the nodes in the graph
    in_degree = {}
    out_degree = {}

    for source in graph:
        if source not in in_degree:
            in_degree[source] = 0
        out_degree[source] = len(graph[source])
        for sink in graph[source]:
            if sink in in_degree:
                in_degree[sink] += 1
            else:
                in_degree[sink] = 1
            if sink not in out_degree:
                out_degree[sink] = 0

    return in_degree, out_degree

def find_endpoints(graph):
    in_degree, out_degree = node_degrees(graph)
    start_node, end_node = -1, -1

    for node in in_degree:
        ins, outs = in_degree[node], out_degree[node]
        # The start node must be that node which has an outdegree that is one greater than its indegree
        if outs == ins + 1:
            if start_node == -1:
                start_node = node
        # The start node must be that node which has an indegree that is one greater than its outdegree
        elif ins == outs + 1:
            if end_node == -1:
                end_node = node

    return start_node, end_node

def combine_cycles(cycle, index, new_cycle):
    cycle = cycle[:index] + new_cycle + cycle[index + 1:]
    return cycle

def find_eulerian_path(graph):
    start_node, end_node = find_endpoints(graph)
    if end_node in graph:
        graph[end_node].add(start_node)
    else:
        graph[end_node] = set([start_node])

    cycle, graph = find_cycle(graph, start_node)
    while graph:
        for i, start_node in enumerate(cycle):
            if start_node in graph:
                new_cycle, graph = find_cycle(graph, start_node)
                cycle = combine_cycles(cycle, i, new_cycle)
                break
    return cycle[:-1]

graph = {}

f = open('input.txt', 'r')
for line in f:
    line = line[:-1].split(' ')
    source = line[0]
    sinks  = line[2].split(',')
    graph[source] = set(sinks)
f.close()

eulerian_path = find_eulerian_path(graph)
f = open('output.txt', 'w')
f.write("%s\n" % ('->'.join(map(str,eulerian_path))))
f.close()

def complement(read):
    # Reverse complement of a read
    reverse_complement = ""
    for char in read:
        if char == 'A':
            reverse_complement += 'T'
        elif char == 'C':
            reverse_complement += 'G'
        elif char == 'G':
            reverse_complement += 'C'
        elif char == 'T':
            reverse_complement += 'A'

    return reverse_complement[::-1]

def construct_de_bruijn_graph(k1mers):
    # Construct de bruijn graph edges encoded by the k + 1 mers
    de_bruin_graph_edges = set()
    for k1mer in k1mers:
        de_bruin_graph_edges.add(k1mer)
        de_bruin_graph_edges.add(complement(k1mer))

    # Construct de bruijn graph edge nodes corresponding to k mers
    k1 = len(k1mers[0])
    edge = lambda element: '(' + node[0 : k1 - 1] + ', ' + node[1 : k1] + ')'
    de_bruin_graph_edge_nodes = [edge(node) for node in de_bruin_graph_edges]

    return de_bruin_graph_edge_nodes

k1mers = []

f = open('input.txt', 'r')
for line in f:
    k1mers.append(line[:-1])
f.close()

de_bruin_graph = construct_de_bruijn_graph(k1mers)
f = open('output.txt', 'w')
f.write("%s\n" % (''.join(de_bruin_graph)))
f.close()

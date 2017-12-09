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

def cyclic_superstring(kmers):
    # Compute cyclic superstring by constructing de bruin graph
    for k in xrange(1, len(kmers[0])):
        de_bruin_graph = set()
        for kmer in kmers:
            for i in xrange(k):
                de_bruin_graph.add(kmer[i : len(kmer) + i - k + 1])
                de_bruin_graph.add(complement(kmer[i : len(kmer) + i - k + 1]))

        k = len(list(de_bruin_graph)[0])
        edge = lambda elmmt: [elmt[0 : k - 1], elmt[1 : k]]
        de_bruin_graph_edges = [edge(elmt) for elmt in de_bruin_graph]

        cyclic_superstring = []
        for x in xrange(2):
            kmer = de_bruin_graph_edges.pop(0)
            cyclic = kmer[0][-1]
            while kmer[1] in [item[0] for item in de_bruin_graph_edges]:
                cyclic += kmer[1][-1]
                [index] = [i for i, pair in enumerate(de_bruin_graph_edges) if pair[0] == kmer[1]]
                kmer = de_bruin_graph_edges.pop(index)
            cyclic_superstring.append(cyclic)

        if len(de_bruin_graph_edges) == 0:
            break

    return cyclic_superstring[0]

kmers = []

f = open('input.txt', 'r')
for line in f:
    kmers.append(line[:-1])
f.close()

cyclic_superstring = cyclic_superstring(kmers)
f = open('output.txt', 'w')
f.write("%s\n" % (cyclic_superstring))
f.close()

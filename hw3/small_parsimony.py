from collections import defaultdict

alphabet = ['A', 'C', 'G', 'T']
parsimony_score = 0

class Node(object):
    def __init__(self, index, leaf):
        self.index = index
        self.leaf = leaf
        self.children = []
        self.edges = []
        self.text = ''
        self.score = defaultdict(int)
        self.scored = False

    def re_init(self):
        self.score = defaultdict(int)
        self.scored = False
        return None

    def is_ripe(self):
        if self.leaf:
            return True
        else:
            for i in self.children:
                if not node_list[i].scored:
                    return False
        return True

    def add_node(self, c_index):
        self.children.append(c_index)
        self.edges.append(0)

    def scoring(self, character):
        if self.leaf:
            for letter in alphabet:
                if letter == self.text[character]:
                    self.score[letter] = 0
                else:
                    self.score[letter] = float('inf')
        else:
            for letter in alphabet:
                for item in self.children:
                    self.score[letter] += min([node_list[item].score[i] + compare(letter, i) for i in alphabet])
        self.scored = True

def compare(a, b):
    if a == b:
        return 0
    else:
        return 1

def hamming_distance(a, b):
    count = 0
    for i in xrange(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def score_tree(character):
    for node in node_list:
        if node.leaf:
            node.scoring(character)
    while not node_list[-1].scored:
        for node in node_list:
            if not node.scored:
                if node.is_ripe():
                    node.scoring(character)

def prune_tree(node, parent_letter = ''):
    if node.leaf == False:
        min_value = float('inf')
        choice = ''
        for letter in alphabet:
            score = node.score[letter]
            if parent_letter != letter:
                score += 1
            if score < min_value:
                min_value = score
                choice = letter
        node.text += choice
        for i in node.children:
            prune_tree(node_list[i], choice)

def assign_score(node):
    global parsimony_score
    if node.leaf:
        return None
    for index, item in enumerate(node.children):
        dd = hamming_distance(node.text, node_list[item].text)
        parsimony_score += dd
        node.edges[index] = dd
        assign_score(node_list[item])

def get_adjacency_list(node, labels):
    for index, item in enumerate(node.children):
        child = node_list[item]
        labels.append(node.text + '->' + child.text + ':' + str(node.edges[index]))
        labels.append(child.text + '->' + node.text + ':' + str(node.edges[index]))
        get_adjacency_list(child, labels)

def small_parsimony():
    for char in xrange(len(node_list[0].text)):
        score_tree(char)
        prune_tree(node_list[-1])
        for node in node_list:
            node.re_init()
    assign_score(node_list[-1])
    labels = []
    get_adjacency_list(node_list[-1], labels)
    return labels

f = open('input.txt', 'r')
num_leaves = int(f.readline())
node_list = [Node(i, True) for i in xrange(num_leaves)]
for i, line in enumerate(f):
    line = line[:-1];
    line = line.split('->')
    node_number = int(line[0])
    if node_number == len(node_list):
        node_list.append(Node(node_number, False))
    if i < num_leaves:
        node_list[node_number].add_node(i)
        node_list[i].text = line[1]
    if i >= num_leaves:
        node_list[node_number].add_node(int(line[1]))
f.close()

tree_labels = small_parsimony()

f = open('output.txt', 'w')
f.write(str(parsimony_score) + '\n')
f.write("%s\n" % ('\n'.join(tree_labels)))
f.close()

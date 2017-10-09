def initialize_matrix(mat, s, t):
    # Initialize m * n matrix with 0 (m = length of s + 1, n = length of t + 1)
    for i in xrange(len(s) + 1):
        row = []
        for j in xrange(len(t) + 1):
            row.append(0)
        mat.append(row)

def base_case(mat, s, t):
    # Aligning i characters to 0 characters must use i gaps
    for i in xrange(len(s) + 1):
        mat[i][0] = i

    for i in xrange(len(t) + 1):
        mat[0][i] = i

def base_case_alignment(mat, s, t):
    # Aligning i characters to 0 characters must use i gaps
    for i in xrange(len(s) + 1):
        mat[i][0] = 1

    for i in xrange(len(t) + 1):
        mat[0][i] = 1

def match_cost(a, b):
    # Cost of match = 0, Cost of mismatch = 1
    if a == b:
        return 0
    else:
        return 1

def compute_opt(mat, alignment_count,  s, t):
    # Compute edit distance matrix and alignment count matrix
    modulo_base = 2**27 - 1

    for i in xrange(1, len(s) + 1):
        for j in xrange(1, len(t) + 1):
            choices = [
                1 + mat[i - 1][j],
                1 + mat[i][j - 1],
                match_cost(s[i - 1], t[j - 1]) + mat[i - 1][j - 1]
            ]
            mat[i][j] = min(choices)
            if mat[i][j] == choices[0]:
                alignment_count[i][j] += alignment_count[i - 1][j]
            if mat[i][j] == choices[1]:
                alignment_count[i][j] += alignment_count[i][j - 1]
            if mat[i][j] == choices[2]:
                alignment_count[i][j] += alignment_count[i - 1][j - 1]
            alignment_count[i][j] %= modulo_base

def count_optimal_alignments(s, t):
    # Compute optimal alignments
    mat = []
    initialize_matrix(mat, s, t)
    base_case(mat, s, t)

    alignment_count = []
    initialize_matrix(alignment_count, s, t)
    base_case_alignment(alignment_count, s, t)

    compute_opt(mat, alignment_count, s, t)

    return alignment_count[len(s)][len(t)]

proteins, i = ['', ''], -1

f = open('input.txt', 'r')
for line in f:
    if ">Rosalind_" in line:
        i = i + 1
    else:
        proteins[i] += line[:-1]
f.close()

s, t = proteins[0], proteins[1]

f = open('output.txt', 'w')
f.write(str(count_optimal_alignments(s, t)))
f.close()

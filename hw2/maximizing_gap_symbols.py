# score assigned to matched symbol(m) > 0
score_match = 1

# score assigned to mismatched non-gap symbol(d) < 0
score_mismatch = -10

# score assigned a symbol matched to a gap symbol '-'
score_gap = -1

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
        mat[i][0] = i * score_gap

    for i in xrange(len(t) + 1):
        mat[0][i] = i * score_gap

def base_case_max_gap(mat, s, t):
    # Aligning i characters to 0 characters must use i gaps
    for i in xrange(len(s) + 1):
        mat[i][0] = i

    for i in xrange(len(t) + 1):
        mat[0][i] = i

def match_cost(a, b):
    # Cost of match = 0, Cost of mismatch = 1
    if a == b:
        return score_match
    else:
        return score_mismatch

def compute_opt(edit_distance, max_gap, s, t):
    # Compute edit distance matrix and alignment path matrix
    for i in xrange(1, len(s) + 1):
        for j in xrange(1, len(t) + 1):
            choices = [
                score_gap + edit_distance[i - 1][j],
                score_gap + edit_distance[i][j - 1],
                match_cost(s[i - 1], t[j - 1]) + edit_distance[i - 1][j - 1]
            ]
            edit_distance[i][j] = max(choices)
            if edit_distance[i][j] == choices[0]:       # If top, add a gap
                max_gap[i][j] = 1 + max_gap[i - 1][j]
            elif edit_distance[i][j] == choices[1]:     # If left, add a gap
                max_gap[i][j] = 1 + max_gap[i][j - 1]
            elif edit_distance[i][j] == choices[2]:     # If a diagonal, do not add gap
                max_gap[i][j] = max_gap[i - 1][j - 1]

def maximum_gap_symbols(s, t):
    # Compute edit distance alignment
    edit_distance = []
    initialize_matrix(edit_distance, s, t)
    base_case(edit_distance, s, t)

    max_gap = []
    initialize_matrix(max_gap, s, t)
    base_case_max_gap(max_gap, s, t)

    compute_opt(edit_distance, max_gap, s, t)

    return max_gap[len(s)][len(t)]

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
f.write(str(maximum_gap_symbols(s, t)))
f.close()
